def remove(rem):
	arr.remove(rem)

def pop():
	arr.pop()

def insert(val,pos):
	arr.insert(pos,val)
	# print(arr)

def append(app):
	arr.append(app)

if __name__ == '__main__':
	arr = []
	n = int(input("Enter numebr of commands"))
	i = 0
	while i < n:
		op = int(input("Enter operation number"))
		if op > 7:
			print('Should insert number between 1 : 7')
			continue
		else:
			if op == 1:
				pos,val = int(input("Enter pos")).split()
				# val = int(input("Enter val"))
				insert(val,pos)
			elif op == 2:
				print(arr)
			elif op == 3:
				rem = int(input("Enter removed value"))
				remove(rem)
			elif op == 4:
				app = int(input("Enter a number to append"))
				append(app)
			elif op == 5:
				arr.sort()
			elif op == 6:
				pop()
			else:
				arr.sort(reverse=True)
		i += 1