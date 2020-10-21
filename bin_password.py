import requests

r = requests.get('https://httpbin.org/basic-auth/wise/refuge', auth=('wise', 'refuge'))

# print(r.text)
print(r.url)