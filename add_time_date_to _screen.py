import cv2
import datetime

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')  # or *'XVID'
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(3, 1280)
cap.set(4, 680)
print(cap.get(3))
print(cap.get(4))

while cap.isOpened():
    ret, frame = cap.read()
    if ret == True:

        font = cv2.FONT_HERSHEY_SIMPLEX

        text = "WIDTH:" + str(cap.get(3)) + "HEIGHT:" + str(cap.get(4))

        datet = str(datetime.datetime.now())

        frame = cv2.putText(frame, datet, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, text, (360, 495), font, 1, (0, 255, 255), 2, cv2.LINE_AA)

        out.write(frame)

        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()

out.release()

cv2.destroyAllWindows()
