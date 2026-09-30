from pathlib import Path
from unittest import result
import cv2


SOURCE = str('road.mp4')
cap = cv2.VideoCapture(SOURCE)
if not cap.isOpened():
    raise RuntimeError('Camera/video open failed')


target = Path('output/photo.png')
target.parent.mkdir(exist_ok=True)
delay = 1 if isinstance(SOURCE, int) else 42
while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (640, 360))
    threshold_value = gray.mean()
    
    eq = cv2.equalizeHist(gray)
    sub_eq = cv2.subtract(eq, 80)

    cv2.imshow('CAPTURE', gray)
    cv2.imshow('EQ', eq)
    cv2.imshow('SUB_EQ', sub_eq)

    key = cv2.waitKey(delay) & 0xFF
    
    if key == ord('s'):
        print('saved:', cv2.imwrite(str(target), gray))
    if key == ord('r'):
        print('saved:', cv2.imwrite(str(target), result))
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
