# Face Recognition by Prerna Mishra
#importing libraries
import cv2
#creating the cascades
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') # We load the cascade for the face.
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml') # We load the cascade for the eyes.


#Creating a function to detect images
def detect(gray, frame): 
    #function that takes as input the image in black and white (gray) and the original image (frame), and that will return the same image with the detector rectangles. 
    faces = face_cascade.detectMultiScale(gray, 1.3, 5) # We apply the detectMultiScale method from the face cascade to locate one or several faces in the image.
    for (x, y, w, h) in faces: # For each detected face:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5) #blue color 
        # We paint a rectangle around the face.
        roi_gray = gray[y:y+h, x:x+w] 
        # We get the region of interest in the black and white image.
        roi_color = frame[y:y+h, x:x+w] 
        # We get the region of interest in the colored image.
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 3) 
        # We apply the detectMultiScale method to locate one or several eyes in the image.
        for (ex, ey, ew, eh) in eyes: # For each detected eye:
            cv2.rectangle(roi_color,(ex, ey),(ex+ew, ey+eh), (0, 255, 0), 5) 
            # We paint a rectangle around the eyes with green, but inside the referential of the face.
    return frame # We return the image with the detector rectangles.


video_capture = cv2.VideoCapture(0) # We turn the webcam on.
#Displyaing the detection on images
while True: # We repeat infinitely (until break that is press q):
    _, frame = video_capture.read() # We get the last frame using read.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # We do some colour transformations.
    canvas = detect(gray, frame) # We get the output of our detect function.
    cv2.imshow('Video', canvas) # We display the outputs.
    if cv2.waitKey(1) & 0xFF == ord('q'): # If we type on the keyboard q:
        break # We stop the loop.
        
        
#closing all the windows after keypress
video_capture.release() # We turn the webcam off.
cv2.destroyAllWindows() # We destroy all the windows inside which the images were displayed.