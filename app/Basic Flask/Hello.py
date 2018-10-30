from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/cal/<var>")
def val_print(var):
    return "Hello %s" %var

    
@app.route("/about")
def about():
    return "About"


if __name__=="__main__":
    app.run()
