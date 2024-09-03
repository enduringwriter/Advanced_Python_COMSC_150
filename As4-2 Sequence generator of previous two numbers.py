def main():
    """
    Generate a sequence of numbers where each number is the sum of the previous two numbers.
    The user provides the number, N, of sequence values.
    """

    result = []
    a1 = int(input('Enter your first number: '))
    a2 = int(input('Enter your second number: '))
    N = int(input('Enter the number of sequences: '))
    result.append(a1)
    result.append(a2)
    
    for i in range(N-2):
        x=result[-2]
        y=result[-1]
        sum=x+y
        result.append(sum)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
