import math
n, p, r = map(int, input("Enter three integer numbers: ").split())
print(f"\nGCD of given numbers is: {math.gcd(n, p, r)}")
print(f"\nLCM of given numbers is: {math.lcm(n, p, r)}")