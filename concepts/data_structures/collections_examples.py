from collections import Counter


def count_elements():
    data = ['John', 'Kelly', 'Peter', 'Kelly']
    return Counter(data)


def most_common():
    data = "recklessness"
    return Counter(data).most_common(1)


if __name__ == "__main__":
    print(count_elements())
    print(most_common())
