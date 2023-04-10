import cv2
trainedFaceData = cv2.CascadeClassifier('trainedData\haarcascade_frontalface_default.xml')
trainedEyeData = cv2.CascadeClassifier('trainedData\haarcascade_eye.xml')
trainedSmileData = cv2.CascadeClassifier('trainedData\haarcascade_smile.xml')

Face = False
Eye = False
Glasses = False
Smile = False


opt = input("what are all the features do u want to detect:\n1.Face\n2.Eye\n3.Smile\n4.All\nYour option: ")
for character in opt:
    if character == "1":
        Face = True
    elif character == "2":
        Eye = True
    elif character == "3":
        Smile = True
    elif character == "4":
        Face = True
        Eye = True
        Glasses = True
        Smile = True


webcam = cv2.VideoCapture(0)

while True:

    successfullFrameRead, frame = webcam.read()

    grayscledImg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

   
    faceCoordinates = trainedFaceData.detectMultiScale(grayscledImg)
    for (x,y,w,h) in faceCoordinates:
        if Face == True:
            cv2.rectangle(frame, (x,y),(x+w,y+h),(0, 225, 0), 2)
            cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

        theFace = frame[y:y+h,x:x+w]
        grayscledtheFace =  cv2.cvtColor(theFace, cv2.COLOR_BGR2GRAY)
        if Smile == True:        
            smileCoordinates = trainedSmileData.detectMultiScale(grayscledtheFace,scaleFactor=1.7, minNeighbors=20)
            for (x_,y_,w_,h_) in smileCoordinates:
                cv2.rectangle(theFace, (x_,y_),(x_+w_,y_+h_),(225, 0, 0), 2)
                cv2.putText(frame, 'smiling', (x_, y_+10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (225, 0, 0), 2)

        if Eye == True:
            eyeCoordinates = trainedEyeData.detectMultiScale(grayscledtheFace,scaleFactor=1.1, minNeighbors=10)
            for (x__,y__,w__,h__) in eyeCoordinates:
                cv2.rectangle(theFace, (x__, y__),(x__+w__, y__+h__),(0, 0, 225), 2)


    cv2.imshow('FaceDetector RealTime',frame)
    key = cv2.waitKey(1)
    
    if key == 27:
        break