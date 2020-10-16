import json

input = '''
[
    {
        "id":"001",
        "x":"2",
        "name":"Andres"
    },
    {
        "id":"003",
        "x":"5",
        "name":"Felipe"
    }
]
'''

info = json.loads(input)
print('User count: ', len(info))

for i in info:
    print('Name ',i["name"])
    print('ID ',i["id"])
    print('Attribute',i["x"])