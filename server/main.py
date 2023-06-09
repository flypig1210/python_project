
# coding: utf-8

# In[ ]:


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return "<html><body><h2>Hello World!</h2></body></html>"

@app.route("/<name>")
def hello(name):
    return f"<html><body><h2>Hello {name}!</h2></body></html>"

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/dologin", methods=["GET"])
def dologin():
    acc = request.args["account"]
    pwd = request.args["password"]
    return f"<html><body><h1>ACC:{acc}, PWD:{pwd}</h1></body></html>"

app.run()

