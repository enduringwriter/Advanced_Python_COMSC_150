def main():
    """
    Email address validation.
    """
    
    email = input('Enter your email: ')

    num = email.find('@')
    if email[0].isalpha() and 5<len(email)<30 and num!=-1 and email[num+1:].find('.')>0:
        result = True
    else:
        result = False

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
