x = int(input("Enter a number checking Palindrome are not: "))
temp = x
sum = 0
while(x > 0):
    rem = x % 10
    sum = sum * 10 + rem
    x = x // 10
if(temp == sum):
    print(f"{sum} is a palindrome Number")
else:
    print(f"{sum} is not a palindrome Number")
