# def name_shuffle(txt):
# 	names = txt.split()
# 	lis = list()
# 	lis.append(names[1])
# 	lis.append(names[0])
# 	newStr = ' '.join(lis)
# 	return newStr

#----------------------------

# def name_shuffle(str):
# 	a, b =str.split()
# 	return b + " " + a



# def name_shuffle(str):
# 	first, last = str.split()
# 	return " ".join([last, first])


'''best one'''

# def name_shuffle(str):
# 	return ' '.join(reversed(str.split(' ')))
name = 'Donald trump'
print(name_shuffle(name))