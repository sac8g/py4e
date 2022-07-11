
print('************** START ***************')
print('Hello from a file')

###

x = 2
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')

print('Finish')

###

n = 5
while n > 0:
    print(n)
    n = n - 1

print('Blast off')

spam = 1
Spam = 2
SPAM = 3

print(spam, Spam, SPAM)

######
# Operators
#   Numeric
#       +, -, *, /, ** (power), % (reminder)
#   Precedence
#       ()
#       **
#       *, /, %
#       +, -
#       left-to-right
#
#
######
eee = 'Hello ' + 'there'

print(type(eee))
# <class 'str'>
ddd = 123

print(type(ddd))
# <class 'int'>

print(type(34.45))
# <class 'float'>

# eee = eee + 1
# Compiler error

print(float(100) + 23)
# 123.0
print(type(float(23) + 234))
# <class 'float'>

print(10/2)
# 5.0
print(9/2)
# 4.5
print(99/100)
# 0.99
print(10.0/2.0)
# 5.0
print(99.0/100.0)
# 0.99

sval = '123'
print(type(sval))

# Compiler error
# print(sval + 1)

ival = int(sval)
print(type(ival))

# Compiler error
# nval = 'Hello'
# niv = int(nval)

## User Input
# nam = input('Who are you: ')
nam = 'Igor'
print('Welcome', nam, '!')

# inp = input('Europe floor? ')
inp = 5
usf = int(inp) + 1
print('US floor:', usf)

# 2022/06/13
# conditional execution
if n > 10:
    print('Test1')
else:
    print('Test2')

x = 5
if x < 2:
    print('Small')
elif x < 10:
    print('Medium')
elif x < 20:
    print('Big')
elif x < 40:
    print('Large')
else:
    print('Huge')
print('All done.')

# try/except
astr = 'Hello Bob'
try:
    istr = int(astr)
except:
    istr = -1

print('First:', istr)

astr = '123'
try:
    istr = int(astr)
except:
    istr = -1

print('Second:', istr)

#instr = input('Enter a number: ')
instr = 'kuku'
try:
    ival = int(instr)
except:
    ival = -1

if ival > 0:
    print('Nice work')
else:
    print('Not a number')

# Functions
def thing():
    print(' Hello')
    print(' Fun')

thing()
print('Zip')
thing()


def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    elif lang == 'en':
        return 'Hello'

print(greet('es'), 'Pedro')
print(greet('en'), 'John')
print(greet('fr'), 'Emanuelle')

# Loops and Iterations
# WHILE
n = 5
while n > 0:
    print(n)
    n = n - 1
print('All done')

# break - out of the innermost loop
# continue - ends the current iteration and jumps to top of the loop

# indefinite loops
# definite loops

for i in [4, 6, 2, 12]:
    print(i)
print('All done')

friends = ['Tom','John','Marry','Kate']
for friend in friends:
    print('Happy New Year', friend)
print('Done')

# Average
count = 0
sum1 = 0
print('Before:', count, sum1)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum1 = sum1 + value
    print(count, sum1, value)
print('After:', count, sum1, sum1 / count)

# Smallest
smallest = None
print('Before:')
for value in [9, 41, 12, 3, 74, 15]:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After:', smallest)

# 2022/06/13
# Strings
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1


fruit = 'banana'
for letter in fruit:
    print(letter)

#

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1

# looping and counting
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

for letter in 'banana':
    print(letter)

# String operations
# Slicing

# M o n t y   P y t h o n
# 0 1 2 3 4 5 6 7 8 9 1011
s = 'Monty Python'
print(s[0:4]) # Mont
print(s[6:7]) # P
print(s[6:30]) # Python
print(s[:2]) # Mo
print(s[8:]) # thon
print(s[:]) # Monty Python

# Concatenation
a = 'Hello'
b = a + 'There'
# HelloThere
c = a + ' ' + 'There'
# Hello There

# using in
fruit = 'banana'
print('n' in fruit)
print('m' in fruit)
print('nan' in fruit)
if 'a' in fruit:
    print('Found it!')

