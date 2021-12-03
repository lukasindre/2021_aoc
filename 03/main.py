import fileinput
from collections import Counter


def commons(which, data):
    if which == "MOST":
        most_common = []
        for x in range(12):
            nums = [y[x] for y in data]
            most_common.append(Counter(nums).most_common(1)[0][0])
        return most_common
    else:
        least_common = []
        for x in range(12):
            nums = [y[x] for y in data]
            least_common.append(Counter(nums).most_common()[:-1-1:-1][0][0])
        return least_common


def retrieve_starting_nums(nums, position, rating):
    zero_count = []
    one_count = []
    for num in nums:
        pos_bit = str(num)[position]
        if pos_bit == '0':
            zero_count.append(num)
        else:
            one_count.append(num)

    if len(one_count) == len(zero_count) and rating == "OXYGEN":
        return one_count
    elif len(one_count) > len(zero_count) and rating == "OXYGEN":
        return one_count
    elif len(one_count) < len(zero_count) and rating == "OXYGEN":
        return zero_count
    elif len(one_count) == len(zero_count) and rating == "CO2":
        return zero_count
    elif len(one_count) > len(zero_count) and rating == "CO2":
        return zero_count
    elif len(one_count) < len(zero_count) and rating == "CO2":
        return one_count


def one(most, least):
    most_common = most
    least_common = least
    print(f"First Puzzle Answer: {int(''.join(most_common),2) * int(''.join(least_common),2)}.")


def two(nums):
    total = None
    position = 0
    starting_nums = nums
    while total != 1 and position < 12:
        starting_nums = retrieve_starting_nums(starting_nums, position, "OXYGEN")
        total = len(starting_nums)
        position += 1
    oxygen = int(starting_nums[0],2)

    total = None
    position = 0
    starting_nums = nums
    while total != 1 and position < 12:
        starting_nums = retrieve_starting_nums(starting_nums, position, "CO2")
        total = len(starting_nums)
        position += 1
    co2 = int(starting_nums[0],2)

    print(f"Puzzle Two Answer: {oxygen * co2}.")


def main():
    data = [x.strip() for x in fileinput.input()]
    most_common = commons("MOST", data)
    least_common = commons("LEAST", data)
    one(most_common, least_common)
    two(data)


if __name__ == "__main__":
    main()
