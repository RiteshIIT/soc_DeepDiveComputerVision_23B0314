import cv2

img=cv2.imread("image.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
equalized_img=cv2.equalizeHist(gray)

cv2.imshow("Grayscale image",gray)
cv2.imshow("Equalized image",equalized_img)

cv2.waitKey(0)
cv2.destroyAllWindows()