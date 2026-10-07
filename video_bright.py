from pathlib import Path
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

    frame = cv2.resize(frame, (640,360))

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    dark = cv2.subtract(gray, 60)
    bright = cv2.add(gray, 60)

    cv2.imshow('CAPTURE', gray)
    cv2.imshow('dark', dark)
    cv2.imshow('bright', bright)
    

    key = cv2.waitKey(delay) & 0xFF

    
    small = gray[140:185, 300:345]

    for flag in [cv2.INTER_NEAREST, cv2.INTER_LINEAR,
             cv2.INTER_CUBIC,   cv2.INTER_AREA]:
        up = cv2.resize(small, (640, 360), interpolation = flag)
        cv2.imshow(f'flag = {flag}', up)

    if key == ord('s'):
        print('saved:', cv2.imwrite(str(target), gray))

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()