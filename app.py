from flask import Flask,request
from PIL import Image
from YoloObjectdet import detect
from emotion import emotion_det



app = Flask(__name__)


@app.route('/',methods=["GET"])
def home():
    return "success",404


@app.route("/hardhat", methods =["POST"])
def hardhat():


    imgarr = Image.open(request.files['file'])

    return detect(imgarr, "hardhat.pt")


@app.route("/emotion",methods=["POST"])
def emotion():
    imgarr = Image.open(request.files['file'])
    

    return emotion_det(imgarr)




@app.route("/helmet", methods=["POST"])
def helmet():
    imgarr=Image.open(request.files['file'])

    return detect(imgarr,"bike_helmet.pt")