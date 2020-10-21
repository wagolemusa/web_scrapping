import requests

payload = {'username':'wise', 'password':'refuge'}

r = requests.post('https://httpbin.org/post', data=payload)
# print(r.text)
# print(r.json())

r_dict = r.json()
print(r_dict['form'])