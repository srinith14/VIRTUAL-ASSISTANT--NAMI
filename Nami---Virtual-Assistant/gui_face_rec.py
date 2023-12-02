#import cv2
#import facerec1 as fr
#import tkinter as tk

#class FaceRecognitionGUI:
#    def __init__(self, window):
#        self.window = window
#        self.window.title("Face Recognition GUI")

#        self.login_button = tk.Button(self.window, text="Login", width=10, command=self.login)
#        self.login_button.pack(pady=10)

#        self.logout_button = tk.Button(self.window, text="Logout", width=10, command=self.logout, state="disabled")
#        self.logout_button.pack(pady=10)

#        self.label = tk.Label(self.window, text="")
#        self.label.pack(pady=10)

#        self.video_capture = cv2.VideoCapture(0)

#        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
#        self.face_recognizer.read('C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml')

#        self.names = {0: "Unknown",
#                      1: "Sannith",
#                      2: "Karthik",
#                      3: "Srinith",
#                      4: "Yash"}

#        self.font = cv2.FONT_HERSHEY_SIMPLEX
#        self.font_scale = 0.7
#        self.font_thickness = 1
#        self.text_padding = 5


#    def login(self):
#        self.login_button.config(state="disabled")
#        self.logout_button.config(state="normal")
#        self.label.config(text="Welcome!")
#        self.recognize_face()


#    def logout(self):
#        self.video_capture.release()
#        cv2.destroyAllWindows()
    
#        self.logged_in = False
#        self.logout_button.config(state="disabled")
#        self.login_button.config(state="normal")
#        self.label.config(text="Logging out... please wait")
#        self.window.destroy()


#    def recognize_face(self):
#        ret, frame = self.video_capture.read()
#        #frame = cv2.flip(frame, 1)
#        faces_detected, gray_img = fr.faceDetection(frame)

#        for (x, y, w, h) in faces_detected:
#            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), thickness=2)

#        for face in faces_detected:
#            (x, y, w, h) = face
#            roi_gray = gray_img[y:y + w, x:x + h]
#            label, confidence = self.face_recognizer.predict(roi_gray)
#            predicted_name = self.names[label]

#            if confidence < 60:
#                (tw, th), _ = cv2.getTextSize(predicted_name, self.font, self.font_scale, self.font_thickness)
#                tx = max(0, x + w // 2 - tw // 2)
#                ty = max(0, y - self.text_padding - th)
#                cv2.putText(frame, predicted_name, (tx, ty), self.font, self.font_scale, (255, 255, 255), self.font_thickness,
#                            cv2.LINE_AA)

#        resized_frame = cv2.resize(frame, (640, 480))
#        cv2.imshow('Face Recognition', resized_frame)

#        if cv2.waitKey(1) & 0xFF == ord("a"):
#            self.video_capture.release()
#            cv2.destroyAllWindows()
#        else:
#            self.window.after(10, self.recognize_face)

#if __name__ == "__main__":
#    window = tk.Tk()
#    gui = FaceRecognitionGUI(window)
#    window.mainloop()

#def add_user(self, name):
#    """
#    Add a new user to the face recognition system.
#    """
#    # Create a new folder with the user's name
#    dir_path = os.path.join(self.dataset_path, name)
#    os.makedirs(dir_path, exist_ok=True)

#    # Open the video stream
#    self.video_capture = cv2.VideoCapture(0)

#    # Loop over frames from the video stream
#    frame_count = 0
#    while True:
#        # Capture the frame from the video stream
#        ret, frame = self.video_capture.read()

#        # Quit if no frame is available
#        if not ret:
#            break

#        # Display the current frame
#        cv2.imshow("Add User", frame)
#        key = cv2.waitKey(1) & 0xFF

#        # Save the frame if the user presses the "s" key
#        if key == ord("s"):
#            # Save the frame to the user's folder
#            image_path = os.path.join(dir_path, "{}.jpg".format(frame_count))
#            cv2.imwrite(image_path, frame)

