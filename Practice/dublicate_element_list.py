num = []
n = int(input("Enter number of terms: "))
for i in range(n):
    number = int(input(f"Enter number {i + 1}: "))
    num.append(number)

print("Duplicate elements:")
for i in range(n):
    for j in range(i + 1, n):
        if num[i] == num[j]:
            print(num[i], end=" ")
            break