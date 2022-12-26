# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def hello_world():
	return render_template('index.html')

# main driver function
if __name__ == '__main__':
	app.run(debug=True)
