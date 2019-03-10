def calculation_total(numbers):
    total = 0

    for num in numbers:
        total += num

    return total


def calculation_max(numbers):
    max = 0

    for num in numbers:
        if num > max:
            max = num

    return max


def calculation_min(numbers):
    min = numbers[0]

    for num in numbers:
        if num < min:
            min = num

    return min
