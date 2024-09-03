def main():
    """
    Count the number of even cluseters with at least 2 or more from the list of 10 user input values.
    
    Assumptions: None.
    """
    
    number = []
    evencnt = 0

    for i in range(10):
        number.append(int(input('Enter a number: ')))
         
    for i in range(10):
        if number[i] % 2 == 0 and number[i-1] % 2 == 0:
            if i==1 or number[i-2] % 2 != 0:
                evencnt += 1
    
    print(evencnt)

    ########################################
    # Do not delete the return statement
    ########################################
    return evencnt


if __name__ == '__main__':
    main()
