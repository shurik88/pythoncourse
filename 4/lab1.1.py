class Library():
    __shelf = {}
    #__history = {}
    def __init__(self, shelf):
        self.Library__shelf = shelf
    def __del__(self):
        pass
        #self.Library__shelf = {}
        #del (self.Library__shelf)
        #print ('destructor')

    def give(self):
        for i in self.Library__shelf:
            self.Library__shelf[i] = self.Library__shelf[i] - 1
        self.currShelf()
    def take(self):
        for i in self.Library__shelf:
            self.Library__shelf[i] = self.Library__shelf[i] + 1
        self.currShelf()
    def currShelf(self):
        print (" ".join(['{0} {1}'.format(k, self.Library__shelf[k]) for k in sorted(self.Library__shelf)]))
    def history(self):
        print (" ".join(['{0} {1}'.format(k, " ".join(str(x) for x in self.Library__shelf[k])) for k  in sorted(self.Library__shelf)]))



data = 'Boogeyman 66 Battleground 50 Astra 12'        
splited = data.split()
dictData = {}
for (i, v) in enumerate(splited):
    if (i % 2 == 0):
        #print (int(splited[i + 1]))
        dictData[splited[i]] = int(splited[i + 1])
        
#books = collections.OrderedDict(alist)

lib = Library(dictData)
lib.currShelf()
lib.give()
lib.take()
del lib