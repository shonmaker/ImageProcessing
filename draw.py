from pathlib import Path
import cv2


color = cv2.imread('output/photo.png')

if color is None:
    # if image doesn't exist than add process   
    raise FileNotFoundError('road.jpg')

result = color.copy()
result = cv2.line(result, (30,60), (220,60), (255,0,0), 3)
result = cv2.rectangle(result, (80,90), (300,250), (0,255,0), 3)
result = cv2.circle(result, (190,170), 30, (0,0,255), 3)

result = cv2.putText(result, 'MY SCENE', (30,40),
                     cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                     (255,255,255), 2, cv2.LINE_AA)



print(result.shape)
cv2.imshow('RESULT',result)
cv2.waitKey(0)
cv2.destroyAllWindows()