import cv2 as cv


vid_capture = cv.VideoCapture('../data/videos/Cars.mp4')

if (vid_capture.isOpened() == False):
    print("Error reading the video file.")
else:
    #Get the frame rate
    fps = vid_capture.get(5)
    print("Frames per Second: ", fps, 'FPS')

    #Get frame count.
    frame_count = vid_capture.get(7)
    print("Frame count: ", frame_count)

while(vid_capture.isOpened()):
    ret, frame = vid_capture.read() #Returns a tuple, first element is a bool, second one is a frame.
    if ret  == True:
        cv.imshow('Frame', frame)
        cv.putText(frame, text=f"Frames per second: {fps}", org=(7, 240), 
                   fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=3, color=(0, 255, 0))

        key = cv.waitKey(20)
        
        if key == ord('q'):
            break
    else:
        break

#Release video and capture object.
vid_capture.release()
cv.destroyAllWindows()
