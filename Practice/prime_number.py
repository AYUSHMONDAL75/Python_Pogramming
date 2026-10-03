n = int(input("Enter a number: "))
def is_prime(n, i=2):
    if n <= 1:
        return False
    if i * i > n:
        return True
    if n % i == 0:
        return False
    return is_prime(n, i + 1)
if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")