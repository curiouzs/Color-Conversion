
# (i) bgr and rgb to hsv and gray

import cv2

img = cv2.imread('apple logo.jpg')

#resizing the image to required size 
img= cv2.resize(img, (270,190))
cv2.imshow('INITIAL IMAGE',img)

#converting bgr image 2 hsv and grey
hsv_bgr = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',hsv_bgr)


gray_bgr = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',gray_bgr)


#converting bgr to rgb format 
bgr_rgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
cv2.imshow('BGR 2 RGB',bgr_rgb)


#rgb to hsv and grey
rgb_hsv = cv2.cvtColor(bgr_rgb,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2GRAY',rgb_hsv)

rgb_grey = cv2.cvtColor(bgr_rgb,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB 2 GREY',rgb_grey)



cv2.waitKey(0)

cv2.destroyAllWindows()