# compare
word = 'banana'
if word == 'banana':
    print('All right, bananas.')

if word < 'banana':
    print('Your word, ' + word + ', comes before banana.' )
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.' )
else:
    print('All right, bananas.')

# string library
greet = 'Hello Zak'
print(greet.lower())
# hello zak
print('Hi There'.lower())
# hi there

stuff = 'Hello World'
# print(dir(stuff))
# ['capitalize', 'casefold', 'center', 'count', 'encode',
# 'endswith', 'expandtabs', 'find', 'format', 'format_map',
# 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal',
# 'isdigit', 'isidentifier', 'islower', 'isnumeric',
# 'isprintable', 'isspace', 'istitle', 'isupper',
# 'join', 'ljust', 'lower', 'lstrip', 'maketrans',
# 'partition', 'removeprefix', 'removesuffix', 'replace',
# 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit',
# 'rstrip', 'split', 'splitlines', 'startswith', 'strip',
# 'swapcase', 'title', 'translate', 'upper', 'zfill']

str = 'Hello World!'
print(str.find('ll'))
print(str.find('oo'))
print(str.upper())
print(str.lower())

nstr = str.replace('World', 'Universe')
print(nstr)

nstr = str.replace('l', 'R')
print(nstr)

# whitespace - space, tab, new line
str = '    Hello World    '
print('***', str.lstrip(), '***')
print('***', str.rstrip(), '***')
print('***', str.strip(), '***')

# prefixes
str = 'Please have a nice day!'
print(str.startswith('Please'))
print(str.startswith('p'))

# parsing
str = 'From tom@uct.ac.za Sat Aug 12 2009'
atpos = str.find('@')
print(atpos)
sppos = str.find(' ', atpos)
print(sppos)
host = str[atpos+1 : sppos]
print(host)
# uct.ac.za

# Reading files
file_handle = open('C:\\dev\\work\\py4e\\src\\first.py', 'r')
print(file_handle)
# <_io.TextIOWrapper name='C:\\dev\\work\\py4e\\src\\first.py' mode='r' encoding='cp1252'>
file_handle.close()

# new line
print('Hello\nWorld!')
stuff2 = 'X\nY'
print(len(stuff2))
print(stuff2)

# file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
# file_handle = open(file_name, 'r')
# count = 0
# for cheese in file_handle:
#     count = count + 1
#     # print(cheese)
# file_handle.close()
# print('File: ' + file_name + ', Line count: ',  count)
#
# file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
# file_handle = open(file_name, 'r')
# for line in file_handle:
#     line = line.rstrip()
#     if line.startswith('for'):
#         print(line)
#
# file_handle.close()
#
# #file_name = input('Enter file name: ')
# # C:\\dev\\work\\py4e\\src\\first.py
# try:
#     file_handle = open(file_name, 'r')
# except:
#     print('File cannot be opened:', file_name)
#     print('Opening C:\\dev\\work\\py4e\\src\\first.py instead...')
#     file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
#     file_handle = open(file_name, 'r')
#     # quit()
#
# count = 0
# for line in file_handle:
#     line = line.rstrip()
#     if line.startswith('for'):
#         print(line)
#         count = count + 1
# print('Number of for lines was', count)
# file_handle.close()

# Lists
list1 = [1, 24, 76]
list2 = ['red', 'yellow', 'blue']
list3 = ['one', 34, 25]
list4 = [4, [98, 245], 90.34, 43]
list5 = []
print()
print(list1)
print(list2)
print(list3)
print(list4)
print(list5)

print()
friends = ['Tom', 'John', 'Kate']
print(friends[2])
print(friends)
friends[1] = 'Igor'
print(friends)
print(len(friends))

print()
print(range(2))

print()
friends = ['Tom', 'John', 'Kate', 'Jack', 'Helen']
for friend in friends:
    print('Happy New Year:', friend)
print()
for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
print()

# Concatenate
a = [1, 2, 3]
b = [4, 5, 6]
d = [5, 6, 7]
c = a + b
e = b + d
print(a)
print(c)
print(e)
print()

