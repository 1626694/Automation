from pickle import TRUE
import cv2
def screenshot():
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videocaptureobject.read()
        cv2.imwrite("imagename.png",frame)
        result = False
    videocaptureobject.release()
    cv2.destroyAllWindows()

screenshot()