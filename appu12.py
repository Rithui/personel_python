
#this code is fir the palindrome number check
string = 'amaama'
half = int(len(string) / 2)


first_str = string[:half]
second_str = string[half:]


if first_str == second_str:
	print(string, 'string is symmetrical')
else:
	print(string, 'string is not symmetrical')

if first_str == second_str[::-1]: # ''.join(reversed(second_str)) [slower]
	print(string, 'string is palindrome')
else:
	print(string, 'string is not palindrome')
