def list_of_multiples (num, length):
	lis = list()
	for i in range(1,length + 1):
		lis.append(num*i)	
	return lis

print(list_of_multiples(7, 5))