import fileinput


def one(data):
    horizontal = 0
    depth = 0
    for movement in data:
        if movement[0] == 'forward':
            horizontal += int(movement[1])
        elif movement[0] == 'up':
            depth -= int(movement[1])
        elif movement[0] == 'down':
            depth += int(movement[1])
    print(f"Puzzle one answer: {depth * horizontal}.")


def two(data):
    horizontal = 0
    depth = 0
    aim = 0
    for movement in data:
        if movement[0] == 'forward':
            horizontal += int(movement[1])
            depth += aim * int(movement[1])
        elif movement[0] == 'up':
            aim -= int(movement[1])
        elif movement[0] == 'down':
            aim += int(movement[1])
    print(f"Puzzle two answer: {depth * horizontal}.")


def main():
    data = [x.strip().split(' ') for x in fileinput.input()]
    one(data)
    two(data)


if __name__ == "__main__":
    main()
