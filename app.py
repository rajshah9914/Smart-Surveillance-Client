from flask import Flask
from firebase import firebase
firebase= firebase.FirebaseApplication("https://sass-cb9b6.firebaseio.com/",None)
app = Flask(__name__)
import requests
import geocoder
from playsound import playsound
from flask import render_template 

Att = ["Fire", "Weapon", "Intruder"]
# filefire = open('fire.txt', 'r')
# fileWeapon = open('weapon.txt', 'r')
# fileIntruder = open('intruder.txt', 'r')

@app.route('/') 
def homepage():

    result= firebase.get('/sass-cb9b6/sass','')

# UPDATE
# result= firebase.put('/sass-cb9b6/sass/-MENTRivnr1SqB73rmqL','fire','1')
#     print(result)
    
#     imgSrcFire = 0
#     imgSrcWeapon = 1
#     imgSrcIntruder = 1
    imgSrcFire = result['-MENTRivnr1SqB73rmqL']['fire']
    imgSrcWeapon = result['-MENTRivnr1SqB73rmqL']['weapon']
    imgSrcIntruder = result['-MENTRivnr1SqB73rmqL']['intruder']
    print(result['-MENTRivnr1SqB73rmqL']['fire'])
    print(result['-MENTRivnr1SqB73rmqL']['intruder'])
    print(result['-MENTRivnr1SqB73rmqL']['weapon'])
    Att = ["Fire", "Weapon", "Intruder"]
    # filefire = open('fire.txt', 'r')
    # imgSrcFire = filefire.read()
    # filefire.close()

    # fileWeapon = open('weapon.txt', 'r')
    # imgSrcWeapon = fileWeapon.read()
    # fileWeapon.close()

    # fileIntruder = open('intruder.txt', 'r')
    # imgSrcIntruder = fileIntruder.read()
    # fileIntruder.close()

    # print(imgSrcFire,imgSrcWeapon,imgSrcIntruder)
    return render_template("index.html", imgSrcFire = imgSrcFire, imgSrcWeapon = imgSrcWeapon, imgSrcIntruder = imgSrcIntruder) 

@app.route("/firealarm")
def firealarm():
    playsound('fire_siren.mp3')
    return "Fire Detected"

@app.route("/sms")
def sms():
    url = "https://www.fast2sms.com/dev/bulk"
    g = geocoder.ip('me')
    print(g.latlng)
    lat=g.latlng[0]
    longi=g.latlng[1]
    msg="Suspicious activity detected..Device has been detecting a robbery..Your quick assistance is required..  GPS Locatation:"+str(g.latlng)
    querystring = {"authorization":"2ndrfwRFhotlDvcy3P8mbKIWxGsq5j0V1gO4iTAQMLUJzYCe9ZsR0OdaCYXHPIm3kg9Lnufv5r2JTDWU","sender_id":"FSTSMS","message":msg,"language":"english","route":"p","numbers":"9834576425"}

    headers = {
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)
    return response.text

if __name__ == "__main__":
    app.run(host='0.0.0.0')
