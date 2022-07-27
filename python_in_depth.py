# Python in Depth
# 2022-07-24

for i in range(5):
    print(i)

print()

i = 0
while i < 5:
    print(i)
    i += 1
i = None

print()

for i in range(5):
    print('--------------')
    try:
        10 / (i - 3)
    except ZeroDivisionError:
        print('Divided by 0')
        continue
    finally:
        print('Always run')

    print(i)

class Rectangle:
    def __init__(self, w, h):
        self._w = w
        self._h = h

    def area(self):
        return self._w * self._h

    def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self._w, self._h)

    # def __str__(self):
    #     return 'Rectangle: width={0}, height={1}'.format(self.w, self.h)

    def __repr__(self):
        return 'Rectangle({0}, {1})'.format(self._w, self._h)

    def __eq__(self, other):
#        return self.h == other.h and self.w == other.w
        if isinstance(other, Rectangle):
            return self._h == other._h and self._w == other._w
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

    def get_width(self):
        return self._w

    def set_width(self, width):
        if width <= 0:
            raise ValueError('Width must be positive!')
        else:
            self._w = width

    def get_height(self):
        return self._h

    def set_height(self, height):
        if height <= 0:
            raise ValueError('Height must be positive!')
        else:
            self._h = height

print()

print('--------------')

r1 = Rectangle(10, 34)
r2 = Rectangle(10, 32)

# print(id(r1))
# print(id(r2))
# print(hex(id(r1)))
# print(hex(id(r2)))


# print(r1.w, r1.h)
# print(r1.area())

# print(hex(id(r1)))
# print(hex(id(r2)))
# print(r1.to_string())
# print(str(r1))
# print(str(r2))
print(r1)
print(r2)
# print(r1 is not r2)
# print(r1 == r2)
# print(r2 < r1)

r1.set_width(-100)


