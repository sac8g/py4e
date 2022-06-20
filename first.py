
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
stuff = 'X\nY'
print(len(stuff))
print(stuff)

file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
file_handle = open(file_name, 'r')
count = 0
for cheese in file_handle:
    count = count + 1
    # print(cheese)
file_handle.close()
print('File: ' + file_name + ', Line count: ',  count)

file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
file_handle = open(file_name, 'r')
for line in file_handle:
    line = line.rstrip()
    if line.startswith('for'):
        print(line)

file_handle.close()

#file_name = input('Enter file name: ')
# C:\\dev\\work\\py4e\\src\\first.py
try:
    file_handle = open(file_name, 'r')
except:
    print('File cannot be opened:', file_name)
    print('Opening C:\\dev\\work\\py4e\\src\\first.py instead...')
    file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
    file_handle = open(file_name, 'r')
    # quit()

count = 0
for line in file_handle:
    line = line.rstrip()
    if line.startswith('for'):
        print(line)
        count = count + 1
print('Number of for lines was', count)
file_handle.close()

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
file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
file_handler = open(file_name)
for line1 in file_handler:
    line1 = line1.rstrip()
    words = line1.split()
    # Guardian
    if len(words) < 3 :
        continue
    if words[0] != 'file_name':
        continue
    if len(words) > 1:
        print(words[2])

print()

file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
file_handler = open(file_name)
for line1 in file_handler:
    line1 = line1.rstrip()
    words = line1.split()
    # Guardian compound
    if len(words) < 3 or words[0] != 'file_name':
        continue
    print(words[2])

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

# Read from file

file_name = 'C:\\dev\\work\\py4e\\src\\first.py'
file_handler = open(file_name)

print()



print('************** FINISH ***************')

