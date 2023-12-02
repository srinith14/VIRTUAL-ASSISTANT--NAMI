#import cv2
#from cv2 import face
#import os
#import numpy as np 
#import facerec1 as fr 


##This module take images stored in diskand perform face detection
#test_img = cv2.imread('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/Test_Images/yash(1).jpg')
#faces_detected,gray_img = fr.faceDetection(test_img)

#print("faceDetected: ",faces_detected)

##faces,faceID = fr.labels_for_training('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingImages')
##face_recognizer = fr.train_classifier(faces,faceID)
##face_recognizer.write('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

###uncomment whwn you have already trained your model
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

#name={0:"Unknown",
#      1:"Sannith",
#      2:"Karthik",
#      3:"Srinith",
#      4:"Yash"}


#for face in faces_detected:
#    (x,y,w,h) = face
#    roi_gray = gray_img[y:y+h,x:x+h]
#    label,confidence = face_recognizer.predict(roi_gray)
#    #print("confidence: ",confidence)
#    #print("label ",label)
#    print("Lable: {} with confidence: {}".format(label, confidence))
#    if label == name:
#        print(name)
#    fr.draw_rect(test_img,face)
#    predicted_name = name[label]
#    if(confidence>37):
#        continue
#    fr.put_text(test_img,predicted_name,x,y)
    
#resized_img = cv2.resize(test_img,(1000,1000))
#cv2.imshow("Faces detection tutorial",resized_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()


#import cv2
#from cv2 import face
#import os
#import numpy as np 
#import facerec1 as fr 

## This module takes images stored in disk and performs face detection
#test_img = cv2.imread('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/Test_Images/yash(1).jpg')
#faces_detected, gray_img = fr.faceDetection(test_img)

#print("Faces Detected: ", faces_detected)

## faces,faceID = fr.labels_for_training('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingImages')
## face_recognizer = fr.train_classifier(faces, faceID)
## face_recognizer.write('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

## Uncomment when you have already trained your model
#face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

#name = {0:"Unknown", 1:"Sannith", 2:"Karthik", 3:"Srinith", 4:"Yash"}

#for face in faces_detected:
#    (x,y,w,h) = face
#    roi_gray = gray_img[y:y+h,x:x+h]
#    label, confidence = face_recognizer.predict(roi_gray)
#    predicted_name = name[label]
#    print("Lable: {} with confidence: {}".format(predicted_name, confidence))
#    fr.draw_rect(test_img, face)
#    if confidence > 37:
#        continue
#    fr.put_text(test_img, predicted_name, x, y)

#resized_img = cv2.resize(test_img, (1000, 1000))
#cv2.imshow("Faces Detection Tutorial", resized_img)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

import cv2
from cv2 import face
import os
import numpy as np 
import facerec1 as fr 


# This module takes an image stored in disk and performs face detection
test_img = cv2.imread('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/Test_Images/yash(1).jpg')
faces_detected, gray_img = fr.faceDetection(test_img)

print("Faces Detected: ", faces_detected)

#faces,faceID = fr.labels_for_training('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingImages')
#face_recognizer = fr.train_classifier(faces,faceID)
#face_recognizer.write('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

# Load the trained face recognizer model
face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

# Define a dictionary to map label numbers to names
name = {
    0: "Unknown",
    1: "Sannith",
    2: "Karthik",
    3: "Srinith",
    4: "Yash"
}

# Loop through each detected face and predict its label
for face in faces_detected:
    (x, y, w, h) = face
    roi_gray = gray_img[y:y+h, x:x+h]
    label, confidence = face_recognizer.predict(roi_gray)
    predicted_name = name[label]
    #print("Lable: {} with confidence: {}".format(predicted_name, confidence))
    print("Lable: {} ".format(predicted_name))
    # Put the predicted name and confidence score on the image
    text = f"{predicted_name}  ({confidence:.2f})"
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    color = (255, 255, 255)
    thickness = 3
    cv2.putText(test_img, text, (x, y-10), font, font_scale, color, thickness, cv2.LINE_AA)
    
    fr.draw_rect(test_img, face)

# Resize and display the image
resized_img = cv2.resize(test_img, (640, 480))
cv2.imshow("Faces Detection Tutorial", resized_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
