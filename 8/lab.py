#import urllib.parse
import urllib.request

from urllib.parse import urlparse
url = "http://en.ifmo.ru/en/contacts/Contacts.htm" #str(input())

url_res = tuple(urlparse(url))
print (url_res)

url_file = urllib.request.urlopen(url)
html_file = url_file.read().decode('utf-8')
#print (html_file)

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    currTag = ''
    content =[]
    def handle_starttag(self, tag, attrs):
        self.currTag = tag
        print ("Start tag:"+tag)

    def handle_endtag(self, tag):
        self.currTag = ''
        print ("End tag:"+tag)

    def handle_data(self, data):
        if self.currTag == 'h1':
            self.content.append(data)
        print ("Data:"+data)    
    

pars = MyHTMLParser()

pars.feed("<h1>http://google.com</h1>")
print (''.join(pars.content))