import cv2
# adding pretrained data from the haar casacde algorithm 

from random import randrange
# importing libraries for generating random numbers


trained_face_data= cv2. CascadeClassifier ('haarcascade_frontal_facedetection.xml')

# choose an img
#img =cv2.imread('frnds2.webp')

webcam= cv2.VideoCapture(0)
# to detect faces from a given video cv2.VideoCapture('video_address')
#to capture video from the webcam.

#iterate over frames forever
while True:

    #read the current frame
    successful_frame_read, frame= webcam.read()

    if successful_frame_read:
       

#convert to grayscale(as computer understands in that form)

      grayscaled_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    else:
       break
    
# #detect faces

    face_cordinates = trained_face_data.detectMultiScale(grayscaled_img)


# #draw rectangle around the faces
# #loop for iterating for each face  
    for (x,y,w,h) in face_cordinates: 
   
    #    cv2.rectangle(frame, (x,y),(x+w, y+h), (randrange(256), randrange(256), randrange(256)) ,2)
     cv2.rectangle(frame, (x,y),(x+w, y+h), (0, 255, 0) ,2)
# # cordinates- (x,y)(x+w, y+h). display images with faces 
 
#     print(face_cordinates)

    cv2. imshow('Clever Programmer Face Detector', frame)

# #pauses the execution until some key is pressed
    key= cv2.waitKey(1)
    if key==81 or key==113:
        break

webcam.release()
print ("It works perfectly!") 