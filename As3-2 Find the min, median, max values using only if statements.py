def main():
    
    """_summary_
    Get three numbers from the user and print them in ascending order.
    Use only if statements to find the min, median, and max values.
    """
    
    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))
    num3 = int(input('Enter the third number: '))
    
    if num1 > num2 > num3:
        minval = num3
        median = num2
        maxval = num1
    elif num1 > num3 > num2:
        minval, median, maxval = num2, num3, num1
    elif num2 > num1 > num3:
        minval, median, maxval = num3, num1, num2
    elif num2 > num3 > num1:
        minval, median, maxval = num1, num3, num2
    elif num3 > num1 > num2:
        minval, median, maxval = num2, num1, num3
    else:
        minval = num1, median = num2, maxval = num3   

    print(minval, median, maxval)
    ########################################
    # Do not delete the return statement
    ########################################
    return minval, median, maxval


if __name__ == '__main__':
    main()
