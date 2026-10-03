x = input("Enter a String For checking Palindrome: ")
if str(x) == str(x)[::-1]:
    print(f"{x} Is a palindrome string")
else:
    print(f"{x} Is not a palindrome string")