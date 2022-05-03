import cv2
import numpy as np
import os
from os import listdir
def empty(a):
        pass
        
CURRENT_DIRECTORY = os.getcwd()        

# create new window with trackbar for HSV Color

cv2.namedWindow("Range HSV")
cv2.resizeWindow("Range HSV", 500, 350)
cv2.createTrackbar("HUE Min", "Range HSV", 0,180,empty)
cv2.createTrackbar("HUE Max", "Range HSV", 180,180,empty)
cv2.createTrackbar("SAT Min", "Range HSV", 0,255,empty)
cv2.createTrackbar("SAT Max", "Range HSV", 255,255,empty)
cv2.createTrackbar("VALUE Min", "Range HSV", 0,255,empty)
cv2.createTrackbar("VALUE Max", "Range HSV", 255,255,empty)

# read image
files = [f for f in listdir(os.path.join(CURRENT_DIRECTORY, "Pics TTKSK"))]

for f in files:
    image = cv2.imread(os.path.join(CURRENT_DIRECTORY, "Pics TTKSK", f))
    scale_percent = 20
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent/ 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA) 
    src_copy = image.copy()
    #src_copy = cv2.cvtColor(src_copy, cv2.COLOR_BGR2GRAY)

    #im2, contours, hierarchy = cv2.findContours(src_copy, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #print(len(contours))


    cv2.imwrite('ctrs.jpg', image)
    while True:

            # get value from trackbar
        h_min = cv2.getTrackbarPos("HUE Min", "Range HSV")
        h_max = cv2.getTrackbarPos("HUE Max", "Range HSV")
        s_min = cv2.getTrackbarPos("SAT Min", "Range HSV")
        s_max = cv2.getTrackbarPos("SAT Max", "Range HSV")
        v_min = cv2.getTrackbarPos("VALUE Min", "Range HSV")
        v_max = cv2.getTrackbarPos("VALUE Max", "Range HSV")
        print('hi')


            # define range of some color in HSV

        lower_range = np.array([h_min, s_min, v_min])
        upper_range = np.array([h_max, s_max, v_max])
        print('i')


    # convert image to HSV

        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # threshold the hsv image to get some color

        thresh = cv2.inRange(hsv, lower_range, upper_range)

    # bitwise AND mask and original image

        bitwise = cv2.bitwise_and(image, image, mask=thresh)
    
        cv2.imwrite("{0}".format(f), bitwise)