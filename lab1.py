def lab1 (w, h, funcName = 'perim'):
    def perim(w1, h1):
        return (w1 + h1) * 2
    def square(w1, h1):
        return w1 * h1
    if funcName == 'perim':
        return perim(w, h)
    else:
        return square(w, h)

width = int(input())
height = int(input())
print ('%d %d' % (lab1(width, height, 'square'), lab1(width, height, 'perim')))