from tracemalloc import take_snapshot
import cv2
import time
import random
starttime = time.time()
def multiplescreenshots():
    number = random.randint(1,50)
    
    videocaptureobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videocaptureobject.read()
        print("iminside")
        imgname = "img"+str(number)+".png"
        cv2.imwrite(imgname, frame)
        starttime = time.time()
        result = False
        print(imgname)
    videocaptureobject.release()
    cv2.destroyAllWindows()

    def main():
        while(True):
        
         multiplescreenshots()
    main()         