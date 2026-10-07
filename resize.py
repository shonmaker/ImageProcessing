import cv2 

path = cv2.imread('test.png')

cv2.imshow('Path',path)
print(path.shape)

a = cv2.resize(path, (320, 180))
b = cv2.resize(path, None, fx  = 0.5, fy = 0.5)

print(a.shape, b.shape)

cv2.imshow('A',a)
cv2.imshow('B',b)

small = path[140:185, 300:345]

for flag in [cv2.INTER_NEAREST, cv2.INTER_LINEAR,
             cv2.INTER_CUBIC,   cv2.INTER_AREA]:
    up = cv2.resize(small, (640, 360), interpolation = flag)
    cv2.imshow(f'flag = {flag}', up)

cv2.waitKey(0)
cv2.destroyAllWindows()