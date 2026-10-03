x = input("Enter 1st list: ")
y = input("Enter 2nd list: ")
print(f"union of two list: {sorted((list(set(x) | set(y))))}")