# Slicing
## second number "up to, but not including"
t = [9, 41, 12, 3, 74, 15]
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])
print()

# build list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
print(stuff)
stuff.append('cookie')
print(stuff)

print()

# in
some = [1, 9, 34, 54, 67]
print(9 in some)
print(15 in some)
print(20 not in some)
print()

# lists in order
friends = ['Tom', 'John', 'Kate', 'Jack', 'Helen']
print(friends)
friends.sort()
print(friends)
print(friends[2])
print()

# built-ins
nums = [3, 34, 65, 21, 10, 4, 78, 9]
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))
print(sum(nums)/len(nums))
print()

# List example
# numlist = list()
# while True:
#    inp = input('Enter a number: ')
#    if inp == 'done':
#        break
#    value = float(inp)
#    numlist.append(value)

# average = sum(numlist) / len(numlist)
# print('Average: ', average)
# print()

# Strings and Lists
# splits by spaces; ignores multiple white chars
# can split by a char, i.e. str.split(':')
aStr = 'With three words'
aList = aStr.split()
print(aList)
print(len(aList))
print(aList[1])
for aWord in aList:
    print(aWord)

print()

# File read
# file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
# file_handler = open(file_name)
# for line1 in file_handler:
#     line1 = line1.rstrip()
#     words = line1.split()
#     # Guardian
#     if len(words) < 3 :
#         continue
#     if words[0] != 'file_name':
#         continue
#     if len(words) > 1:
#         print(words[2])

print()

# file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
# file_handler = open(file_name)
# for line1 in file_handler:
#     line1 = line1.rstrip()
#     words = line1.split()
#     # Guardian compound
#     if len(words) < 3 or words[0] != 'file_name':
#         continue
#     print(words[2])

## Dictionaries
# 2022-06-20
# no order
# index things with a lookup tag
# lists index by order, dictionaries index by tags

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissue'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse)

dict1 = { 'chuck': 3, 'chris': 43, 'tom': 100}
dict2 = {}
dict3 = dict()

print(dict1)
print(dict2)
print(dict3)

# dictionaries - counting

def addCount( dict4, name ):
    if name in dict4:
        dict4[name] = dict4[name] + 1
    else:
        dict4[name] = 1

dict5 = dict()
addCount( dict5, 'name1' )
addCount( dict5, 'name2' )
addCount( dict5, 'name3' )
addCount( dict5, 'name3' )
addCount( dict5, 'name2' )
addCount( dict5, 'name1' )
addCount( dict5, 'name1' )
print(dict5)

print()
# same
names = ['name1', 'name2', 'name4', 'name1', 'name1', 'name2', 'name4', 'name4', 'name12', 'name1']
counts = {}
for name in names:
    if name in counts:
        counts[name] = counts[name] + 1
    else:
        counts[name] = 1

print(counts)
print()

# get method
name1 = 'name1'
print(name1, counts.get( name1, 0 ))
name1 = 'name2'
print(name1, counts.get( name1, 0 ))
name1 = 'name3'
print(name1, counts.get( name1, 0 ))
name1 = 'name4'
print(name1, counts.get( name1, 0 ))
name1 = 'name12'
print(name1, counts.get( name1, 0 ))


print()

counts1 = dict()
print('Enter a line: ')
# line = input('')
line1 = 'aaa bbb bbb fff ggg aaa ggg fff fff www rrr ggg www'
words1 = line1.split()
print('Words: ', words1)
print('Counting...')
for word1 in words1:
    counts1[word1] = counts1.get(word1, 0) + 1
print('Counts', counts1)

for key in counts1:
    print(key, counts1[key])

##
print('List:')
print(list(counts1))
print('Keys:')
print(counts1.keys())
print('Values:')
print(counts1.values())
print('Items:')
print(counts1.items())

# two-dimensional iteration
# cool feature
for key2, value2 in counts1.items():
    print(key2, value2)

print()

