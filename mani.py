import flask
# save this as app.py
from flask import Flask, render_template

app = Flask(__name__,
            template_folder='templates_private',
            static_folder='static_public')

@app.route("/")
def hello():

    # return "Hello, World Saurabh ji !"
    return render_template('index.html')

@app.route("/saurabh")
def test():
    return "Hello,Saurabh bhai54757658 !"
# app.run(debug= True)

@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/variable_create")
def variable_create():
    name= "Saurabh Sharma"
    return render_template("variable.html", name22 = name)
app.run(debug=True)

# name22 = this part belongs to template se uthata h
# name == this part belong to python program se uthata h
#in flask our app is here our website inside flask fremwork