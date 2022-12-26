from flask import Flask
import random


app = Flask(__name__)
random_number = random.randint(0,10)
print(random_number)

@app.route("/")
def hello_world():
    return "<h1>Guess a number between 0 to 10<h1>" \
        '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" width=200 >'

@app.route('/<int:post_id>')
def show_post(post_id):
    number = '%d' % post_id
    if random_number == int(number):
        return "<h1> You found me</h1>" \
            "<img src='https://media.giphy.com/media/QyK8gRzGW2fV6qo8Hm/giphy.gif'>"
           
    elif int(number) > random_number:
        return "<h1 style='color: red'>  Too high, try again!</h1>" \
             "<img src='https://media.giphy.com/media/JOX6vqoOSejOOu8gqF/giphy.gif'>"
            
    else:
        return "<h1  style='color: purple'>Too low, try again!low </h1>" "<img src='https://media.giphy.com/media/IevhwxTcTgNlaaim73/giphy.gif'>"             
    
   


