from urllib import request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_866758.xml'
print ("Retrieving", url)
html = request.urlopen(url)
data = html.read()
print("Retrieved",len(data),"characters")

tree = ET.fromstring(data)
results = tree.findall('comments/comment')
icount=len(results)
suma=0

for result in results:
    suma += int(result.find('count').text)
print(icount)
print(suma)