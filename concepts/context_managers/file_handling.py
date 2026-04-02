def write_file():
    names = ['John', 'Jane', 'Doe']

    with open("names.txt", "w") as f:
        for name in names:
            f.write(name + "\n")


def read_file():
    with open("names.txt", "r") as f:
        return f.read()


if __name__ == "__main__":
    write_file()
    print(read_file())
