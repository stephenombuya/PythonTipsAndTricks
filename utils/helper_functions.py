from collections import Counter
import time
import sys


def flatten_list(nested_list):
    return [item for sublist in nested_list for item in sublist]


def most_frequent_element(data):
    return Counter(data).most_common(1)[0]


def swap_values(x, y):
    return y, x


def memory_size(obj):
    return sys.getsizeof(obj)


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} executed in {end - start:.4f}s")
        return result
    return wrapper