# # Most common word in a file
# file_name1 = 'C:\\dev\\work\\py4e\\src\\first.py'
# file_handler1 = open(file_name1)
#
# counts3 = dict()
# for line1 in file_handler1:
#     words3 = line1.split()
#     for word3 in words3:
#         counts3[word3] = counts3.get(word3, 0) + 1
#
# bigcount = None
# bigword = None
# for word3, count3 in counts3.items():
#     if bigcount is None or count3 > bigcount:
#         bigword = word3
#         bigcount = count3
#
# print(bigword, bigcount)
# print()

# 2022-06-23
# 2022-06-25
# Tuples (similar to a list, but immutable as a string)
print('******** Tuples *******')
x1 = ('Tom', 'Jerry', 'Duck')

## x1[2] = 'Donald'
## TypeError: 'tuple' object does not support item assignment

y1 = ( 34, 32, 5, 9, 45 )

# list
l1 = list()
t1 = tuple()

print('Tuple: ', dir(t1))
# count, index
print('List: ', dir(l1))
# append, count, extend, index, insert, pop, remove, etc.

print(x1)
print(y1)
print('Max in y1:', max(y1))

for item in y1:
    print(item)

for item1 in x1:
    print(item1)

# tuples and assignment
(x, y) = (4, 'Jack')
print(y)
(a, b) = (45, 34)
print(a)

# tuples wit dictionaries
dict6 = dict()
dict6['Alex'] = 3
dict6['Marrie'] = 25
dict6['Albert'] = 67

for (k, v) in dict6.items():
    print(k, v)

tups = dict6.items()
print(tups)

# tuples are comparable
test1 = (0,1,3) < (4,3,0)
test2 = ('John', 'Sam') > ('John', 'Ariya')
print(test1)
print(test2)

# sorting lists of tuples
dict7 = {'a':10, 'b':1, 'e':12, 'c':22}
print(dict7.items())
# sort by keys
print(sorted(dict7.items()))

print('Sorted by keys:')
for m, n in sorted(dict7.items()):
    print(m, n)

print('Sorted by values:')
tmp_list = list()
for p1, p2 in dict7.items():
    tmp_list.append((p2, p1))

print('Unsorted: ')
print(tmp_list)

tmp_list = sorted(tmp_list, reverse=True)
print('Sorted: ')
print(tmp_list)

# 10 most common words in a file
file_name3 = 'C:\\dev\\work\\py4e\\src\\clown.txt'
file_handler3 = open(file_name3)
counts2 = dict()
for line3 in file_handler3:
    words2 = line3.split()
    for word2 in words2:
        counts2[word2] = counts2.get(word2, 0) + 1

list6 = list()
for key3, val3 in counts2.items():
    newtup = (val3, key3)
    list6.append(newtup)

list6 = sorted(list6, reverse = True)

for val3, key3 in list6[:10] :
    print(key3, val3)

print()

# second version of the same
print( 'Shorter version:' )
# List comprehensiom:
## [(val4,key4) for key4, val4 in counts2.items()]
print( sorted( [(val4,key4) for key4, val4 in counts2.items()], reverse=True )[:10])

# 2022-06-25
# Regular Expressions
print('******** RegEx *******')


# w/o RegEx
print('===== W/O regEx')
file_name4 = 'C:\\dev\\work\\py4e\\src\\clown.txt'
file_handler4 = open(file_name4)
for line4 in file_handler4:
    line4 = line4.rstrip()

    # line contains Costco
#    if line4.find('Costco') >= 0:
#        print(line4)

    # line startes with Costco
    if line4.startswith('Costco'):
        print(line4)


# w/ RegEx
print('===== W/ regEx')
import re
file_name5 = 'C:\\dev\\work\\py4e\\src\\clown.txt'
file_handler5 = open(file_name5)
for line5 in file_handler5:
    line5 = line5.rstrip()

# line contains Costco
#    if re.search('Costco', line5) :
#        print(line5)

# line starts with Costco
    if re.search('^Costco', line5) :
        print('*** Costco:')
        print(line5)

# line starts with X
    if re.search('^X.*:', line5) :
        print('*** X-generic:')
        print(line5)

# line starts with X - more specific
    if re.search('^X-\S+:', line5) :
        print('*** X-specific:')
        print(line5)

print()

