import cv2

img=cv2.imread("image.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur for noise reduction 
blurred_img = cv2.GaussianBlur(gray, (5, 5), 0)  

thresh=127
# cv2.THRESH_BINARY: Pixels above thresh become 255 (white), below become 0 (black)

ret,threshold_img=cv2.threshold(blurred_img,thresh,255,cv2.THRESH_BINARY)

cv2.imshow("Grayscale image ", gray)
cv2.imshow("Thresholded image",threshold_img)

cv2.waitKey(0)
cv2.destroyAllWindows()