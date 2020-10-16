import xml.etree.ElementTree as ET

data = '''<person>
    <name>Andres</name>
    <phone type="intl">
        3213456789
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ',tree.find('email').get('hide'))