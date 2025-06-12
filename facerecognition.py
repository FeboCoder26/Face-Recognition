import cv2
import time

face_capture = cv2.CascadeClassifier(
    "C:/Users/ashra/PycharmProjects/PythonProject1/.venv/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
while True:
    ret, video = video_capture.read()
    out.write(video)
    if not ret:
        break
    color = cv2.cvtColor(video, cv2.COLOR_BGR2GRAY)
    faces = face_capture.detectMultiScale(color, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                          flags=cv2.CASCADE_SCALE_IMAGE)
    if len(faces) > 0:
        cv2.imwrite("detected_face.jpg", video)
        cv2.putText(video, f'Faces:{len(faces)}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    for (x, y, w, h) in faces:
        cv2.rectangle(video, (x, y), (x + w, y + h), (0, 255, 0), 2)
        out.release()

    cv2.imshow('im LIVE', video)
    key = cv2.waitKey(1) & 0xFF
    if key != ord('s'):
        continue
    filename = f"screenshot_{int(time.time())}.jpg"
    if cv2.imwrite(filename, video):
        print(f"screenshot saved:{filename}")
    else:
        print("no screenshot saved")

if key == ord('a'):
     running = False

video_capture.release()
cv2.destroyAllWindows()
