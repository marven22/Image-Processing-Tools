import cv2
import numpy as np
import os

count = 0
for img_name in os.listdir(".\\HSV_Thresholded_Images_TTKSK"):
    #print(img)
    # load resized image as grayscale
    img = cv2.imread(".\\HSV_Thresholded_Images_TTKSK\\" + "Kenya_1_TTKSK_Pics_1_2021-03-08-03-07-10.jpg")
    h, w, _ = img.shape
    #print(h,w)

    # load background image as grayscale
    back = np.zeros([600, 600, 3], dtype= np.uint8)#cv2.imread('background.png', cv2.IMREAD_GRAYSCALE)
    hh, ww, _ = back.shape
    print(hh,ww)

    # compute xoff and yoff for placement of upper left corner of resized image   
    yoff = round((hh-h)/2)
    xoff = round((ww-w)/2)
    #print(yoff,xoff)

    # use numpy indexing to place the resized image in the center of background image
    try:
        result = back.copy()
        result[yoff:yoff+h, xoff:xoff+w] = img

    # view result
    #cv2.imshow('CENTERED', result)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

        result = cv2.resize(result, (224, 224), interpolation=cv2.INTER_AREA)
        print(img_name)
        cv2.imshow('result.jpg', result)
        cv2.waitKey(0)
        cv2.imwrite(os.path.join('.\\3_success', img_name), result)
        os.remove('.\\3_test\\{0}'.format(img_name))
        count += 1
    except:
        cv2.imwrite(os.path.join('.\\3_test', img_name), img)
    # save resulting centered image
    #print(type(img))
