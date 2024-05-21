from ultralytics import YOLO
from flask import jsonify





def detect(image, model_name):
    model_name = model_name
    model = YOLO(model_name)
    result = model.predict(source=image,verbose=False)


    if result[0].boxes.data.tolist():

        return jsonify(result[0].boxes.data.tolist())
    
    else:
        return jsonify(0)