from flask import Flask
from flask import request
import json
#import serial
#import RPi.GPIO as GPIO

#ser = serial.Serial('/dev/ttyACM0', 9600)

app = Flask(__name__)

@app.route("/",methods = ["POST", "GET"])
def hello():
  if request.method == 'POST':
    for i in request.form:
      command = i + ":" + request.form[i]
      print command
      #ser.write(command) # f is used to collect force sensor data

    return "Recieved info" 

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
