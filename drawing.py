
import cv2
import numpy as np
#img=cv2.imread("lena.jpg",-1)
img=np.zeros([512,512,3],np.uint8)

img=cv2.line(img, (0,0), (255,255), (0,255,0), thickness=3)
img=cv2.arrowedLine(img, (0,255), (255,255), (0,255,0), thickness=3)

img=cv2.rectangle(img,(100,100),(360,255),(0,0,255),-1)

img=cv2.circle(img,(360,280),63,(155,155,155),-1)


font=cv2.FONT_HERSHEY_SIMPLEX
img=cv2.putText(img,"OpenCV",(10,500),font,4,(255,255,255),10,cv2.LINE_AA )







cv2.imshow("lena",img)
k = cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.destroyAllWindows()