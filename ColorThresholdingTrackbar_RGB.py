#import opencv and numpy
import cv2  
import numpy as np

#trackbar callback fucntion does nothing but required for trackbar
def nothing(x):
	pass

#create a seperate window named 'controls' for trackbar
cv2.namedWindow('controls',2)
cv2.resizeWindow("controls", 550,10);

#create trackbar in 'controls' window with name 'r''
cv2.createTrackbar('l_r','controls',0,255,nothing)
cv2.createTrackbar('l_g','controls',0,255,nothing)
cv2.createTrackbar('l_b','controls',0,255,nothing)
cv2.createTrackbar('h_r','controls',255,255,nothing)
cv2.createTrackbar('h_g','controls',255,255,nothing)
cv2.createTrackbar('h_b','controls',255,255,nothing)
#create a black image 
image = cv2.imread('test4.jpg')
scale = 20
width = int(image.shape[1] * scale/ 100)
height = int(image.shape[0] * scale/ 100)
dim = (width, height)
image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
img = image.copy()
#img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)   

while(1):
 
    
    #cv2.cvtColor(img, cv2.RGB2BGR)
	
	#returns current position/value of trackbar 
    l_r= int(cv2.getTrackbarPos('l_r','controls'))
    l_g=int(cv2.getTrackbarPos('l_g','controls'))
    l_b=int(cv2.getTrackbarPos('l_b','controls'))
    h_r= int(cv2.getTrackbarPos('h_r','controls'))
    h_g=int(cv2.getTrackbarPos('h_g','controls'))
    h_b=int(cv2.getTrackbarPos('h_b','controls'))    

    lowerRange = np.array([l_r, l_g, l_b])
    upperRange = np.array([h_r, h_g, h_b])        
	
    thresh = cv2.inRange(img, lowerRange, upperRange)

    bitwise = cv2.bitwise_and(img, img, mask=thresh)

    #assign trackbar value to r,g,b channel of the image
    #img[:,:,0]=b
    #img[:,:,1]=g
    #img[:,:,2]=r

    cv2.imshow('img.jpg',img)
    cv2.imshow('bitwise.jpg', bitwise)
    cv2.imshow('thresh.jpg', thresh)
	
    cv2.imwrite("bitwise.jpg", bitwise)
    cv2.imwrite("thresh.jpg", thresh)
    #waitfor the user to press escape and break the while loop 
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
#destroys all window
cv2.destroyAllWindows()