"""Core RLM implementation using Datapizza AI."""

import asyncio
from typing import Optional, Dict, Any

from datapizza.clients.openai_like import OpenAILikeClient
from datapizza.memory import Memory
from datapizza.type import TextBlock, ROLE

from .types import CompletionResult
from .repl import REPLExecutor, REPLError
from .prompts import build_system_prompt, build_user_prompt
from .parser import parse_response, is_final

class RLMError(Exception):
    pass

class MaxIterationsError(RLMError):
    pass

class MaxDepthError(RLMError):
    pass

class RLM:
    """Recursive Language Model powered by Datapizza AI."""

    def __init__(
        self,
        model: str,
        recursive_model: Optional[str] = None,
        api_base: Optional[str] = None,
        api_key: Optional[str] = None,
        max_depth: int = 5,
        max_iterations: int = 30,
        _current_depth: int = 0,
        **llm_kwargs: Any
    ):
        self.model = model
        self.recursive_model = recursive_model or model
        self.api_base = api_base or "http://localhost:11434/v1"
        self.api_key = api_key or "ollama"
        self.max_depth = max_depth
        self.max_iterations = max_iterations
        self._current_depth = _current_depth
        self.llm_kwargs = llm_kwargs

        # Statistiche Interne
        self._llm_calls = 0
        self._iterations = 0
        self._total_tokens = 0

    def _create_env(self, context: str, query: str) -> Dict[str, Any]:
        """Create REPL environment with recursive capabilities."""
        async def recursive_llm(sub_query: str, sub_context: str) -> str:
            if self._current_depth >= self.max_depth:
                return "Error: Maximum recursion depth exceeded."

            sub_rlm = RLM(
                model=self.recursive_model,
                recursive_model=self.recursive_model,
                api_base=self.api_base,
                api_key=self.api_key,
                max_depth=self.max_depth,
                max_iterations=self.max_iterations,
                _current_depth=self._current_depth + 1,
                **self.llm_kwargs
            )

            result = await sub_rlm.acomplete(sub_query, sub_context)
            # Accumula i token dai sotto-livelli ricorsivi al livello principale
            self._total_tokens += sub_rlm.stats.get('total_tokens', 0)
            return result['answer']

        def sync_recursive_llm(sub_query: str, sub_context: str) -> str:
            try:
                loop = asyncio.get_running_loop()
                import concurrent.futures
                with concurrent.futures.ThreadPoolExecutor() as executor:
                    future = executor.submit(asyncio.run, recursive_llm(sub_query, sub_context))
                    return future.result()
            except RuntimeError:
                return asyncio.run(recursive_llm(sub_query, sub_context))

        return {
            'context': context,
            'query': query,
            'recursive_llm': sync_recursive_llm
        }

    async def acomplete(self, query: str, context: str) -> CompletionResult:
        env = self._create_env(context, query)
        repl = REPLExecutor(timeout=self.llm_kwargs.get('timeout', 5), max_output_chars=10_000)

        system_prompt = build_system_prompt(len(context), self._current_depth)

        # Inizializzazione Client Datapizza
        client = OpenAILikeClient(
            api_key=self.api_key,
            model=self.model,
            system_prompt=system_prompt,
            base_url=self.api_base
        )

        memory = Memory()
        current_query = build_user_prompt(query)

        for iteration in range(self.max_iterations):
            self._iterations += 1
            self._llm_calls += 1

            try:
                # Chiamata sincrona a Datapizza racchiusa in un thread per non bloccare async
                response = await asyncio.to_thread(client.invoke, current_query, memory=memory)
                llm_text = response.text if hasattr(response, 'text') else str(response)

                # --- ESTRAZIONE TOKEN DATAPIZZA + EURISTICA OLLAMA ---
                tokens = 0
                if hasattr(response, 'usage') and response.usage:
                    tokens = getattr(response.usage, 'total_tokens', 0)
                    if tokens == 0:
                        tokens = getattr(response.usage, 'prompt_tokens', 0) + getattr(response.usage, 'completion_tokens', 0)
                if tokens == 0:
                    tokens = getattr(response, 'prompt_tokens_used', 0) + getattr(response, 'completion_tokens_used', 0)

                # Fallback in caso di stream/API difettosa
                if tokens == 0:
                    input_len = len(current_query) + sum(len(str(t.content)) for t in memory.turns) + len(system_prompt)
                    tokens = (input_len + len(llm_text)) // 4

                self._total_tokens += int(tokens)

            except Exception as e:
                raise RLMError(f"LLM call failed: {str(e)}")

            # Aggiornamento manuale della cronologia della chat per Datapizza
            memory.add_turn(TextBlock(content=current_query), role=ROLE.USER)
            memory.add_turn(TextBlock(content=llm_text), role=ROLE.ASSISTANT)

            # Controlla se la risposta è finale
            if is_final(llm_text):
                answer = parse_response(llm_text, env)
                if answer is not None:
                    return {
                        "answer": answer,
                        "iterations": self._iterations,
                        "depth": self._current_depth,
                        "llm_calls": self._llm_calls,
                        "total_tokens": self._total_tokens
                    }

            # Se non è finale, estrae ed esegue il codice Python nel REPL
            try:
                execution_result = repl.execute(llm_text, env)
            except Exception as e:
                execution_result = f"Error: {e}"

            # Passa l'output del REPL alla prossima iterazione
            current_query = f"REPL OUTPUT:\n{execution_result}\n\nWhat is your next step?"

        raise MaxIterationsError(f"Exceeded max iterations ({self.max_iterations})")

    def complete(self, query: str, context: str) -> str:
        """Wrapper Sincrono: Restituisce la risposta e popola le stats."""
        self._llm_calls = 0
        self._iterations = 0
        self._total_tokens = 0

        try:
            result = asyncio.run(self.acomplete(query, context))
            return result["answer"]
        except Exception as e:
            return f"Error: {e}"

    @property
    def stats(self) -> Dict[str, int]:
        """Restituisce le metriche dell'ultima esecuzione."""
        return {
            'llm_calls': self._llm_calls,
            'iterations': self._iterations,
            'depth': self._current_depth,
            'total_tokens': self._total_tokens
        }