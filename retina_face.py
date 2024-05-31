from retinaface import RetinaFace
from flask import jsonify
import numpy as np
import cv2
from io import BytesIO
import base64
from PIL import Image

def face_det(image):
    numpy_image = np.array(image)
    cv2_image = cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)

    det = RetinaFace.detect_faces(cv2_image)
    print(det)
    serilializable_det = convert_to_serializable(det)

    return jsonify(serilializable_det),200


def convert_to_serializable(det):
    if isinstance(det, dict):
        serializable_det = {}
        for key, value in det.items():
            serializable_det[key] = convert_to_serializable(value)
        return serializable_det
    elif isinstance(det, list):
        return [convert_to_serializable(item) for item in det]
    elif isinstance(det, np.ndarray):
        return det.tolist()
    elif isinstance(det, (np.int32, np.int64)):
        return int(det)
    elif isinstance(det, (np.float32, np.float64)):
        return float(det)
    else:
        return det


def face_extract_r(imgarr):

    images =[]
    personsimages={}

    source = imgarr
    numpyimage = np.array(source)
    source = numpyimage
    # source = cv2.imread(source)
    cv2converted = cv2.cvtColor(numpyimage,cv2.COLOR_RGB2BGR)

    source = cv2converted
    
    # source = cv2.resize(numpyimage,source.shape)

    faces = RetinaFace.extract_faces(img_path = source, align = True)

    # print(persons[0].boxes.xyxy[0])
    
    if (len(faces) >0):

        i=0
        for face in faces:
            
            # x_min,y_min,x_max,y_max = map (int,person)

            # cropped_person = source[y_min:y_max,x_min:x_max]
            # target_dpi = 500
            # current_dpi = 96  
            # scaling_factor = target_dpi / current_dpi
            # cropped_person = cv2.resize(cropped_person, None, fx=scaling_factor, fy=scaling_factor)
            # cv2.imwrite(f"/home/rtx/vechile_cropper_poc/results/test{i}.jpg",cropped_person)
            buff = BytesIO()
            fromarrayimage = Image.fromarray(face)
            fromarrayimage.save(buff,format="JPEG")
            encoded = base64.b64encode(buff.getvalue()).decode("utf-8")
            personsimages[f'img{i}.jpg'] = encoded
            images.append(personsimages)
            personsimages  = {}

            i+=1
        responseper = {'total':str(i),
                    'images ': images

            }
            


        return responseper,200
    else:
         return None,299