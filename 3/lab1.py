import hashlib
text = input().encode()

dict = {'md5': hashlib.md5(text).hexdigest(),
'sha1': hashlib.sha1(text).hexdigest(), 
'sha224': hashlib.sha224(text).hexdigest(),
'sha256': hashlib.sha256(text).hexdigest(), 
'sha384': hashlib.sha384(text).hexdigest(), 
'sha512': hashlib.sha512(text).hexdigest() 
}

for (i, v) in sorted(dict.items(), key = lambda x: x[0], reverse = False):
	print (i, v)