from flask import Flask, render_template
from datetime import date
import requests
import json

app = Flask(__name__)





@app.route('/')
def home():
    
    return "<h1>Please enter your name in url after '/'</h1>"


@app.route('/<post_id>')
def show_post(post_id):
    name = post_id
    
    req = requests.get("https://api.agify.io/?name=" + name )
    results = json.loads(req.text)
    age = results['age']
    
    req = requests.get("https://api.genderize.io/?name=" + name )
    results = json.loads(req.text)
    gender = results["gender"]
    return render_template('index.html',name = name, age = age, gender = gender)

if __name__ == "__main__":
    app.run(debug=True)


