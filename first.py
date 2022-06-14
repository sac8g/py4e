
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
sum = 0
print('Before:', count, sum)
for value in [9, 41, 12, 3, 74, 15]:
    count = count + 1
    sum = sum + value
    print(count, sum, value)
print('After:', count, sum, sum / count)

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




print('************** FINISH ***************')
