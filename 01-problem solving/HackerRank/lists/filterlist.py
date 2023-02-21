def filter_list(l):
	# for element in l:
	# 	if isinstance(element,str):
	# 		l.remove(element)
	# return l
	for element in l :
		if type(element) == type("str"):
			l.remove(element)
	return l

lis = [1,2,3,'a',4,'mena']
li = filter_list(lis)
print(li)