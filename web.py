import urllib.request
# with urllib.request.urlopen('http://www.python.org/') as f:
	# print(f.read(300))

# with urllib.request.urlopen('http://www.python.org/') as f:
	# print(f.read(100).decode('utf-8'))

# req = urllib.request.Request(url='http://127.0.0.1:8000/')
# with urllib.request.urlopen(req) as f:
# 	print(f.read().decode('utf-8'))


DATA = b'some data'
req = urllib.request.Request(url='http://localhost:8080', data=DATA, method='PUT')
with urllib.request.urlopen(req) as f:
	pass
print(f.status)
print(f.reason)