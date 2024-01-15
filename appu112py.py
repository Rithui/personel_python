string="The geeks for geeks"
half=int(len(string)/2)
first_str=string[:half]
second_str=string[half:]
if first_str==second_str:
    print(string,"the string is symmetric")
else:
    print(string,"the string is not symmetric")

if first_string==second_string[::-1]:
    print(string,"the string is palindrome")

else:
    print(string,"the string is not palindrome")
