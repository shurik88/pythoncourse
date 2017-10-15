import collections

class Library():
    __shelf = {}
    #__history = {}
    def __init__(self, shelf):
        self.Library__shelf = shelf
    def __del__(self):
        self.Library__shelf = {}
        del (self.Library__shelf)
        #print ('destructor')

    def give(self, book):
        self.Library__shelf[book].append(self.Library__shelf[book][-1]-1)
    def take(self, book):
        self.Library__shelf[book].append(self.Library__shelf[book][-1]+1)
    def currShelf(self):
        print (" ".join(['{0} {1}'.format(k, v[-1]) for k,v in self.Library__shelf.items()]))
    def history(self):
        print (" ".join(['{0} {1}'.format(k, " ".join(str(x) for x in v)) for k,v in self.Library__shelf.items()]))



data = 'Boogeyman 5 Battleground 10'        
splited = data.split()
alist = []
for (i, v) in enumerate(splited):
    if (i % 2 == 0):
        print (int(splited[i + 1]))
        alist.append((splited[i], [int(splited[i + 1])]))
        
books = collections.OrderedDict(alist)

lib = Library(books)
lib.give('Boogeyman')
lib.take('Boogeyman')
lib.give('Battleground')
lib.take('Battleground')
lib.history()
del lib