import requests


URL = "http://rpianamdev.wv.cc.cmu.edu:5000" 
#URL = "http://0.0.0.0:5000" 

while True:
  deviceNum = raw_input("Please enter the device to operate: ")
  if ("led" in deviceNum):
    variance = raw_input("Enter brightness (0-100): ")
    #print ledNum
   
  r = requests.post(URL, data = {deviceNum:variance})
  print r.text


