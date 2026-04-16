"""
Modulo per il monitoraggio delle performance (Tempo e Token) di RLM.
"""
import time
import litellm


class PerformanceMonitor:
    def __init__(self):
        self.global_start = None
        self.global_end = None

    def start_execution(self):
        self.global_start = time.perf_counter()

    def stop_execution(self):
        self.global_end = time.perf_counter()
        return self.global_end - self.global_start


class StepTimer:
    def __init__(self):
        self.start_time = None
        self.elapsed = 0.0

    def __enter__(self):
        self.start_time = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.elapsed = time.perf_counter() - self.start_time


class LitellmTokenTracker:
    """
    Ascolta passivamente tutte le chiamate fatte da LiteLLM
    e accumula i token per ogni step ricorsivo.
    """

    def __init__(self):
        self.total_tokens = 0
        self.step_tokens = 0

    def reset_step(self):
        self.step_tokens = 0

    def track(self, kwargs, completion_response, start_time, end_time):
        try:
            tokens = 0
            # Cerca l'oggetto usage standard
            usage = getattr(completion_response, 'usage', None)
            if usage:
                tokens = getattr(usage, 'total_tokens', 0)
                if tokens == 0:
                    tokens = getattr(usage, 'prompt_tokens', 0) + getattr(usage, 'completion_tokens', 0)

            # Fallback se è un dizionario
            elif isinstance(completion_response, dict) and 'usage' in completion_response:
                u_dict = completion_response['usage']
                tokens = u_dict.get('total_tokens', 0) or (
                            u_dict.get('prompt_tokens', 0) + u_dict.get('completion_tokens', 0))

            self.total_tokens += tokens
            self.step_tokens += tokens
        except Exception:
            pass


# Istanza globale del tracker per l'intero progetto
token_tracker = LitellmTokenTracker()


def setup_token_tracking():
    """Aggancia il tracker agli eventi di successo di LiteLLM."""
    if token_tracker.track not in litellm.success_callback:
        litellm.success_callback.append(token_tracker.track)