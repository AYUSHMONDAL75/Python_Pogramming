std1 = {}
std2 = {}
n = int(input("Enter number of elements: "))

print("\nFor 1st student data collection")
for i in range (n):
    key = input("Enter name: ")
    value = input("Enter age: ")
    std1[key] = value

print("\nFor 2nd student data collection")
for i in range (n):
    key = input("Enter name: ")
    value = input("Enter age: ")
    std2[key] = value

std1.update(std2)
print("\nMargeof two students data collection is: ",std1)  

print("\nSorted by Value")
items = dict(sorted(std1.items(), key = lambda key: key[1]))
print(items)