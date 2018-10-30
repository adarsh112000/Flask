from flask import Flask,render_template
app=Flask(__name__)
@app.route("/<user>/<user1>/<user2>")
def Hi(user,user1,user2):
    str1="Beautiful day in Shrilanka!"
    str2="Tiger zinda hey movie was so cool!"
    return render_template("final.html",user=user,user1=user1,user2=user2,str1=str1,str2=str2)
@app.route("/index")
def index():
    user={"username":"Dhiraj"}
    posts=[
    {
        "author":{"username":"Daniel"},
        "body":"Beautiful day in Srilanka!"
    },
    {
        "author":{"username":"Amar"},
        "body":"Tiger zinda hey movie was so cool"
    }
        ]
    return render_template("index.html",user=user,posts=posts)
if __name__=="__main__":
    app.run(debug=True)

