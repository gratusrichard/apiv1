from flask import Flask,request
from PIL import Image
from YoloObjectdet import detect
from emotion import emotion_det



app = Flask(__name__)


@app.route('/',methods=["GET"])
def home():
    return "success",404


#hardhat

@app.route("/hardhat", methods =["POST"])
def hardhat():


    imgarr = Image.open(request.files['file'])

    return detect(imgarr, "hardhat.pt")

#emotion

@app.route("/emotion",methods=["POST"])
def emotion():
    imgarr = Image.open(request.files['file'])
    

    return emotion_det(imgarr)


#helmet
@app.route("/helmet", methods=["POST"])
def helmet():
    imgarr=Image.open(request.files['file'])

    return detect(imgarr,"bike_helmet.pt")

#chefhat


@app.route("/chefhat", methods=["POST"])
def chefhat():
    imgarr = Image.open(request.files['file'])

    return detect(imgarr,"chef_hat.pt")
