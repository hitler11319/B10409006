import base64
s1 = base64.b64encode(bytes('hello world', 'utf-8')).decode()
s2 = base64.b64decode(s1).decode()
print (s1)
print (s2)
