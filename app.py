from flask import Flask,request
from PIL import Image
from hardhat import detect
from emotion import emotion_det



app = Flask(__name__)


@app.route('/',methods=["GET"])
def home():
    return "success",404


@app.route("/hardhat", methods =["POST"])
def hardhat():


    imgarr = Image.open(request.files['file'])

    return detect(imgarr)


@app.route("/emotion",methods=["POST"])
def emotion():
    imgarr = Image.open(request.files['file'])
    

    return emotion_det(imgarr)