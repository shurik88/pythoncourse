from xml.etree import ElementTree

file1 = open('data.xml', 'r')
tree = ElementTree.parse(file1)

root = tree.getroot()
print ('root tag {0}'.format(root.tag))

for i in tree.getiterator('order'):
    print (i.tag, i.attrib)


import sqlite3
print (sqlite3.apilevel)

con = sqlite3.connect('testdb.db')
con.close()