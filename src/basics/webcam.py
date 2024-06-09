import cv2 as cv

video_captrue = cv.VideoCapture(0)

if (video_captrue.isOpened() == False):
    print("Couldn't access the webcam.")

while (video_captrue.isOpened()):
    ret, img = video_captrue.read()
    if ret == True:
        # img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        cv.imshow("WebCam Capture", img)

        key = cv.waitKey(20)

        if(key == 113) & 0xff:
            break
    else:
        break

video_captrue.release()
cv.destroyAllWindows()