import time, subprocess , os

while True:
	localtime = time.asctime(time.localtime()) # returns 'Thu Mar 19 01:08:48 2020'
	lis = localtime.split(' ') #['Thu', 'Mar', '19', '01:09:23', '2020']

	if (lis[3] == '01:21:00'):
		#subprocess.call(['shudown' , '/s' , '/t' , '?'])
		os.system('shutdown -s')