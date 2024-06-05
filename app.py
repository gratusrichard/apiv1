from flask import Flask,request,jsonify
from PIL import Image
from YoloObjectdet import detect
from emotion import emotion_det
from yoloPretrained import detect_pretrained
from retina_face import face_det, face_extract_r
import numpy as np
import base64
from io import BytesIO

app = Flask(__name__)


@app.route('/',methods=["GET"])
def home():
    return "success",200


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



#sleep_detection

@app.route("/sleep",methods=['POST'])
def sleep():
    imgarr = Image.open(request.files['file'])
    return detect(imgarr,"sleep")




@app.route("/crowd", methods=['POST'])
def crowd():
    imgarr = Image.open(request.files['file'])
    detection = detect_pretrained(imgarr,'yolov8m.pt')
    threshold = request.form.get('threshold')
    threshold = int(threshold)
    print(threshold)
    
    # detection = int(detection)
    length = len(detection)
    print("length," ,length)
    diff = length-threshold

    if not detection:
        return None,200

    if length > threshold:
        body = {"crowded":str(True),
                "people": str(length),
                "difference": str(diff)
                }
        
        return jsonify(body),200
    else:
        body = {
            "crowded":str( False),
            "people":str(length),
            "difference": str(diff)
                }

        return jsonify(body),200
    


@app.route("/face", methods=["POST"])
def face():
    imgarr = Image.open(request.files['file'])

    return face_det(imgarr)


@app.route("/crop",methods=["POST"])
def crop():
        image = Image.open(request.files['file']) 
        numpy_image = np.array(image)

        x_min =int( request.form.get("x_min"))
        y_min= int(request.form.get("y_min"))
        x_max = int(request.form.get("x_max"))
        y_max = int(request.form.get("y_max"))


        croped_image = numpy_image[y_min:y_max, x_min:x_max]


        image_from_arr = Image.fromarray(croped_image)

        buff = BytesIO()

        image_from_arr.save(buff,format="JPEG")

        encoded = base64.b64encode(buff.getvalue()).decode("utf-8")

        encoded_dict = {"image":encoded}

        return jsonify (encoded_dict) ,200

        


@app.route('/face_extract',methods=["POST"])
def face_extract():
    imgarr = Image.open(request.files["file"])
    return face_extract_r(imgarr=imgarr)
    


def is_within(detected_box, bounding_box):
    dxmin, dymin, dxmax, dymax = detected_box
    bxmin, bymin, bxmax, bymax = bounding_box
    
    return dxmin >= bxmin and dymin >= bymin and dxmax <= bxmax and dymax <= bymax

@app.route('/detect', methods=['POST'])
def detect():
    data = request.get_json()
    
    bounding_boxes = data.get('bounding_boxes', [])
    detected_box = data.get('detected_box', None)
    
    if detected_box is None or not bounding_boxes:
        return jsonify({'error': 'Invalid input'}), 400
    
    for index, bounding_box in enumerate(bounding_boxes):
        if is_within(detected_box, bounding_box):
            return jsonify({'index': index}), 200
    
    return jsonify({'index': -1}), 200  


