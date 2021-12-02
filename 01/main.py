import fileinput


def one(data):
    total = len(data)
    counter = 0
    pos = 0

    while pos < total:
        if data[pos] > data[pos-1]:
            counter += 1

        pos += 1

    print(f"First Puzzle Answer: {counter}.")


def two(data):
    total = len(data)
    counter = 0
    pos = 0

    while pos+3 < total:
        if data[pos] + data[pos+1] + data[pos+2] < data[pos+1] + data[pos+2] + data[pos+3]:
            counter += 1

        pos += 1

    print(f"Second Puzzle Answer: {counter}.")


def main():
    data = ([int(x.strip()) for x in fileinput.input()])

    one(data)
    two(data)


if __name__ == "__main__":
    main()
