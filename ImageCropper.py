import cv2
import numpy as np
import os
from os import listdir
drawn = False 
startx, starty = -1, -1 
rectangle = (0, 0, 0, 0)

CURRENT_DIRECTORY = os.getcwd()

def load_and_resize(path):
   image = cv2.imread(path)
   new_size = (300, 300)
   resized_image = cv2.resize(image, new_size, interpolation=cv2.INTER_AREA)
   return resized_image
   
def select_roi(event, newx, newy, flags, params):
    global startx, starty, drawn, rectangle
    if event == cv2.EVENT_LBUTTONDOWN:
        startx, starty = newx, newy
        cv2.circle(image, (startx, starty), 4, (255, 255, 120), -1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawn = True
        rectangle = (startx, starty, startx - newx, starty - newy) 
        print("\nROI Selected Successfully")
        cv2.rectangle(image, (startx, starty), (newx, newy), (255, 255, 255), 2)
        cv2.imwrite('ROI_Cropping.jpg', image)
        cv2.imshow('img.jpg', image)
        cv2.waitKey(0)

def extract_foreground(image): 
    global drawn

    cv2.namedWindow(winname='BG Subractor')
    cv2.setMouseCallback('BG Subractor', select_roi)

    print("\nSelect ROI from mouse pointer.")

    black_mask = np.zeros(image.shape[:2], np.uint8)
    background = np.zeros((1, 65), np.float64)
    foreground = np.zeros((1, 65), np.float64)
    while True:  
        if drawn:
            print("\nPerforming Background Subtraction")
           
            cv2.grabCut(image, black_mask, rectangle,background, foreground,5, cv2.GC_INIT_WITH_RECT)

            mask2 = np.where((black_mask == 2) | (black_mask == 0), 0, 1).astype('uint8')

            image = image * mask2[:, :, np.newaxis]

            drawn = False
            print("\nExtraction complete")

        cv2.imshow('BG Subractor', image)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cv2.destroyAllWindows()       

image = load_and_resize(os.path.join(CURRENT_DIRECTORY, "Kenya_244_TTKSK_Pics_1_2021-03-08-05-19-12.jpg") 
extract_foreground(image)
cv2.imwrite("roi_{0}".format("output.jpg"), image)