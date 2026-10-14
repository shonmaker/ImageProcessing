import sys, cv2, numpy as np
sys.path.insert(0, str(__import__("pathlib").Path(__file__).resolve().parent.parent))

import common as C

img = C.load("tl_day_red.png", True)
C.show("INRANGE", img)
cv2.waitKey(0)