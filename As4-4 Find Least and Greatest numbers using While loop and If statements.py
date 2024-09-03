def main():
    """
    Find the least and greatest values of a list of 5 user input values,
    without using sorted(), min(), or max() functions.
    Assume the values inputted are integers.
    """
    numbers = []
    maxval = 0
    minval = float('inf')

    while len(numbers) < 5:
        num = int(input('Enter value: '))
        if num > maxval:
            maxval = num
        if num < minval:
            minval = num
        numbers.append(num)

    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
