import sys
import cv2 as cv
import numpy as np

PREVIEW     = 0 # Preview Mode.
BLUR        = 1 # Blurring filter.
GRAY        = 2
FEATURES    = 3 # Corner Feature Detector.
CANNY       = 4 # Canny Edge Detector. 

feature_params = dict(maxCorners=500,
                      qualityLevel=0.2,
                      minDistance=15,
                      blockSize=9)

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

image_filter = PREVIEW
alive = True

win_name  = "Camera filters"
cv.namedWindow(win_name, cv.WINDOW_NORMAL)
result = None

source = cv.VideoCapture(s)

while alive:
    has_frame, frame = source.read()
    if not has_frame:
        break

    frame = cv.flip(frame, 1)

    if image_filter == PREVIEW:
        result = frame
    elif image_filter == CANNY:
        result = cv.Canny(frame, threshold1=50, threshold2=150)
    elif image_filter == BLUR:
        result = cv.blur(frame, (13, 13))
    elif image_filter == GRAY:
        result = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        ret, frame = cv.threshold(result, 5, 255, cv.THRESH_BINARY)
        result = frame
    elif image_filter == FEATURES:
        result = frame
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        corners = cv.goodFeaturesToTrack(frame_gray, **feature_params)
        if corners is not None:
            for x, y in np.float32(corners).reshape(-1, 2):
                cv.circle(result, (int(x), int(y)), 10, (0, 255, 0), 1)
            
            # for corner in corners:
            #     x, y = corner.ravel()
            #     cv.circle(result, (x,y), 10, (0, 255, 0), 1)
                

    cv.imshow(win_name, result)

    key = cv.waitKey(1)
    if key == ord('Q') or key == ord('q') or key == 27:
        alive = False
    elif key == ord('B') or key == ord('b'):
        image_filter = BLUR
    elif key == ord('C') or key == ord('c'):
        image_filter = CANNY
    elif key == ord('F') or key == ord('f'):
        image_filter = FEATURES
    elif key == ord('G') or key == ord('g'):
        image_filter = GRAY
    elif key == ord('P') or key == ord('p'):
        image_filter = PREVIEW
    
source.release()
cv.destroyWindow(win_name)
