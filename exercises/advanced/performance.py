import timeit
import sys


def compare_generator_vs_list():
    gen_time = timeit.timeit(
        'sum((num**2 for num in range(10000)))', number=1000
    )

    list_time = timeit.timeit(
        'sum([num**2 for num in range(10000)])', number=1000
    )

    gen_mem = sys.getsizeof((num**2 for num in range(10000)))
    list_mem = sys.getsizeof([num**2 for num in range(10000)])

    return {
        "generator_time": gen_time,
        "list_time": list_time,
        "generator_memory": gen_mem,
        "list_memory": list_mem,
    }


if __name__ == "__main__":
    print(compare_generator_vs_list())
