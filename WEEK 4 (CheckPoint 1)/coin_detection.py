import cv2
import numpy as np

img=cv2.imread("image.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
kernel=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])
sharpened_img=cv2.filter2D(blur,-1,kernel)

thresh=cv2.adaptiveThreshold(sharpened_img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,11,2)


contours,_=cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

image_width=57.6 #cm
min_d=12
max_d=22

i=0
detected_coins=[]
for cnt in contours:
    i+=1
    print(i)
    (center,radius)=cv2.minEnclosingCircle(cnt)
    diameter_cm=2*radius*(1/(img.shape[1]/image_width))
    if min_d<=diameter_cm<=max_d:
        detected_coins.append((center,diameter_cm))
        cv2.circle(img,(int(center[0]),int(center[1])),int(radius),(0,255,0),2)

print(f"Total coins detected : {len(detected_coins)}")

for center, diameter_cm in detected_coins:
    print(f"Coin diameter :  {diameter_cm:.2f} cm")
    

cv2.imshow("thresh",thresh)
cv2.imshow("Detected coins", img)
cv2.waitKey(0)
cv2.destroyAllWindows()