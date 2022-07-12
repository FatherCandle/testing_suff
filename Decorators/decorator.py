import functools

# Basic decorator
def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")
        return result

    return wrapper


@start_end_decorator
def do_stuff(x: int, key_word: str):
    num = x * 5
    print(key_word)
    return num


# Decorator that uses an argument (implement by defining another func wrapping the decorator)
def repeat(num_times):
    def repeat_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result

        return wrapper

    return repeat_decorator


# Using multiple decorators for the same function
@repeat(num_times=3)
def greet(name: str):
    print(f"Hello: {name}")


def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__!r} returned {result!r}")
        return result

    return wrapper


@debug
@start_end_decorator
def say_hello(name: str):
    gretting = f"Hello: {name}"
    print(gretting)
    return gretting


# Using a class decorator (useful for saving state)
class CountCalls:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print(f"This is executed {self.num_calls} times")
        return self.func(*args, **kwargs)


@CountCalls
def say_hi():
    print("Hi")


def main():
    # Testing basic decorator
    result = do_stuff(5, "wow")
    print(result)

    # Testing decorator with arguments
    greet("Motherfucker")

    # Testing using multiple decorators
    say_hello("boga")

    # Testing class decorator
    say_hi()
    say_hi()


if __name__ == "__main__":
    main()
