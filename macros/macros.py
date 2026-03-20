import config as cfg

import events.keyboard_events as kb
import events.mouse_events as ms
from state import state

import time

kbe = kb.Events()
mse = ms.Events()

def macros():
    is_autoclick_key = cfg.AUTOCLICK_KEY if bool(cfg.AUTOCLICK_KEY) else False
    is_autofill_key = cfg.AUTOFILL_KEY if bool(cfg.AUTOFILL_KEY) else False

    curent_state_back = mse.is_pressed("back") or kbe.is_pressed(is_autofill_key)
	
    if curent_state_back and not state.prev_state_back:
        kbe.click("E")
        time.sleep(1 / cfg.clicks_per_second)
        kbe.key_down("SHIFT_L")
	
    if not curent_state_back and state.prev_state_back:
        kbe.key_up("SHIFT_L")
        time.sleep(1 / cfg.clicks_per_second)
        kbe.click("E")
		
    state.prev_state_back = curent_state_back

    if mse.is_pressed("forward") or kbe.is_pressed(is_autoclick_key):
        mse.click("left")
        time.sleep(1 / cfg.clicks_per_second)
    elif mse.is_pressed("back") or kbe.is_pressed(is_autofill_key):
        mse.click("left")
        time.sleep(1 / cfg.clicks_per_second)
    else:
        time.sleep(0.01)