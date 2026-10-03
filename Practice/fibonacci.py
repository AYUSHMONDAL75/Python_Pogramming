x = int(input("Enternumber of term: "))
a = 0
b = 1
print("Fibonacci series is: ")
for i in range (x):
    print(a, end = " ")
    c = a + b
    a = b
    b = c