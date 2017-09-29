def f1(x):
    return x * x

def f2(*args):
    return list(map(f1, args))

def f3(*args, **kvargs):
    print('args:', args)
    print('kvargs', kvargs)

print( f2( 1, 2, 3, 4))

f3(1, 4, 6, 7, a1='efe', a2=4)