# 2022-06-27
## RegEx matching and extraction
# - re.search() - returns True/False
# - re.findall() - match and extract


x2 = 'My 2 favorite numbers are 19 and 42. I also like 345'
y2 = re.findall('[0-9]+', x2)
print(y2)
# ['2', '19', '42', '345']

y2 = re.findall('[AEIOU]+', x2)
print(y2)
# ['I']

# greedy matching = tries to get the largest possible string
x3 = 'From: Using the : character'
# greedy
y3 = re.findall('^F.+:', x3)
print(y3)
# ['From: Using the :']

# same, but non-greedy
y3 = re.findall('^F.+?:', x3)
print(y3)
# ['From:']

# String extraction
y3 = re.findall('(^F.+?):', x3)
print(y3)
# ['From']

## 2022-07-05

# IPv4
x3 = 'My IP address is: 134.138.105.23 1.1.1.1 22.22.22.22 111234.3.3.3 '
y3 = re.findall('[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}', x3)
print(y3)
# ['134.138.105.23', '1.1.1.1', '22.22.22.22', '234.3.3.3']

# Emails
x3 = "kuku@kaka.com kuku.kaka@keke"
y3 = re.findall('\S+@\S+\.\S+', x3)
print(y3)
# ['kuku@kaka.com']

# Host from Email
x3 = 'From kuku@kaka.com Sat Jul 2, 2022'
y3 = re.findall('@([^ ]*)', x3)
print(y3)
# ['kaka.com']

x3 = 'From kuku@kaka.com Sat Jul 2, 2022'
y3 = re.findall('^From .*@([^ ]*)', x3)
print(y3)
# ['kaka.com']

# Prefix spec chars with /
x3 = 'The cost is $13.32 EA'
y3 = re.findall('\$[0-9.]+', x3)
print(y3)
# ['$13.32']
print()

###############################
### Networking Programming
#
# import socket
# mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# mysock.connect(('data.pr4e.org', 80))
#
# # Apps protocols
# cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
# mysock.send(cmd)
#
# while True:
#     data = mysock.recv(512)
#     if (len(data) < 1):
#         break
#     print(data.decode(),end='')
# mysock.close()

print()

# Characters
# https://en.wikipedia.org/wiki/ASCII
# http://www.catonmat.net/download/ascii-cheat-sheet.png

print(ord('H'))
# 72
print(ord('e'))
# 101
print(ord('\n'))
# 10

print()

## Unicode


# Python 3.x
x4 = b'abc'
print(type(x4))
# <class 'bytes'>

x5 = '이광춘'
print(type(x5))
# <class 'str'>

x6 = u'이광춘'
print(type(x6))
# <class 'str'>

print()

# urllib for Network (HTTP)
# urllib makes web pages look like a file

# import urllib.request, urllib.parse, urllib.error
#
# fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# for line in fhand:
#     print(line.decode().strip())

print()

# like a file
# fhand1 = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
# counts3 = dict()
# for line5 in fhand1:
#     words3 = line5.decode().split()
#     for word3 in words3:
#         counts3[word3] = counts3.get(word3, 0) + 1
# print(counts3)
# {'But': 1, 'soft': 1, 'what': 1, 'light': 1, 'through': 1,
# 'yonder': 1, 'window': 1, 'breaks': 1, 'It': 1, 'is': 3,
# 'the': 3, 'east': 1, 'and': 3, 'Juliet': 1, 'sun': 2,
# 'Arise': 1, 'fair': 1, 'kill': 1, 'envious': 1, 'moon': 1,
# 'Who': 1, 'already': 1, 'sick': 1, 'pale': 1, 'with': 1,
# 'grief': 1}

print()

##
# Web Scraping
# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl
import collections

collections.Callable = collections.abc.Callable

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# url = input('Enter - ')
url = 'https://www.dr-chuck.com/page1.htm'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))
#    print(tag)

print()

# 2022-07-07
# Web Services
# XML as wire format


# 2022-07-10
# SOA

# Geo Services - Google

# API Security and Rate Limiting

# Objects in Python


print('************** FINISH ***************')

