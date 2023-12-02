##import cv2
##import os
##import numpy as np 
##import facerec1 as fr

###capture image from web cam first
##face_recognizer = cv2.face.LBPHFaceRecognizer_create()
##face_recognizer.read('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

###face_recognizer.read('trainingData.yml')

##name={0:"Unknown",
##      1:"Sannith",
##      2:"Karthik",
##      3:"Srinith",
##      4:"Yash"}


##cam = cv2.VideoCapture(0)

##while True:
##    ret, test_img = cam.read()
##    faces_detected,gray_img = fr.faceDetection(test_img)

##    for (x,y,w,h) in faces_detected:
##        cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=6)

##    resized_img =cv2.resize(test_img,(1000,700))
##    cv2.imshow('FAce detection tutorial',resized_img)
##    cv2.waitKey(10)

##    for face in faces_detected:
##        (x,y,w,h) = face
##        roi_gray = gray_img[y:y+w,x:x+h]
##        label,confidence = face_recognizer.predict(roi_gray)
##        print(confidence,label)
##        fr.draw_rect(test_img,face)
##        predicted_name = name[label]
##        if confidence < 60:
##            fr.put_text(test_img,predicted_name,x,y)

##    resized_img = cv2.resize(test_img,(1000,700))
##    cv2.imshow("Face Rcognition",resized_img)
##    if cv2.waitKey(10) == ord('q'):
##        break

##cam.release()
##cv2.destroyAllWindows()


##import cv2
##import os
##import numpy as np 
##import facerec1 as fr

###capture image from web cam first
##face_recognizer = cv2.face.LBPHFaceRecognizer_create()
##face_recognizer.read('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

###face_recognizer.read('trainingData.yml')

##name={0:"Unknown",
##      1:"Sannith",
##      2:"Karthik",
##      3:"Srinith",
##      4:"Yash"}


##cam = cv2.VideoCapture(0)

##while True:
##    ret, test_img = cam.read()
##    faces_detected,gray_img = fr.faceDetection(test_img)

##    for (x,y,w,h) in faces_detected:
##        cv2.rectangle(test_img,(x,y),(x+w,y+h),(255,0,0),thickness=2)

##    resized_img =cv2.resize(test_img,(1000,700))
##    #cv2.imshow('FAce detection tutorial',resized_img)
##    #cv2.waitKey(10)

##    for face in faces_detected:
##        (x,y,w,h) = face
##        roi_gray = gray_img[y:y+w,x:x+h]
##        label,confidence = face_recognizer.predict(roi_gray)
##        predicted_name = name[label]
##        if confidence < 60:
##            fr.draw_rect(test_img,face)
##            fr.put_text(test_img,predicted_name,x,y)
##            print("Predicted name: {} with confidence: {}".format(predicted_name, confidence))
##            print()

##    resized_img = cv2.resize(test_img,(1000,700))
##    cv2.imshow("Face Recognition",resized_img)
##    if cv2.waitKey(10) == ord('q'):
##        break

##cam.release()
##cv2.destroyAllWindows()


#import cv2
#import facerec1 as fr
#import time
#import orginalNami as nami

#face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#face_recognizer.read('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

#name = {0: "Unknown",
#        1: "Sannith",
#        2: "Karthik",
#        3: "Srinith",
#        4: "Yash"}

#font = cv2.FONT_HERSHEY_SIMPLEX
#font_scale = 0.7
#font_thickness = 1
#text_padding = 5

#cam = cv2.VideoCapture(0)
#cam.set(3, 640)
#cam.set(4, 480)
#minW = 0.1*cam.get(3)
#minH = 0.1*cam.get(4)
#start_time = time.time()

#face_detected = False
#while True:
#    ret, test_img = cam.read()
#    faces_detected, gray_img = fr.faceDetection(test_img)

#    for (x, y, w, h) in faces_detected:
#        cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
#        face_detected = True

#    if face_detected:
#        for face in faces_detected:
#            (x, y, w, h) = face
#            roi_gray = gray_img[y:y + w, x:x + h]
#            label, confidence = face_recognizer.predict(roi_gray)
#            fr.draw_rect(test_img, face)
#            predicted_name = name[label]
#            #print("Predicted name: {} with confidence: {}".format(predicted_name, confidence))

#            if confidence < 100:
#                (tw, th), _ = cv2.getTextSize(predicted_name, font, font_scale, font_thickness)
#                tx = max(0, x + w // 2 - tw // 2)
#                ty = max(0, y - text_padding - th)
#                cv2.putText(test_img, predicted_name, (tx, ty), font, font_scale, (255, 255, 255), font_thickness,
#                            cv2.LINE_AA)
#                print("Face Recognized.")
#                print("Predicted name: {} with confidence: {}".format(predicted_name, confidence))
#                if predicted_name in name:
#                    nami.run()
#                else:
#                    pass
##                    print("Access denied.")
#            else:
#                print("Face not Recognized....")
#    #else:
#    #    #print("Face not Recognized....")
#    #    #face_detected = False
#    #    break

#    resized_img = cv2.resize(test_img, (640, 480))
#    cv2.imshow("Face Recognition", resized_img)
#    elapsed_time = time.time() - start_time
#    if elapsed_time > 3:
#        break
#    k = cv2.waitKey(10) & 0xff 
#    if k == 27:
#        break

#cam.release()
#cv2.destroyAllWindows()

import cv2
import facerec1 as fr
import time
import orginalNami as nami

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

name = {0: "Unknown",
        1: "Sannith",
        2: "Karthik",
        3: "Srinith",
        4: "Yash"}

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 0.7
font_thickness = 1
text_padding = 5

cam = cv2.VideoCapture(0)
cam.set(3, 640)
cam.set(4, 480)
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)
start_time = time.time()

def recognition():
    face_detected = False
    recognized = False
    while True:
        ret, test_img = cam.read()
        faces_detected, gray_img = fr.faceDetection(test_img)

        for (x, y, w, h) in faces_detected:
            cv2.rectangle(test_img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
            face_detected = True

        if face_detected:
            for face in faces_detected:
                (x, y, w, h) = face
                roi_gray = gray_img[y:y + w, x:x + h]
                label, confidence = face_recognizer.predict(roi_gray)
                fr.draw_rect(test_img, face)
                predicted_name = name[label]

                if confidence < 70:
                    (tw, th), _ = cv2.getTextSize(predicted_name, font, font_scale, font_thickness)
                    tx = max(0, x + w // 2 - tw // 2)
                    ty = max(0, y - text_padding - th)
                    cv2.putText(test_img, predicted_name, (tx, ty), font, font_scale, (255, 255, 255), font_thickness,
                                cv2.LINE_AA)
                    print("Face Recognized.")
                    #print("Predicted name: {} with confidence: {}".format(predicted_name, confidence))
                    print("Predicted name: {} ".format(predicted_name))
                    recognized = True
                else:
                    print("Face not ////Recognized.")
                    recognized = False
                    break
        else:
            print("Face not Recognized....")
            recognized = False

        resized_img = cv2.resize(test_img, (640, 480))
        cv2.imshow("Face Recognition", resized_img)
        elapsed_time = time.time() - start_time
        if elapsed_time > 3:
            break
        k = cv2.waitKey(10) & 0xff 
        if k == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    return recognized

#recognition()

if recognition():
     pass
     nami.run_Nami()  # if recognized, run Nami virtual assistant
else:
    print("Access Denied.")  # if not recognized, access denied.
    pass