#            # Increment the frame count
#            frame_count += 1

#            # Display a message indicating that the frame was saved
#            print("Saved frame {} for {}".format(frame_count, name))

#        # Quit if the user presses the "q" key
#        elif key == ord("q"):
#            break

#    # Release the video stream and close all windows
#    self.video_capture.release()
#    cv2.destroyAllWindows()

#    # Train the face recognition model with the new data
#    self.train_model()


import cv2
import os
import numpy as np
import tkinter as tk
from tkinter import messagebox
import datetime


class FaceRecognitionGUI:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier("C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/Haar_Cascade/haarcascade_frontalface_default.xml")
        self.video_capture = cv2.VideoCapture(0)
        self.face_recognizer = cv2.face.LBPHFaceRecognizer_create()
        self.face_recognizer.read("C:/Users/yasha/source/repos/NAMI Virtual assistant/Nami(org)/trainingData.yml")
        self.name = {0: "Unknown",
                      1: "Sannith",
                      2: "Karthik",
                      3: "Srinith",
                      4: "Yash"}
        self.logged_in = False
        self.window = tk.Tk()
        self.window.title("Face Recognition Login")
        self.window.protocol("WM_DELETE_WINDOW", self.on_exit)
        self.window.geometry("400x150")
        self.window.resizable(False, False)

        self.user_label = tk.Label(self.window, text="Please log in", font=("Arial Bold", 12))
        self.user_label.pack(pady=10)

        self.login_button = tk.Button(self.window, text="Log In", command=self.login, font=("Arial", 12))
        self.login_button.pack(pady=10)

        self.logout_button = tk.Button(self.window, text="Log Out", state="disabled", command=self.logout,
                                       font=("Arial", 12))
        self.logout_button.pack(pady=10)

        self.label = tk.Label(self.window, text="")
        self.label.pack(pady=10)

        self.window.mainloop()

    def on_exit(self):
        self.video_capture.release()
        cv2.destroyAllWindows()
        self.window.destroy()

    def update_user_label(self, name):
        self.user_label.config(text="Welcome, {}".format(name))

    def recognize_user(self):
        while True:
            ret, frame = self.video_capture.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
            name = "Unknown"
            for (x, y, w, h) in faces:
                roi_gray = gray[y:y + h, x:x + w]
                id_, confidence = self.face_recognizer.predict(roi_gray)
                if confidence < 100:
                    name = str(self.name[id_])
                    confidence = "{0}%".format(round(100 - confidence))
                else:
                    name = "Unknown"
                    confidence = "{0}%".format(round(100 - confidence))
                cv2.putText(frame, str(name), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                cv2.putText(frame, str(confidence), (x + w // 2, y + h + 30), cv2.FONT_HERSHEY_SIMPLEX, 1,
                            (255, 255, 0), 2)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("Face Recognizer", frame)
            if cv2.waitKey(1) & 0xFF == ord("a"):
                self.video_capture.release()
                cv2.destroyAllWindows()
                return name
        return name

    def login(self):
        if self.logged_in:
            messagebox.showinfo("Already Logged In", "You are already logged in.")
            return

        name = self.recognize_user()
        if name == "Unknown":
            messagebox.showerror("Error", "Face not recognized. Please try again.")
            return

        self.logged_in = True
        self.login_button.config(state="disabled")
        self.logout_button.config(state="normal")
        self.update_user_label(name)



    def logout(self):
        self.video_capture.release()
        cv2.destroyAllWindows()
        
        self.logged_in = False
        self.logout_button.config(state="disabled")
        self.login_button.config(state="normal")
    
        # Clear the user label
        self.update_user_label("")
    
        # Reset the window title and instruction label
        self.window.title("NAMI Virtual Assistant")
        self.label.config(text="Please log in to continue")




if __name__ == "__main__":
    gui = FaceRecognitionGUI()
