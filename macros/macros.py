import config as conf

import events.keyboard_events as kb
import events.mouse_events as ms
from state import state

import time

cfg = conf.config

kbe = kb.Events()
mse = ms.Events()

last_click_time = 0
last_click_shift_time = 0
shift = False

def macros():
    global last_click_time, last_click_shift_time, shift
    # ======================
    # FORVARD IN OUT
    # ======================

    is_autoclick_key = cfg.AUTOCLICK_KEY if bool(cfg.AUTOCLICK_KEY) else False

    # ======================
    # BACK IN OUT
    # ======================

    is_autofill_key = cfg.AUTOFILL_KEY if bool(cfg.AUTOFILL_KEY) else False

    curent_state_back = mse.is_pressed("back") or kbe.is_pressed(is_autofill_key)

    if cfg.MODE == "kitpvp":
        if curent_state_back and not state.prev_state_back:
            kbe.click("E")
            time.sleep(1 / cfg.clicks_per_second)
            kbe.key_down("SHIFT_L")
        
        if not curent_state_back and state.prev_state_back:
            kbe.key_up("SHIFT_L")
            time.sleep(1 / cfg.clicks_per_second)
            kbe.click("E")
        
    state.prev_state_back = curent_state_back

    # ======================
    # TIMING CLICK
    # ======================

    now = time.perf_counter()
    delay = 1 / cfg.clicks_per_second

    if now - last_click_time >= delay:
        if cfg.MODE == "kitpvp":
            if mse.is_pressed("forward") or kbe.is_pressed(is_autoclick_key):
                mse.click("left")
            elif mse.is_pressed("back") or kbe.is_pressed(is_autofill_key):
                mse.click("left")
            else:
                time.sleep(0.01)

        elif cfg.MODE == "bedwars":
            if mse.is_pressed("forward") or kbe.is_pressed(is_autoclick_key):
                mse.click("left")
            elif mse.is_pressed("back") or kbe.is_pressed(is_autofill_key):
                mse.click("right")
            else:
                time.sleep(0.01)
        
        last_click_time = now