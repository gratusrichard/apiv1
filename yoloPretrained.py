from ultralytics import YOLO





def detect_pretrained(image, model_name):
    model_name = model_name
    model = YOLO(model_name)
    result = model.predict(source=image,verbose=False,classes=[0])


    if result[0].boxes.data.tolist():

        return result[0].boxes.data.tolist()
    
    else:
        return False