import cv2 as cv
import matplotlib.pyplot as plt

vid_cap = cv.VideoCapture(0)

# if(vid_cap.isOpened() == False):
#     print("Could not access the camera.")

while True:
    ret, frame = vid_cap.read()

    frame_width = int(vid_cap.get(3))
    frame_height = int(vid_cap.get(4))
    fps = int(vid_cap.get(cv.CAP_PROP_FPS))

    out_avi = cv.VideoWriter("10th_feb.avi", cv.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps, (frame_width, frame_height))
    out_mp4 = cv.VideoWriter("10th_feb.mp4", cv.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))  
    
    if ret == True:
        cv.imshow("It's you mofo", frame)
        
        
        out_avi.write(frame)
        out_mp4.write(frame)

        key = cv.waitKey(8)

        if key == ord('q'):
            break
    else:
        break
    
    # out_avi.release()
    # out_mp4.release()

vid_cap.release()
cv.destroyAllWindows()
