
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

#@app.route('/')
#def hello_world():
#    return 'Hello from Dion!'

#
# Retrieve records in a list
#
import requests


headers = {
        'Authorization': 'Bearer keyP0wFDIJaZwktXT',
}

r = requests.get('https://api.airtable.com/v0/appN7kHShxTPBSEPp/flaskdemo?maxRecords=3&view=Grid%20view', headers=headers)
#print("Status Code:",r.status_code)
html_doc = r.content.decode('utf-8')


@app.route("/")
def myhome():
    return render_template("myhome.html")

@app.route("/table")
def table():
    data=html_doc
    return render_template("table.html",data=data)

#@app.route(" /aboutus")
#def aboutus():
# return render_template('aboutus.html')


