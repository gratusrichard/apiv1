from flask import Flask,request
from PIL import Image
from hardhat import detect


app = Flask(__name__)


@app.route('/',methods=["GET"])
def home():
    return 1


@app.route("/hardhat", methods =["POST"])
def hardhat():


    imgarr = Image.open(request.files['file'])

    return detect(imgarr)