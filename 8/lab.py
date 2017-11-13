#import urllib.parse
import urllib.request

from urllib.parse import urlparse
url = "http://en.ifmo.ru/en/contacts/Contacts.htm" #str(input())
url_res = tuple(urlparse(url))
print (url_res)

url_file = urllib.request.urlopen(url)
html_file = url_file.read().decode('utf-8')
start = 0
index = html_file.find('<h1>', start)
data = []
while index != -1:
    close = html_file.find('</h1>', index)
    data.append(html_file[index+4:close])
    start = close
    index = html_file.find('<h1>', start)
print (' '.join(data))

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    content =[]
    h1Opened = False
    currData = ''
    def handle_starttag(self, tag, attrs):
        if self.h1Opened:
            temp = []
            for name, value in attrs:
                temp.append('{0}="{1}"'.format(name, value))
            if len(temp) != 0:
                self.currData+='<{0} {1}>'.format(tag, ' '.join(temp))
            else:
                self.currData+='<{0}>'.format(tag)
            
        if tag == "h1":
            self.h1Opened = True

    def handle_endtag(self, tag):                
        if self.h1Opened and tag != "h1":
            self.currData+='</{0}>'.format(tag)

        if tag == "h1":
            self.h1Opened = False
            self.content.append(self.currData)
            self.currData = ''

    def handle_data(self, data):   
        if self.h1Opened:
            self.currData+=data

#pars = MyHTMLParser()
#pars.feed('<h1><a test="ewfwefew" k="1">wfwefwfwefwef</a></h1>')
#print (''.join(pars.content))