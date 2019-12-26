import cv2
cap = cv2.VideoCapture(0)
#img = cv2.imread("a.jpg")
n=0
x=1
y=1
size =40
l_scale = int(size/1.73)
x2 = x+l_scale
y2 = y + size
x3 = x2-l_scale
y3 = y2 + size
while True:
    x = x+1; x2 = x2+1; x3 = x3+1
    y = y+1; y2 = y2+1; y3 = y3+1

    ret, img = cap.read()
    #cv2.rectangle(img,(x,y),(x+200,y+150),(0,255,0),3)
    cv2.line(img,(x,y),(x+l_scale,y+size),(255,0,0),2)
    cv2.line(img,(x2,y2),(x2-l_scale,y2+size),(255,0,0),2)
    cv2.line(img,(x3,y3),(x3-size,y3),(255,0,0),2)
    cv2.imshow('image', img)
    cv2.waitKey(10)
    n=n+1
cv2.destroyAllWindows()
