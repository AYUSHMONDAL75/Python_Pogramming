num = []
n = int(input("Enter number of terms: "))
for i in range (n):
    number = float(input(f"Enter {i+1} number: "))
    num.append(number)
print(f"Maximum number is {max(num)}")
print(f"Minimum number is {min(num)}")