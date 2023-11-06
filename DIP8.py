#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import cv2
image = cv2.imread("carss.jpg",0)
img = cv2.GaussianBlur(image,(3,3),0)
plt.axis('off')
plt.imshow(img)
plt.show()


# In[2]:


edge = cv2.Canny(img,50,100)
plt.imshow(edge,cmap='gray')
plt.title('Edged Image after applying Canny Edge Detector')
plt.xticks([])
plt.yticks([])
plt.show()


# In[3]:


lines=cv2.HoughLinesP(edge,1,np.pi/180, threshold=80, minLineLength=50,maxLineGap=250)


# In[4]:


for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(edge,(x1,y1),(x2,y2),(250,0,0),3)


# In[5]:


plt.imshow(edge)
plt.axis('off')
plt.show()


# In[ ]:




