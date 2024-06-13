# from retinaface import RetinaFace
# import cv2

# # Detect faces
# resp = RetinaFace.detect_faces(r"C:\Users\gratu\Downloads\peoplesp.jpg")

# # Get the facial area of the first detected face
# facial_area = resp['face_1']['facial_area']
# x1, y1, x2, y2 = facial_area

# # Calculate the dimensions of the face
# face_width = x2 - x1
# face_height = y2 - y1
# image = cv2.imread(r'C:\Users\gratu\Downloads\peoplesp.jpg')

# # Expand the bounding box by a 3:3 ratio
# new_x1 = int(max(0, x1 - 1.2*face_width))
# new_y1 = int(max(0,y1 - 0.25 *face_height))
# new_x2 = int(min(image.shape[1], x2 + 1.2*face_width))
# new_y2 = int(min(image.shape[0], y2 + 3*face_height))

# # Read the image

# # Draw the expanded rectangle around the detected half-body region
# image_with_rectangle = cv2.rectangle(image.copy(), (new_x1, new_y1), (new_x2, new_y2), color=(255, 255, 0), thickness=2)

# # Crop the expanded region from the image
# cropped_image = image[new_y1:new_y2, new_x1:new_x2]

# # Display the image with the rectangle
# cv2.imshow('Expanded Bounding Box', image_with_rectangle)
# cv2.waitKey(0)

# # Display the cropped half-body image
# cv2.imshow('Cropped Half Body', cropped_image)
# cv2.waitKey(0)

# # Destroy all OpenCV windows
# cv2.destroyAllWindows()





from retina_face import half_body
import cv2

image = cv2.imread(r'C:\Users\gratu\Downloads\testcrowd.jpg')
half_body(image)