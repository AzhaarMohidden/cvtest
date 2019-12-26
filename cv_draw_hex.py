def drawHex(x, y, p):
        size =40
        l_scale = int(size/1.73)
        x2 = x+l_scale
        y2 = y + size
        x3 = x2-l_scale
        y3 = y2 + size
        cv2.line(p,(x,y),(x+l_scale,y+size),(255,0,0),2)
        cv2.line(p,(x2,y2),(x2-l_scale,y2+size),(255,0,0),2)
        cv2.line(p,(x3,y3),(x3-size,y3),(255,0,0),2)
