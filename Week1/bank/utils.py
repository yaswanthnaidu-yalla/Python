import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args,**kwargs)

        end_time = time.time()
        print(f"{func.__name__} excecuted in {end_time-start_time:.6f} seconds")
        return result
    return wrapper
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing: {func.__name__}")
        print(f"  args:{args},kwargs:{kwargs}")
        result=func(*args, **kwargs)

        print(result)
        return result
    return wrapper
def retry(max_attempts=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args,**kwargs):
            for attempt in range(1, max_attempts+1):
                try:
                    return func(*args,**kwargs)
                except Exception as e:
                    print(f"Attempt{attempt}/{max_attempts}failed for {func.__name__}:{e}")
                    if attempt==max_attempts:
                        print("Max tries reached, failed permanently.")
                        raise e
            return wrapper
        return decorator
            
def transaction_history(filepath="data/transaction.log"):
    try:
        with open(filepath, "r") as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        yield "No transaction history found."