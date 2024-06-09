import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
# To capture video from webcam. 
#cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture('Shadrack.png')

win_name = "Camera Preview"
cv2.namedWindow(win_name, cv2.WINDOW_GUI_NORMAL)

# To use a video file as input 
cap = cv2.VideoCapture(0)



while True:
    # Read the frame
    ret, img = cap.read()
    if not ret:
        break

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h),(255, 0, 0))
        
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for ex, ey, ew, eh in eyes:
            cv2.rectangle(roi_color,(ex, ey), (ex+ew, ey+eh), (0, 255, 0))

    k = cv2.waitKey(1) & 0xff
    if k ==27:
        break
    
    cv2.imshow(win_name, img)

cap.release()
cv2.destroyAllWindows()
