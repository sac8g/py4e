import json
# List of dictionaries
data = '''
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]'''

info = json.loads(data)
print('User count:', len(info))
print('Type: ', type(info))
print(info)

for item in info:
    print('Item Type: ', type(item))
    print('Item: ', item)
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])

# User count: 2
# Type:  <class 'list'>
# [{'id': '001', 'x': '2', 'name': 'Chuck'}, {'id': '009', 'x': '7', 'name': 'Brent'}]
# Item Type:  <class 'dict'>
# Item:  {'id': '001', 'x': '2', 'name': 'Chuck'}
# Name Chuck
# Id 001
# Attribute 2
# Item Type:  <class 'dict'>
# Item:  {'id': '009', 'x': '7', 'name': 'Brent'}
# Name Brent
# Id 009
# Attribute 7

print()
# Code: http://www.py4e.com/code3/json2.py
# http://www.youtube.com/watch?v=kc8BAR7SHJI

