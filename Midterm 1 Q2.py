def main():
    """
    Find the longest and short words in a user input stream without using a list.
    The program stops when the use enters 'stop'.
    """

    longest = shortest = ''
    # can use shortest "a"*10000 or can setup within while loop

    while True:
        string = input('Enter string, type "stop" to quit the program: ')

        if not shortest:
            shortest = string

        if string.lower() == 'stop':
            break
        if len(string) > len(longest):
            longest = string
        if len(string) < len(shortest):
            shortest = string

    ########################################
    # Do not delete the return statement
    ########################################
    return longest, shortest
##


if __name__ == '__main__':
    main()
