my_str=input("Enter the string to check whether its a palindrome or not")

chk_str = reversed(my_str)

if list(my_str) == list(chk_str):
    print("its a palindrome")
else:
    print("Not a palindrome")

print(list(my_str))
print(chk_str)
