import cv2

img = cv2.imread("a.jpg")

cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
