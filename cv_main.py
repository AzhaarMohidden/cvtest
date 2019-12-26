import cv2
from drwhx import cv_draw_hex
cap = cv2.VideoCapture(0)
while True:
    ret, img = cap.read()
    cv_draw_hex.drawHex(150,150, 70, 1,  img)
    cv2.imshow('image', img)
    cv2.waitKey(10)
cv2.destroyAllWindows()
