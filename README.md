# Color Conversion
## AIM
To perform the color conversion between RGB, BGR, HSV, and YCbCr color models.

## Software Required:
Anaconda - Python 3.7
## Algorithm:
### Step1:
Import cv2 library and upload the image or capture an image.
<br>
### Step2:
Read the saved image using cv2.imread("filename.jpg").
<br>
### Step3:
Convert the image into the given color transformation using cv2.cvtColor(image, cv2.BGR2YCrCb) 
and similarly for other color formats. 
<br>
### Step4:
Split and merge the image using cv2.split(hsv) and cv2.merge([h,s,v]) 
<br>
### Step5:
Output the image using cv2.imshow("OUTPUT", image)
<br>

## Program:
### Developed By: LOKESH KRISHNAA M
### Register Number: 212220230030
# i) Convert BGR and RGB to HSV and GRAY
```python
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
```
# ii)Convert HSV to RGB and BGR
```python
#(ii)Convert HSV to RGB and BGR
img = cv2.imread("apple logo.jpg")
#resizing the image to required size 
img1= cv2.resize(img, (270,190))
#converting  bgr to hsv so it can be converted into rgb and bgr
hsv = cv2.cvtColor(img1 , cv2.COLOR_BGR2HSV)
cv2.imshow("INITIAL_HSV ", hsv)
#HSV TO RGB FORMAT
hsv_rgb = cv2.cvtColor(hsv, cv2.COLOR_HSV2RGB)
cv2.imshow("HSV2RGB", hsv_rgb)
#HSV TO BGR FORMAT
hsv_bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow("HSV_BGR", hsv_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
# iii)Convert RGB and BGR to YCrCb
```python 
# (iii)convert RGB and BGR to YCrCb
import cv2
img = cv2.imread("apple logo.jpg")
img1= cv2.resize(img, (270,190))
cv2.imshow("BGR_COLOR ", img1)
#bgr to ycrcb
img_ycrcb = cv2.cvtColor(img1 , cv2.COLOR_BGR2YCrCb)
cv2.imshow("BGR_YCRCB ", img_ycrcb)
#converting  rgb to bgr so it can be converted into YCrCb
img_bgr = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
cv2.imshow("RGB COLOR", img_bgr)
#rgb 2 ycrcb
img_bgr_y = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2YCrCb)
cv2.imshow("RGB2YCrCb", img_bgr_y)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
# iv)Split and Merge RGB Image
```python 
# (iv) Split and Merge RGB Image
img = cv2.imread("apple logo.jpg")
#resizing the image to required size 
img1= cv2.resize(img, (270,190))
b,g,r = cv2.split(img1)
cv2.imshow("RED MODEL", r)
cv2.imshow("GREEN MODEL", g)
cv2.imshow("BLUE MODEL ", b)
#Merge:
merger = cv2.merge([b,g,r])
cv2.imshow("MERGED IMAGE", merger )
cv2.waitKey(0)
cv2.destroyAllWindows()
```
# v) Split and merge HSV Image
```python 
# (v)Split and merge HSV Image
img = cv2.imread("apple logo.jpg")
#resizing the image to required size 
img1= cv2.resize(img, (270,190))
#converting  bgr to hsv so it can be converted into rgb and bgr
hsv = cv2.cvtColor(img1 , cv2.COLOR_BGR2HSV)
cv2.imshow("INITIAL_HSV ", hsv)
h,s,v = cv2.split(hsv)
cv2.imshow("RED MODEL", h)
cv2.imshow("GREEN MODEL", s)
cv2.imshow("BLUE MODEL ", v)
#Merge:
merger = cv2.merge([h,s,v])
cv2.imshow("MERGED IMAGE", merger )
cv2.waitKey(0)
cv2.destroyAllWindows()
```

## Output:
### i) BGR and RGB to HSV and GRAY
<img width ="50%" height ="60%" src ="https://user-images.githubusercontent.com/75234646/162552839-4997f75e-ddd1-48ae-85b4-f8257c181623.png">

### ii) HSV to RGB and BGR
<img width="50%" height ="60%" src="https://user-images.githubusercontent.com/75234646/162553053-8a7f605e-e3f1-4331-a444-b3735a261c6d.png">

### iii) RGB and BGR to YCrCb
<img src ="https://user-images.githubusercontent.com/75234646/162552639-dffc8cde-a2f3-4d4c-b2d2-4f6790e70240.png" height ="60%" width="50%">

### iv) Split and merge RGB Image
<img height="60%" width="50%" src="https://user-images.githubusercontent.com/75234646/162553205-4e0ab820-0171-49cb-985e-88fcdf2e95ae.png">

### v) Split and merge HSV Image
<img width ="50%" height="60%" src="https://user-images.githubusercontent.com/75234646/162552806-ce5f4bad-82ba-49d4-9205-144663d5b14b.png">

## Result:
Thus the color conversion was performed between RGB, HSV and YCbCr color models.
