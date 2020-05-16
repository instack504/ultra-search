from flask import Flask,request,redirect
from flask import render_template
import requests
# from source import makeRequest
app = Flask(__name__)

q=''
r=''
agent = ''
def makeRequest(q,agent):
    url = 'http://www.google.com/search?q='+q.replace(" ","%20")
    h = {
        "User-Agent":agent
    }
    resp = requests.get(url, headers = h)
    return resp
@app.route("/")
def index():
    # global agent
    # agent = request.cookies['userAgent']
    return render_template("index.html")

@app.route("/process", methods = ['POST'])
def process():
    global q,r,agent
    
    agent = request.cookies['userAgent']
    q = request.form['q']
    r = makeRequest(q,agent)
    return redirect("results")
@app.route("/results")
def result():
    return r.content
def getAgent():
    return agent
if __name__ == "__main__":
    app.run(debug=True)
