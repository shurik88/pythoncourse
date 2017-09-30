def lab2 (w, h, funcName = 'perim'):

    def perim(w1, h1):
        return (w1 + h1) * 2
    def square(w1, h1):
        return w1 * h1
    if funcName == 'perim':
        return (lambda w1, h1: (w1 + h1) * 2)(w, h)
    else:
        return (lambda w1, h1: (w1 * h1))(w, h)

width = int(input())
height = int(input())
print ('%d %d' % (lab2(width, height, 'square'), lab2(width, height, 'perim')))