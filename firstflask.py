from flask import Flask, request, render_template, make_response 

import json

app = Flask(__name__)

@app.route("/")  
def helloworld():
    return "Hello, World!"

@app.route("/name")  
def hellotohn():
    return "Hello, Tohn!"

@app.route("/home2")
def home2():
    print('we are in home2')
    # getting input with name = fname in HTML form
    namein = request.form['first name']
    print(namein)
    
    return render_template("home.html",namein='tohn')

if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=True,port=5001)#host='0.0.0.0',port=5001