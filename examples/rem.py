import sys
import cv2 as cv

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]
    

PREVIEW = 0
CANNY   = 1
GRAY    = 2
BLUR    = 3

img_filter = PREVIEW
result = None

win_name = "Camera Frame"
cv.namedWindow(win_name, cv.WINDOW_FULLSCREEN)
source  = cv.VideoCapture(s)

while True:
    has_frame, frame = source.read()
    
    if not has_frame:
        break
    
    frame = cv.flip(frame, 1)
    
    if img_filter == PREVIEW:
        result = frame
    elif img_filter == GRAY:
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # ret, frame = cv.threshold(frame, thresh=10, maxval=255, type=cv.THRESH_BINARY)
        result = frame
    elif img_filter == BLUR:
        result = cv.blur(frame, (20, 20))
    elif img_filter == CANNY:
        result = cv.Canny(frame, threshold1=10, threshold2=100)
    
    cv.imshow(win_name, result)
    
    key = cv.waitKey(1)
    if key == ord('D') or key ==  ord('d'):
        img_filter = PREVIEW
    if key == ord('G') or key == ord('g'):
        img_filter = GRAY
    elif key == ord('B') or key == ord('b'):
        img_filter = BLUR
    elif key == ord('C') or key == ord('c'):
        img_filter = CANNY
    elif key == 27 or key == ord('Q') or key == ord('q'):
        break
    
source.release()
cv.destroyWindow(win_name)
