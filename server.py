from flask import Flask
from flask import request
import json

app = Flask(__name__)

@app.route("/",methods = ["POST", "GET"])
def hello():
    #request.method == 'POST'
    print "Got: ", request.form["foo"]
    return 'lol'
    return json.dumps(request.form["foo"])

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
