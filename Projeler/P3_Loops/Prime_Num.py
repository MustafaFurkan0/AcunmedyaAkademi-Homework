# 1’den 100’e kadar olan tüm asal sayıları bulan program

def prime_num():
    primes = []
    for i in range(2,101):
        is_prime = True
        for j in range(2,int(i**0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

print(prime_num())  