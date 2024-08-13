def is_prime(n, i=2):
    if n <= 2:
        return n == 2
    if n % i == 0:
        return False
    if i * i > n:
        return True
    return is_prime(n, i + 1)

def print_primes(n):
    if n < 2:
        return
    print_primes(n - 1)
    if is_prime(n):
        print(n)


number = 20
print_primes(number)
