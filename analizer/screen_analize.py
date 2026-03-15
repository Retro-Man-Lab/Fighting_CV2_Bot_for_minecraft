from state import state

import time
import cv2
import numpy as np

def mouse_callback(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDOWN:

        img = param

        pixel = img[y, x]  # BGR
        b, g, r = pixel

        print(f"x={x}, y={y}")
        print(f"BGR: {b}, {g}, {r}")

def count_heards(hud):
    # hud = cv2.imread("minecraft/fiting_CV2_Bot/images/hud.png")
    hsv = cv2.cvtColor(hud, cv2.COLOR_BGR2HSV)

    lower_red1 = np.array([0,230,255])
    upper_red1 = np.array([0,240,255])

    mask = cv2.inRange(hsv, lower_red1, upper_red1)

    kernel = np.ones((3,3),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    hearts = 0
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)

        area = cv2.contourArea(cnt)
        ratio = w / h

        if 80 < area < 800 and 0.7 < ratio < 1.3 and x < hud.shape[1]*0.5:
            hearts += 1
    
    state.player['hp'] = hearts

def count_heale(hud):
    hsv = cv2.cvtColor(hud, cv2.COLOR_BGR2HSV)

    lower = np.array([5, 100, 140])
    upper = np.array([15, 120, 210])

    mask = cv2.inRange(hsv, lower, upper)

    contours,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    slot_width = hud.shape[1] / 9
    slot_area = slot_width ** 2

    heal_slots = []
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)

        area = cv2.contourArea(cnt)
        ratio = area / slot_area

        if 0.05 < ratio < 0.35:
            center_x = x + w/2
            slot = int(center_x / slot_width)

            heal_slots.append(slot + 1)

    state.player["heal"] = heal_slots

def analize_screen():
    if state.is_active_window_minecraft:
        img = state.img

        h, w = img.shape[:2]
        hud = img[int(h - w * 0.40 * 0.216):h, int(w*0.30):int(w*0.70)]

        count_heards(hud)
        count_heale(hud)
        # print(state.player)