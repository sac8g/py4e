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

