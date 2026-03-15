import config as cfg

import events.keyboard_events as kb
import events.mouse_events as ms
from state import state

import time

kbe = kb.Events()
mse = ms.Events()

def macros():
    curent_state_back = mse.is_pressed("back")
	
    if curent_state_back and not state.prev_state_back:
        kbe.click("E")
        time.sleep(cfg.clicks_per_second)
        kbe.key_down("SHIFT")
	
    if not curent_state_back and state.prev_state_back:
        kbe.key_up("SHIFT")
        time.sleep(cfg.clicks_per_second)
        kbe.click("E")
		
    state.prev_state_back = curent_state_back

    if mse.is_pressed("forward"):
        mse.click("left")
        time.sleep(cfg.clicks_per_second)
    elif mse.is_pressed("back"):
        mse.click("left")
        time.sleep(cfg.clicks_per_second)
    else:
        time.sleep(0.01)