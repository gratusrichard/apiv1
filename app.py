from flask import Flask,request,jsonify
from PIL import Image
from YoloObjectdet import detect
from emotion import emotion_det
from yoloPretrained import detect_pretrained
from retina_face import face_det, face_extract_r,half_body
import numpy as np
import base64
from io import BytesIO
from deepface import DeepFace


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



#crowd detection
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
    

#face detection
@app.route("/face", methods=["POST"])
def face():
    imgarr = Image.open(request.files['file'])

    return face_det(imgarr)

#image roi cropping 
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

        

#face extraction
@app.route('/face_extract',methods=["POST"])
def face_extract():
    imgarr = Image.open(request.files["file"])
    return face_extract_r(imgarr=imgarr)
    

#within roi
def is_within(detected_box, bounding_box):
    dxmin, dymin, _, _ = detected_box
    bxmin, bymin, bxmax, bymax = bounding_box
    
    return dxmin >= bxmin and dymin >= bymin and dxmin <= bxmax and dymin <= bymax
#within roi endpoint
@app.route("/detect", methods=["POST"])
def detect_object():
  data = request.get_json()

  if not data:
    return jsonify({"error": "Missing data in request body"}), 400

  bounding_boxes = data.get("bounding_boxes", {})
  detected_box = data.get("detected_box")

  if not bounding_boxes or not detected_box:
    return jsonify({"error": "Missing required fields in data"}), 400

  detected_x1, detected_y1 = detected_box[0], detected_box[1]

  for box_name, box in bounding_boxes.items():
    box_x1, box_y1, box_x2, box_y2 = box

    if detected_x1 >= box_x1 and detected_x1 <= box_x2 and detected_y1 >= box_y1 and detected_y1 <= box_y2:
      return jsonify({"bounding_box": box_name})

  return jsonify({"bounding_box": None})

#Face Recognition

@app.route('/facerecog',methods=["POST"])
def faceRecog():
    face1 = request.files['face1']
    face2 = request.files['face2']
    face1 = Image.open(face1)
    face2 = Image.open(face2)

    face1 = np.array(face1)
    face2 = np.array(face2)

    face_recog = DeepFace.verify(face1,face2,model_name="Facenet512",detector_backend='retinaface',enforce_detection=False)
    face_analyze = DeepFace.analyze( face2,
        actions = ['emotion','race'],enforce_detection=False)
    
    
    
    return {'facerecog':face_recog,
            'faceanalyze':face_analyze}



    
    
@app.route("/peoplehalf", methods=['POST'])
def peoplehalf():
        imgarr = Image.open(request.files["file"])
        return half_body(imgarr)


