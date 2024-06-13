import gradio as gr
from retinaface import RetinaFace
import numpy as np
import cv2
import os


# Create the output folder if it doesn't exist
output_folder = "output"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

def face_extract_r(image):
    faces = RetinaFace.extract_faces(img_path=image)
    extracted_faces_paths = []

    for i, face in enumerate(faces):
        face_path = os.path.join(output_folder, f"face_{i}.jpg")
        cv2.imwrite(face_path, face)
        
        extracted_faces_paths.append(face_path)

    return extracted_faces_paths

iface = gr.Interface(
    fn=face_extract_r,
    inputs="image",
    outputs="text",
    title="Face Extraction",
    description="Upload an image with faces, and the extracted faces will be saved locally in the 'output' folder."
)

iface.launch(share=False)
