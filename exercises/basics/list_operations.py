def sort_lists():
    list1 = [2, 5, 6, 8, 1, 8, 9, 11]
    list2 = ["Kenya", "USA", "Tanzania", "Egypt", "Cambodia"]

    list1.sort(reverse=True)
    list2.sort(reverse=True)

    return list1, list2


def flatten_example():
    nested = [[1, 2, 3], [4, 5, 6]]
    return [i for j in nested for i in j]


def list_formatting():
    numbers = [3452735, 4272538]
    return [f"{num:,}" for num in numbers]


if __name__ == "__main__":
    print(sort_lists())
    print(flatten_example())
    print(list_formatting())
