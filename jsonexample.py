import json

data = '''
{
    "name" : "Andres",
    "phone" : {
        "type" : "intl",
        "number" : "3124567890"
    },

    "email": {
        "hide" : "yes"
    }
}
'''

info = json.loads(data)
print ('Name', info["name"])
print ('Hide', info["email"]["hide"])