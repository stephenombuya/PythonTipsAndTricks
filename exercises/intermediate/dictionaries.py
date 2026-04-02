def merge_dictionaries():
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    return dict1 | dict2


def dictionary_comprehension():
    data = {'height': 70, 'weight': 50}
    return {k: float(v) for k, v in data.items()}


def access_keys(data):
    return set(data.keys())


if __name__ == "__main__":
    print(merge_dictionaries())
