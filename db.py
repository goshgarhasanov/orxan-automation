import json
def getDB():
    f=open('db.json')
    data=json.load(f)
    return data