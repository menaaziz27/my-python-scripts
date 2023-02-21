import os 
import time

current_path = os.path.dirname(os.path.realpath(__file__))

lis = []

for filePath, Directories, fileName in os.walk(current_path):
	for files in fileName:
		path = ''
		path = os.path.join(filePath , files)
		lis.append(path)
# print(lis)

maxSize = lis[0]
for file_path in lis:
	if os.stat(file_path).st_size > os.stat(maxSize).st_size:
		maxSize = file_path


# print(os.path.basename(maxSize) ,' is ', os.stat(maxSize).st_size / 1024/1024) >>> it prints it in bytes
from_Bytes_to_MBs = (os.stat(maxSize).st_size) /1024/1024
print(os.path.basename(maxSize) , 'is', '{:.1f}'.format(from_Bytes_to_MBs) , 'MBs')
print()
print(maxSize)
time.sleep(5)