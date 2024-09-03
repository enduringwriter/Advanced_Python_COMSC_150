def main():
    """
    Calculate and store the remainder of a user defined number by
    dividing the number by 2 until the remainder is less than 2
    (which means the remainder is either 1 or 0).
    The program calculates the binary representation of a number.
    """

    number = int(input('Enter your input: '))
    result = []

    while number > 0:
        remainder = number%2
        # print(remainder)
        result.append(remainder)
        # print(result)
        number = number//2

    print(*result)
    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
