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

    result = frame.copy()
    result = cv2.line(result, (30,60), (220,60), (255,0,0), 3)
    result = cv2.rectangle(result, (10,10), (1270,710), (0,255,0), 3)
    result = cv2.circle(result, (640,360), 360, (0,0,255), 3)

    result = cv2.putText(result, 'MY SCENE', (30,40),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                        (255,255,255), 2, cv2.LINE_AA)
    
    cv2.imshow('CAPTURE', result)

    key = cv2.waitKey(delay) & 0xFF

    if key == ord('s'):
        print('saved:', cv2.imwrite(str(target), frame))

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()