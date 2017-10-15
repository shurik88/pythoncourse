import hashlib

class Converter():
    def convert(self, data):
        books = {}
        splitted = data.split()
        for (i, v) in enumerate(splitted):
            if (i % 2 == 0):
                books[splitted[i]] = int(splitted[i + 1])
        return books

class Hash():
    algs = {
        'md5': lambda text : hashlib.md5(text.encode()).hexdigest(),
        'sha1': lambda text : hashlib.sha1(text.encode()).hexdigest(), 
        'sha224': lambda text : hashlib.sha224(text.encode()).hexdigest(),
        'sha256': lambda text : hashlib.sha256(text.encode()).hexdigest(), 
        'sha384': lambda text : hashlib.sha384(text.encode()).hexdigest(), 
        'sha512': lambda text : hashlib.sha512(text.encode()).hexdigest() 
    }
    def __init__(self, algName):
        self.alg = algName
    def hash(self, data):
        return self.algs[self.alg](data)


inputData = input()
c = Converter()
books = c.convert(inputData)
alg = input()
hash = Hash(alg)
for key in sorted(books):
    print ("%s %s" % (key, books[key]))
#print ([hash.hash(k) for (k, v) in books.items()])
hashes = sorted([hash.hash(k) for (k, v) in books.items()])

print (" ".join(['{0} {1}'.format(alg, v) for v in hashes]))