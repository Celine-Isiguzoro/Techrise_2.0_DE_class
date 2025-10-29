def is_prime(number):
    if number < 2:
        return False
    
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
    
    return True

def find_primes(start, end):
    primes = []
    current = start
    
    while current <= end:
        if is_prime(current):
            primes.append(current)
        current += 1
    
    return primes

print(find_primes(1, 20))