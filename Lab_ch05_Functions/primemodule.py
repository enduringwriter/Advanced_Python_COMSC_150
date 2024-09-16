def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # or use math.isqrt(n) or use int(math.sqrt(n))
        if n % i == 0:
            return False  # number is not a prime number
    return True


def print_primes(n):
    for i in range(2, n):
        if is_prime(i):
            print(i, end='\t')


def get_primes(n):
    prime_numbers = []
    for i in range(2, n):
        if is_prime(i):
            prime_numbers.append(i)
    return prime_numbers
