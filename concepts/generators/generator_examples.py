def number_generator(n):
    for i in range(n):
        yield i


def return_vs_yield(n):
    def with_return():
        for i in range(n):
            return i

    def with_yield():
        for i in range(n):
            yield i

    return with_return(), list(with_yield())


if __name__ == "__main__":
    print(list(number_generator(5)))
    print(return_vs_yield(5))
