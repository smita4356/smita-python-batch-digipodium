import cv2
#loading image
img=cv2.imread('rose1.jpg')
print(img)
cv2.imshow('using cv2',img)
cv2.waitKey(5000)