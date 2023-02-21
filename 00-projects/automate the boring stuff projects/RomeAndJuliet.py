import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
#res.status_code
#200
#len(res.text)
#178978
#print(res.text[:500])
file = open('RomeAndJuliet.txt' , 'wb')
for chunck in res.iter_content(100000):
	file.write(chunck)

	
#100000
#78978
file.close()
