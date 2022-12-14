import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import time
import keyboard
import pyautogui

letterIndex = ""

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon = 0.8, maxHands=2)

classifier = Classifier("Model/keras_model.h5" , "Model/labels.txt")

offset = 20
imgSize = 300

labels = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "X", "Y"]

def letterCaptureStart():
    global letterIndex
    while True:
        succes, img = cap.read()
        imgOutput= img.copy()
        hands, img = detector.findHands(img)
        if hands:
            hand1 = hands[0]
            x,y,w,h = hand1['bbox']
                
            imgWhite = np.ones((imgSize,imgSize,3), np.uint8)*255
            imgCrop = img[y - offset : y + h + offset, x - offset : x + w + offset]
                
            imgCropShape = imgCrop.shape
                
            aspectRatio = h/w
                
            if aspectRatio > 1:
                k = imgSize/h
                wCal = math.ceil(k*w)
                imgResize = cv2.resize(imgCrop, (wCal,imgSize))
                imgResizeShape = imgResize.shape
                wGap = math.ceil((imgSize-wCal)/2)
                imgWhite[ : , wGap : wCal + wGap] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw = False)
                #print(prediction, index)
                    
            else:
                k = imgSize/w
                hCal = math.ceil(k*h)
                imgResize = cv2.resize(imgCrop, (imgSize,hCal))
                imgResizeShape = imgResize.shape
                hGap = math.ceil((imgSize-hCal)/2)
                imgWhite[hGap : hCal + hGap: ,] = imgResize
                prediction, index = classifier.getPrediction(imgWhite, draw = False)
                
            cv2.putText(imgOutput, labels[index], (x,y-20), cv2.FONT_HERSHEY_COMPLEX,2,(255,0,255), 2)
            cv2.rectangle(imgOutput, (x - offset, y - offset), (x + w + offset, y + h + offset), (255, 0, 255), 4)
            letterIndex = labels[index]
            #def letterIndex():
            #    letterIndex = labels[index]
            #    print("LetterCapture")
            #    print(letterIndex)
                
            #letterIndex()
                    
            #cv2.imshow("ImageCrop", imgCrop)
            #cv2.imshow("ImageWhite", imgWhite)
            if keyboard.is_pressed('space'):
                pyautogui.hotkey("alt","tab")
                time.sleep(1)
                
        cv2.imshow("Image", imgOutput)
        cv2.waitKey(1)
