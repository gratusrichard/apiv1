
import cv2
from rmn import RMN
m = RMN()
from flask import jsonify
import numpy
def emotion_det(image):

        opencvImage = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
        results = m.detect_emotion_for_single_frame(opencvImage)
        if results:
            return jsonify(results)
        else:
            return None
        
