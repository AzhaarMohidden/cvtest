import cv2
def drawHex(x, y, size, img):
        #scale dependes on the angle of slant of the line and is the inverse tangent of the angle
        l_scale = int(size/1.73)
        size_s = size - (size/2)
        ls_scale = int(size_s/1.73)
        #initaiate position of each line starting point => x, y
        x2 = x + l_scale; x3 = x2 - l_scale; x4 = x3 - size; x5 = x4 - l_scale; x6 = x
        y2 = y + size; y3 = y2 + size; y4 = y3; y5 = y4 - size; y6 = y
# draw line
# Hexagon
        cv2.line(img,(x,y),(x+l_scale,y+size),(255,0,0),2)
        cv2.line(img,(x2,y2),(x2-l_scale,y2+size),(255,0,0),2)
        cv2.line(img,(x3,y3),(x3-size,y3),(255,0,0),2)
        cv2.line(img,(x4,y4),(x4-l_scale,y4-size),(255,0,0),2)
        cv2.line(img,(x5,y5),(x5+l_scale,y5-size),(255,0,0),2)
        cv2.line(img,(x6,y6),(x6-size,y6),(255,0,0),2)
#Name line
        cv2.line(img,(x,y),(x+ls_scale,y-size + size_s),(255,0,0),2)
        cv2.line(img,(x+ls_scale,y-size + size_s),(x+size*2,y-size + size_s),(255,0,0),2)
