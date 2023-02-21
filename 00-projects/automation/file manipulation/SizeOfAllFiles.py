import os
import time 

current_dir = os.path.dirname(os.path.realpath(__file__))

lis = []
for pathname, folders, filename in os.walk(current_dir):
	for file in filename:
		path = ''
		path = os.path.join(pathname,file)
		lis.append(path)
#print(lis)
Dict = {}
for files in lis:
	Dict[files] = os.stat(files).st_size

for i in Dict.keys(): #this for loop to modify dictionary values from bytes to MBs
	Dict[i] = Dict[i]/1024/1024
	# print(Dict[i])
# print(Dict) #size in bytes
for key, value in sorted(Dict.items(), key=lambda item: item[1]): #This for loop to sort dictionary by value
    print("%s >>> %s" % (key, '{:.2f}'.format(value)), 'MBs')

n = input()
# sorted_Dictionary = sorted((key,value) for key,value in Dict.items())
# for p,s in sorted_Dictionary:
# 	print(p,">>>",s)
# print(Dict.sort().reverese(True))
# print(sorted(Dict,reverese=True))