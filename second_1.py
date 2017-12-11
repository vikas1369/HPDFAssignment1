from flask import Flask
app = Flask(__name__)
import requests
import json
@app.route('/authors')
def getListofAuthors():
    r=requests.get("https://jsonplaceholder.typicode.com/users")
    data=r.json();
    listName=[];
    for i in data:
        listName.append(i["name"]);
    return json.dumps(listName);
    r=requests.get("https://jsonplaceholder.typicode.com/posts")
    data=r.json();
    listName=[];
    for i in data:
        listName.append(i["body"]);
    return json.dumps(listName);
