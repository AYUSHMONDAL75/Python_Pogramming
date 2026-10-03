num = []
n = int(input("Enter number of terms: "))
for i in range(n):
    number = int(input(f"Enter {i + 1} number: "))
    num.append(number)
max_num = num[0]
min_num = num[0]
for i in range(1, n):
    if max_num < num[i]:
        max_num = num[i]
    if num[i] < min_num:
        min_num = num[i]
print("\nMaximum number =", max_num)
print("Minimum number =", min_num)