import time
import threading

import vision.screen
import analizer.screen_analize as scr_anal
import controller.control as contr
import macros.macros as mac
import control_panel.ctrl_panel as ct_pan
import config as cfg


def vision_task():
	while True:
		if vision.screen.capture():
			scr_anal.analize_screen()
		time.sleep(0.025)

vision_task__ = threading.Thread(target=vision_task, daemon=True)
vision_task__.start()
print("[BOOT] Vision system activate")

def controller_task():
	while True:
		if cfg.AUTO_HEAL:
			contr.controler()
		time.sleep(0.025)
controller_task__ = threading.Thread(target=controller_task, daemon=True)
controller_task__.start()
print("[BOOT] Controller system activate")

def macros_task():
	while True:
		if cfg.AUTO_CLICK:
			mac.macros()
		time.sleep(0.05)
macros_task__ = threading.Thread(target=macros_task, daemon=True)
macros_task__.start()
print("[BOOT] Macros system activate")

print("\n[BOOT] Bot ready to use\n")

threading.Thread(target=ct_pan.panel_task, daemon=True).start()
threading.Thread(target=ct_pan.keyboard_task, daemon=True).start()

while cfg.RUNNING:
	time.sleep(0.001)