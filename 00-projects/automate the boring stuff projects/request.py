import requests

res = requests.get('https://imgs.xkcd.com/comics/python.png')

#print(res)
#print(dir(res))
#print(help(res))
with open ('comic.png' ,'wb') as f:
	f.write(res.content)

#exists in C:\Users\3azzouz\mypythonscripts
#this is the png in write byte mode :)