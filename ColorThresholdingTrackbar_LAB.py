import cv2
import numpy as np

def empty(a):
        pass

# create new window with trackbar for HSV Color

cv2.namedWindow("Range LAB")
cv2.createTrackbar('l_L','Range LAB',0,100,empty)
cv2.createTrackbar('h_L','Range LAB',100,100,empty)
cv2.createTrackbar('l_A','Range LAB',0,255,empty)
cv2.createTrackbar('h_A','Range LAB',255,255,empty)
cv2.createTrackbar('l_B','Range LAB',0,255,empty)
cv2.createTrackbar('h_B','Range LAB',255,255,empty)

# read image
image = cv2.imread("test4.jpg")
scale_percent = 20
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent/ 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA) 
src_copy = image.copy()

img = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)
while True:

        # convert image to LAB


        #print(img[1, 0, 0])

        
        l_L = cv2.getTrackbarPos('l_L', 'Range LAB')
        h_L = cv2.getTrackbarPos('h_L', 'Range LAB')        
        l_A = cv2.getTrackbarPos('l_A', 'Range LAB')
        h_A = cv2.getTrackbarPos('h_A', 'Range LAB')        
        l_B = cv2.getTrackbarPos('l_B', 'Range LAB')
        h_B = cv2.getTrackbarPos('h_B', 'Range LAB')        
        
        lower_range = np.array([l_L, l_A, l_B])
        upper_range = np.array([h_L, h_A, h_B])
        
        thresh = cv2.inRange(img, lower_range, upper_range)
        
        bitwise = cv2.bitwise_and(img, img, mask=thresh)
        #img[:] = img[:] + [l, a, b]
        
        cv2.imshow("Original Image", image)
        cv2.imshow("LAB Image", thresh) 
        cv2.imshow("bitwise Image", bitwise)             

        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
                mode = not mode
        elif k == 27:
                break

cv2.destroyAllWindows()
