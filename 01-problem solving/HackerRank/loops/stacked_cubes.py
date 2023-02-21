def stack_boxes(n):
	sum = 0
	for i in range(1,n):
		sum += i 
	return n + (sum*2)

print(stack_boxes(2))
print(stack_boxes(4))
print(stack_boxes(3))