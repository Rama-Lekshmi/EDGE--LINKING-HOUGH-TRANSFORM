# Edge-Linking-using-Hough-Transform...

## Aim:

To write a Python program to detect the lines using Hough Transform.

## Software Required:

Anaconda - Python 3.7 .

## Algorithm:

### Step 1:

Import all the necessary packages required for the program.

### Step 2:

Load a image using imread() from cv2 module.

### Step 3:

Convert the image to grayscale image.

### Step 4:

Using Canny edge operator from cv2, detect the edges of the image.

### Step 5:

Using the HoughLinesP(), detect the line co-ordinates for every points in the images. Using For loop, draw the lines on the found co-ordinates.

### Step 6:

Display the image found by the HoughLinesP() and end the program.

## Program:

```python
## Developer name:Rama E. K. Lekshmi
## Register no:212222240082

# Read image and convert it to grayscale image:

import numpy as np
import matplotlib.pyplot as plt
import cv2
image = cv2.imread("carss.jpg",0)
img = cv2.GaussianBlur(image,(3,3),0)
plt.axis('off')
plt.imshow(img)
plt.show()

```

```python

# Find the edges in the image using canny detector and display:

edge = cv2.Canny(img,50,100)
plt.imshow(edge,cmap='gray')
plt.title('Edged Image after applying Canny Edge Detector')
plt.xticks([])
plt.yticks([])
plt.show()

```

```python

# Detect points that form a line using HoughLinesP:

lines=cv2.HoughLinesP(edge,1,np.pi/180, threshold=80, minLineLength=50,maxLineGap=250)

```

```python

# Draw lines on the image:

for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(edge,(x1,y1),(x2,y2),(250,0,0),3)
    
```

```python

# Display the result:

plt.imshow(edge)
plt.axis('off')
plt.show()

```

## Output:

### Input image:

![carss](https://github.com/Javith-farkhan/Edge-Linking-using-Hough-Transform/assets/94296805/2b94c576-c222-4d00-9132-114324fadcff)


### Grayscale image:

![Di8 1](https://github.com/Javith-farkhan/Edge-Linking-using-Hough-Transform/assets/94296805/fda7fd66-bb36-4cc3-be05-bc4705e2491e)


### Canny Edge detector output:

![Di8 2](https://github.com/Javith-farkhan/Edge-Linking-using-Hough-Transform/assets/94296805/b27508b8-db47-4784-bed1-466f4e11fc71)


### Display the result of Hough transform:

![Di8 3](https://github.com/Javith-farkhan/Edge-Linking-using-Hough-Transform/assets/94296805/0d3cc618-947d-4da0-a7cd-f9d4e044e879)


## Result:

Thus the program is written with python and OpenCV to detect lines using Hough transform.

