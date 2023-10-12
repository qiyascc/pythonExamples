is_palindrome = lambda num: str(num) == str(num)[::-1]
is_prime = lambda num: num > 1 and all(num % i != 0 for i in range(2, int(num**0.5) + 1))

palindromes = [num for num in range(1, 1001) if is_palindrome(num)]
primes = [num for num in range(1, 1001) if is_prime(num)]

print("Polindroms:", palindromes)
print("Primes: ", primes)
