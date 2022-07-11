import json
# Dictionary
data = '''{
  "name" : "Chuck",
  "phone" : {
    "type" : "intl",
    "number" : "+1 734 303 4456"
   },
   "email" : {
     "hide" : "yes"
   }
}'''

info = json.loads(data)
print('Type: ', type(info))
print(info)
print('Name:', info["name"])
print('Hide:', info["email"]["hide"])
print('Phone:', info["phone"])
print('Phone Type: ', type(info["phone"]))
print('Phone Number:', info["phone"]["number"])
print('Phone type:', info["phone"]["type"])

# Type:  <class 'dict'>
# {'name': 'Chuck', 'phone': {'type': 'intl', 'number': '+1 734 303 4456'}, 'email': {'hide': 'yes'}}
# Name: Chuck
# Hide: yes
# Phone: {'type': 'intl', 'number': '+1 734 303 4456'}
# Phone Type:  <class 'dict'>
# Phone Number: +1 734 303 4456
# Phone type: intl
