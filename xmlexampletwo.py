import xml.etree.ElementTree as ET

input = '''<stuff>
    <users>
        <user x="2">
            <id>01</id>
            <name>Andres</name>
        </user>
        <user x="7">
            <id>09</id>
            <name>Galeano</name>
        </user>
    </users>
</stuff>'''

stuff = ET.fromstring(input)
lst = stuff.findall('users/user')
print('User count: ', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))
