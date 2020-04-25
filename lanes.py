import cv2
import numpy as np

def canny(image):
    lane_image=np.copy(image)
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray,(5,5),0)
    canny = cv2.Canny(blur,50,150)
    return canny

image = cv2.imread("test_image.jpg")

canny=canny(image)
cv2.imshow('result',canny)
cv2.waitKey(0)
