str = "Ayush-is-a-good-boy"

sum = "1 + 2 + 3 + 4"
str1 = "a"
str2 = "aa"
print(f"Lower case of {str} is {str.lower()}")
print(f"Upper case of {str} is {str.upper()}")

print(list(str)[::-1])

str= "".join(str[::-1])
print(str)
print(eval(sum))
print("ayush, mondal".isalnum())
print("".join(set(str2) - set(str1)))