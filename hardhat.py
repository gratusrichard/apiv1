from ultralytics import YOLO
from flask import jsonify
model = YOLO("hardhat.pt")



def detect(image):
    result = model.predict(source=image,verbose=False)


    if result[0].boxes.data.tolist():

        return jsonify(result[0].boxes.data.tolist())
    
    else:
        return jsonify(0)