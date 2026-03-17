import cv2
import numpy as np

hud = cv2.imread("minecraft/fiting_CV2_Bot/images/hud.png")

def mouse_callback(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        hud = param

        pixel = hud[y, x]  # BGR
        b, g, r = pixel

        print(f"x={x}, y={y}")
        print(f"BGR: {b}, {g}, {r}")

y, x, a = hud.shape
hud_croped = hud[int(y*0.5): y, : ]

cv2.imshow("hud", hud_croped)
cv2.setMouseCallback("hud", mouse_callback, hud_croped)
cv2.waitKey(0)

hsv = cv2.cvtColor(hud_croped, cv2.COLOR_BGR2HSV)

print(hsv.shape)

cv2.imshow("hud", hsv)
cv2.setMouseCallback("hud", mouse_callback, hsv)
cv2.waitKey(0)

lower = np.array([5, 100, 140])
upper = np.array([15, 120, 210])

mask = cv2.inRange(hsv, lower, upper)

cv2.imshow("hud", mask)
cv2.waitKey(0)


kernel = np.ones((3,3),np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

hearts = 0
for cnt in contours:
    x,y,w,h = cv2.boundingRect(cnt)

    cv2.rectangle(hud, (x, y), (x + w, y + h), (0, 255, 0), 2)
    hearts += 1

print(len(contours))
cv2.imshow("hud", hud)
cv2.setMouseCallback("hud", mouse_callback, hud)
cv2.waitKey(0)
