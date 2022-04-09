# Color Conversion
## AIM
To perform the color conversion between RGB, BGR, HSV, and YCbCr color models.

## Software Required:
Anaconda - Python 3.7
## Algorithm:

### Step1:

<br>

### Step2:

<br>

### Step3:

<br>

### Step4:

<br>

### Step5:

<br>

## Program:


```python
# Developed By: LOKESH KRISHNAA
# Register Number: 212220230030
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

# (ii)Convert HSV to RGB and BGR

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

cv2

r,g,b = cv2.split(img1)

cv2.imshow("RED MODEL", r)
cv2.imshow("GREEN MODEL", g)
cv2.imshow("BLUE MODEL ", b)



#Merge:
merger = cv2.merge([r,g,b])
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
<br>
![Screenshot (26)](https://user-images.githubusercontent.com/75234646/162552626-ba7b1d5c-6b53-4429-8e26-a78f9d1f96e3.png)



<br>

### ii) HSV to RGB and BGR
<br>
![Screenshot (28)](https://user-images.githubusercontent.com/75234646/162552618-dce4d93d-a94b-45c5-bec0-3c32b0d99ada.png)



<br>

### iii) RGB and BGR to YCrCb
<br>

![Screenshot (31)](https://user-images.githubusercontent.com/75234646/162552639-dffc8cde-a2f3-4d4c-b2d2-4f6790e70240.png)


<br>

### iv) Split and merge RGB Image
<br>
![Screenshot (29)](https://user-images.githubusercontent.com/75234646/162552661-a5c53413-535a-491c-8e1e-2be50487557d.png)



<br>

### v) Split and merge HSV Image
<br>
![Screenshot (30)](https://user-images.githubusercontent.com/75234646/162552648-41268065-be8d-4b5c-991e-0a1e3883cf06.png)


<br>



## Result:
Thus the color conversion was performed between RGB, HSV and YCbCr color models.
