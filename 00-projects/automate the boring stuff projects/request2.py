import requests

res = requests.get('https://requests.readthedocs.io/en/master/')

#to make sure that the site has arrived a response
print(res.status_code)
print(res.ok) # it returns True if the response is less than 400 and Flase if >= 400
print(res.headers)
print(res.text)

#this is the source of HTML code :)