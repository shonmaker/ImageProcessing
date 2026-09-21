from pathlib import Path
import cv2


img = cv2.imread('road.jpg')

if img is None:
    # if image doesn't exist than add process   
    raise FileNotFoundError('road.jpg')

print(img.shape, img.dtype)
cv2.imshow('IMG',img)
cv2.waitKey(0)
cv2.destroyAllWindows()