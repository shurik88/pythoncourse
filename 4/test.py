class Etest(object):
    x = 1

e = Etest()
print (e.x)

class Test2(type):
    x = 1

#e1 = Test2(int)

class A(object):
    x=5
    def xx(self):
        print(self.x)

a = A()
a.xx()

class A(object):
    x = 7
    def xx(self):
        print(self.x)

print (a.x)

a1 = A()
a1.xx()
print (a1.x)

print (a.x, a1.x)



