titleInput = str(input())
h1Color = str(input())
pColor = str(input())
h1Input = str(input())
pInput = str(input())

styleInput = 'h1{{color:{0}}}p{{color:{1}}}'.format(h1Color, pColor)

#print (styleInput)


def myTag(tagName):
    onelineTags = ['title', 'style', 'h1', 'p']
    def decorator(func):
        def inner(content):
            if tagName in onelineTags:
                return '<{0}>{1}</{0}>'.format(tagName, content)
            else:
                return '<{0}>\n{1}\n</{0}>'.format(tagName, content)
            #print("<%s>"%tagName)
            #res = func(content)
            #print("</%s>"%tagName)
        return inner
    return decorator


@myTag('title')
def content(text = 'hello'):
    return text

title = content

@myTag('style')
def content(text = 'hello'):
    return text

style = content

@myTag('head')
def content(text):
    return text
head = content

@myTag('h1')
def content(text = 'hello'):
    return text

h1 = content

@myTag('p')
def content(text = 'hello'):
    return text

paragraph = content

@myTag('body')
def content(text):
    return text
body = content

@myTag('html')
def content(text):
    return text
html = content

print (html (head(title(titleInput) + '\n' + style(styleInput)) + '\n' + body(h1(h1Input) + '\n' + paragraph(pInput))))



#print (head(title('my title') + '\n' + style('my style')))
#print (title('my title'))
#print (style('my style'))