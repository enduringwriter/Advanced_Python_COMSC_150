import random

## assumption that the number is greater than 1

def isPrime(number):
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return number

def gen_primes(numbers):
    prime_list = []
    for number in range(2,numbers):
    #     prime_check = isPrime(number)
    #     if prime_check:
    #         prime_list.append(prime_check)
    # return prime_list

    # or use yield
        if isPrime(number):
            yield number

def main():
    N = 20
    primes = gen_primes(N)
    print('This is the generator: ', primes)
    print('primes : ', list(primes))

    N = 30
    primes = gen_primes(N)
    print('This is the generator: ', primes)
    print('primes : ', list(primes))


if __name__ == '__main__':
    main()
