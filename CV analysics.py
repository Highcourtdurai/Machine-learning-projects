import numpy as np
import matplotlib.pyplot as plt
import cv2

data=cv2.imread("opencv.png")

cv2.imshow("image",data)
cv2.waitKey(0)
cv2.destroyAllWindows()