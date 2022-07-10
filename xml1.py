import xml.etree.ElementTree as ET

data = '''
<person>
  <name>Chuck</name>
  <phone type="intl">
    +1 734 303 4456
  </phone>
  <email hide="yes" />
</person>'''

tree = ET.fromstring(data)
print('Tree Type: ', type(tree))
print('Tree: ', tree)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))

# Tree Type:  <class 'xml.etree.ElementTree.Element'>
# Tree:  <Element 'person' at 0x000001A13B211760>
# Name: Chuck
# Attr: yes
