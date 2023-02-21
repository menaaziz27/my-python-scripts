import requests

res = requests.get('https://httpbin.org/basic-auth/mena/aziz' , auth = ('mena' , 'aziz'))

print(res.text)