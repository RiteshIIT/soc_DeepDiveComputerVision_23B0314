import cv2

img=cv2.imread("image.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edges=cv2.Canny(gray,75,150) #adjust thresholds as needed

cv2.imshow("Grayscale image",gray)
cv2.imshow("Edges",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()