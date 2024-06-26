import cv2
import numpy as np

img=cv2.imread("image.jpg")
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel=np.array([
    [0,-1,0],
    [-1,5,-1],
    [0,-1,0]
])

#The kernel variable defines a 3x3 matrix used for sharpening. The central value (5) emphasizes the center pixel, while the negative values around it subtract from the neighboring pixels. This enhances the edges and creates a sharper appearance.

sharpened_img=cv2.filter2D(gray,-1,kernel)
#The cv2.filter2D function applies the sharpening kernel as a convolution filter. The -1 as the second argument indicates using the same data type for the output image.

cv2.imshow("Grayscale img",gray)
cv2.imshow("Sharpened img",sharpened_img)

cv2.waitKey(0)
cv2.destroyAllWindows()