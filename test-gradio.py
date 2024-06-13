import gradio as gr
from deepface import DeepFace
import numpy as np
from PIL import Image
import json

def image_comp(image1, image2):
    # Convert the PIL images to numpy arrays
    image1_np = np.array(image1)
    image2_np = np.array(image2)
    
    # Save images to disk temporarily
    image1_path = "temp_image1.jpg"
    image2_path = "temp_image2.jpg"
    Image.fromarray(image1_np).save(image1_path)
    Image.fromarray(image2_np).save(image2_path)
    
    try:
        # Perform face verification
        verification_result = DeepFace.verify(image1_path, image2_path, model_name="Facenet512", detector_backend='retinaface', enforce_detection=False,distance_metric="eucledian")
        
        # Perform emotion analysis on the first image (as an example)
        emotion_result = DeepFace.analyze(image1_path, actions=['emotion', 'race'], enforce_detection=False)
        
        # Format the results
        formatted_result = {
            "Verification Result": {
                "Verified": verification_result['verified'],
                "Distance": verification_result['distance'],
                "Threshold": verification_result['threshold'],
                "Model": verification_result['model'],
                "Detector Backend": verification_result['detector_backend'],
                "Similarity Metric": verification_result['similarity_metric'],
                "Facial Areas": verification_result['facial_areas'],
                "Time": verification_result['time']
            },
            "Emotion Analysis Result": {
                "Dominant Emotion": emotion_result[0]['dominant_emotion'],
                "Emotion Scores": emotion_result[0]['emotion'],
                "Region": emotion_result[0]['region'],
                "Face Confidence": emotion_result[0]['face_confidence'],
                "Dominant Race": emotion_result[0]['dominant_race'],
                "Race Scores": emotion_result[0]['race']
            }
        }

        # Convert the result to a JSON string for better display
        return json.dumps(formatted_result, indent=4)
    except Exception as e:
        return str(e)

demo = gr.Interface(
    fn=image_comp,
    inputs=[gr.Image(type="pil"), gr.Image(type="pil")],
    outputs="text"  # Use 'text' output type to display the JSON string
)

demo.launch(debug=True)
