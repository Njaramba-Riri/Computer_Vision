import cv2 as cv
import sys

img = cv.imread(cv.samples.findFile("/home/riri/Desktop/Computer_Vision/Images/cat.jpeg"))

if img is None:
    sys.exit("Could not find image file.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("starry_cat.jpg", img)
