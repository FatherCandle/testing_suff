import time
import functools

# Run time decorator
def RuntimePrinter(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter()
        print(f"Finished in {round(finish-start, 2)} second(s)")
        return result

    return wrapper
