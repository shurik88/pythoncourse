funcs = [(lambda w, h: w*h), (lambda w, h: (w + h)*2)]


width = int(input())
height = int(input())

for index, func in enumerate(funcs):
    print ('%d %d' % (index, func(width, height)))

alist = list(map(lambda x: x(width, height), funcs))
print (alist)
print (" ".join(str(v) for v in alist))