#Parent_and_child_template
from flask import Flask,render_template
app=Flask(__name__)
@app.route("/")
def home():
    render_template("home.html")
    
