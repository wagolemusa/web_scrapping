import requests

r = requests.get('https://xkcd.com/353/')

# print(r.status_code)
# print(dir(r))
print(r.headers)