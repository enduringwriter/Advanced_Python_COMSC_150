def main():
    """
    Alphabet range generator with input validation.
    Assumptions: all inputs are lowercase
    """

    result = []
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
    
        if not (start.isalpha() and end.isalpha()):
            print('Input error')
            continue
        if ord(start) > ord(end):
            print('Input error. End letter must be greater or equal to start letter')
            continue
        break
    
    for i in range(ord(start), ord(end)+1):
        result.append(chr(i))
       
    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
