rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
a = []
b = []
c = []

print("Enter first matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    a.append(row)

print("Enter second matrix:")
for i in range(rows):
    row = list(map(int, input().split()))
    b.append(row)

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(a[i][j] + b[i][j])
    c.append(row)

print("\nResultant of two Matrixs:")
for i in range(rows):
    print(*c[i])