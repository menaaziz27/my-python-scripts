inp = input()
lis = [False]*5

for letter in inp:
	if letter.isalnum():
		lis[0] = True
	if letter.isalpha():
		lis[1] = True
	if letter.isdigit():
		lis[2] = True
	if letter.islower():
		lis[3] = True
	if letter.isupper():
		lis[4] = True

print(lis[0])
print(lis[1])
print(lis[2])
print(lis[3])
print(lis[4])