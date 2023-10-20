import functools

# 1. Caching results to improve performance with `lru_cache`.
@functools.lru_cache(maxsize=128)
def expensive_function(n):
    # ... expensive calculations ...
    return result

# 2. Creating partial functions with `partial`.
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)  # Create a square function.

# 3. Changing the order of arguments with `partial`.
divide = partial(power, exponent=-1)  # Create a division function.

# 4. Comparing objects with `cmp_to_key`.
from functools import cmp_to_key

sorted_list = sorted(my_list, key=cmp_to_key(compare_function))

# 5. Memoization with `lru_cache`.
@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# 6. Function composition with `reduce`.
from functools import reduce

result = reduce(lambda x, f: f(x), [func1, func2, func3], initial_value)

# 7. Timeout for function execution with `timeout`.
from functools import timeout

@timeout(5)  # Set a timeout of 5 seconds.
def long_running_function():
    # ...

# 8. Partial ordering with `total_ordering`.
from functools import total_ordering

@total_ordering
class MyClass:
    def __eq__(self, other):
        # ...

    def __lt__(self, other):
        # ...

# 9. Function wrappers and decorators with `wraps`.
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # ...
    return wrapper

# 10. Counting function calls with `wraps` and a decorator.
def count_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.call_count += 1
        return func(*args, **kwargs)
    wrapper.call_count = 0
    return wrapper

@count_calls
def my_function():
    # ...

# You can access the call count with `my_function.call_count`.
