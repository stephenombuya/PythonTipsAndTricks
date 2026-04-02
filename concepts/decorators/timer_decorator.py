import time


def timer(func):
    def inner(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time: {end - start:.4f}s")
        return result
    return inner


@timer
def heavy_task():
    return [i**2 for i in range(1_000_000)]


if __name__ == "__main__":
    heavy_task()
