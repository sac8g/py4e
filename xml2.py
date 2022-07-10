import xml.etree.ElementTree as ET

input = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('Lst Type: ', type(lst))
print('Lst: ', lst)
print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))

# Lst Type:  <class 'list'>
# Lst:  [<Element 'user' at 0x0000012B45144D10>, <Element 'user' at 0x0000012B45144E00>]
# User count: 2
# Name Chuck
# Id 001
# Attribute 2
# Name Brent
# Id 009
# Attribute 7

