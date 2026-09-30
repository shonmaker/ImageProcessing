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
    _,binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
    tv,otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    cv2.imshow('CAPTURE', gray)
    cv2.imshow('BINARY', binary)
    cv2.imshow('OTSU', otsu)

    key = cv2.waitKey(delay) & 0xFF
    
    if key == ord('s'):
        print('saved:', cv2.imwrite(str(target), gray))
    if key == ord('r'):
        print('saved:', cv2.imwrite(str(target), result))
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
