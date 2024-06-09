import sys
import cv2 as cv

s = 0
if len(sys.argv) > 1:
    s = sys.argv[1]

win_name = "Camera Preview"
cv.namedWindow(win_name, cv.WINDOW_GUI_NORMAL)

source = cv.VideoCapture(s)

#models
net = cv.dnn.readNetFromCaffe(prototxt="models/deploy.prototxt",
                              caffeModel="models/res10_300x300_ssd_iter_140000.caffemodel")

eye_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_eye.xml')

#NN model parameters
img_width = 300
img_height = 300
mean = [104, 117, 123]
conf_threshold = 0.2

while cv.waitKey(1) != 27:
    has_frame, frame = source.read()
    if not has_frame:
        break
    
    frame = cv.flip(frame, 1)
    frame_width = frame.shape[1]
    frame_height = frame.shape[0]

    blob = cv.dnn.blobFromImage(frame, 0.5, (img_width, img_height), mean, swapRB=False, crop=False)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    net.setInput(blob)
    detections = net.forward()
    
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x_bottom_left = int(detections[0, 0, i, 3] * frame_width)
            y_bottom_left = int(detections[0, 0, i, 4] * frame_height)
            x_top_right = int(detections[0, 0, i, 5] * frame_width)
            y_top_right = int(detections[0, 0, i, 6] * frame_height)

            cv.rectangle(frame, (x_bottom_left, y_bottom_left), (x_top_right, y_top_right), (255, 0, 0))
            # cv.circle(frame, (x_bottom_left, x_bottom_left), 5, cv.LINE_AA)

            roi_gray = gray[y_bottom_left:y_bottom_left + y_top_right, x_bottom_left:x_bottom_left + x_top_right]
            roi_frame = frame[y_bottom_left:y_bottom_left + y_top_right, x_bottom_left:x_bottom_left + x_top_right]
            eyes = eye_cascade.detectMultiScale(roi_gray)
            for x, y, w, h in eyes:
                cv.rectangle(roi_frame, (x, y), (x+w, y+h), (0, 0, 255))

            label = "Confidence: %.4f" % confidence
            label_size, baseline = cv.getTextSize(label, cv.FONT_HERSHEY_SIMPLEX, .5, 2)
            cv.rectangle(frame, (x_bottom_left, y_bottom_left - label_size[1]),
                         (x_bottom_left + label_size[0], y_bottom_left + baseline), (255, 255, 255), cv.FILLED)

            cv.putText(frame, label, (x_bottom_left, y_bottom_left),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))
    
    t, _ = net.getPerfProfile()
    label = "Inference Time: %.2f ms" % (t * 1000 / cv.getTickFrequency())
    cv.putText(frame, label, (0, 15), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0))

    cv.imshow(winname=win_name, mat=frame)

source.release()
cv.destroyAllWindows()
