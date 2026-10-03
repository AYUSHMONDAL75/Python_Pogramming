d = {} 
n = int(input("Enter number of terms: "))
for i in range(n):
    num = input("Enter name: ")
    age = int(input("Enter age: "))
    dept = input("Enter depertment: ")
    d = {
        'name': num, 
        'age': age,
        'dept': dept
    }
print(d)