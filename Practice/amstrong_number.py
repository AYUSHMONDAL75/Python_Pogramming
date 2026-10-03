x = int(input("Enter a number checking Amstrong: "))
temp = x
sum = 0
while(x > 0):
    rem = x % 10
    sum = sum + (rem * rem * rem)
    x = x // 10
if(temp == sum):
    print(f"{sum} is a Amstrong Number")
else:
    print(f"{sum} is not a Amstrong Number")