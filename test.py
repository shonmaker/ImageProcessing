import cv2

color = cv2.imread('road.jpg')
gray = cv2.imread('road.jpg', cv2.IMREAD_GRAYSCALE)

if color is None or gray is None:
    # if image doesn't exist than add process   
    raise FileNotFoundError('road.jpg')

print(color.shape, gray.dtype)
cv2.imshow('COLOR',color)
cv2.imshow('GRAY',gray)
cv2.waitKey(0)
cv2.destroyAllWindows()