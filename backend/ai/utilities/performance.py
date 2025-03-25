import time
from typing import Callable

def check_performance(func: Callable) -> Callable:
    """Decoratore per misurare le prestazioni"""
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"⏱️ Tempo esecuzione {func.__name__}: {end-start:.4f} secondi")
        return result
    return wrapper
