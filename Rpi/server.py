from flask import Flask
from flask import request
import json
import math
import serial
#import RPi.GPIO as GPIO

#ser = serial.Serial('/dev/ttyACM0', 9600)

app = Flask(__name__)

deviceLocations = [(150,150),(250,150),(400,150)]
coordReceive = [0,0]

def getClosestDist(x,y,d):
  closestInd = 3
  leastDist = 1000
  for i in range(len(deviceLocations)):
    #print deviceLocations[i][0]
    #print deviceLocations[i][1]
    dist = math.sqrt((x-deviceLocations[i][0])**2 +(y-deviceLocations[i][1])**2) 
    #print "dist",dist
    if dist<leastDist:
      leastDist = dist
      closestInd = i
  if leastDist>d:
    return -1
  return closestInd

@app.route("/",methods = ["POST", "GET"])
def hello():
  if request.method == 'POST':
    coordReceive[0] = int(request.form['x'])
    coordReceive[1] = int(request.form['y'])
    #print coordReceive
    
    deviceInd = getClosestDist(coordReceive[0],coordReceive[1],20)
    #print deviceInd

    if deviceInd == 0:
      serial.write("led0")
    elif deviceInd == 1:
      serial.write("led1")
    elif deviceInd == 2:
      serial.write("led2")

    return "Recieved info" 

if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
