import time
import config as conf

import events.keyboard_events as kb
import events.mouse_events as ms
from state import state

cfg = conf.config

kbe = kb.Events()
mse = ms.Events()

last_click_time = 0


def run_kitpvp():
    global last_click_time

    is_autoclick_key = cfg.AUTOCLICK_KEY or False
    is_autofill_key = cfg.AUTOFILL_KEY or False

    curent_state_back = mse.is_pressed("back") or kbe.is_pressed(is_autofill_key)

    # ===== HEAL LOGIC =====
    if curent_state_back and not state.prev_state_back:
        kbe.click("E")
        time.sleep(1 / cfg.KIT_CPS)
        kbe.key_down("SHIFT_L")

    if not curent_state_back and state.prev_state_back:
        kbe.key_up("SHIFT_L")
        time.sleep(1 / cfg.KIT_CPS)
        kbe.click("E")

    state.prev_state_back = curent_state_back

    # ===== CLICK =====
    now = time.perf_counter()
    delay = 1 / cfg.KIT_CPS

    if now - last_click_time >= delay:
        if mse.is_pressed("forward") or kbe.is_pressed(is_autoclick_key):
            mse.click("left")

        elif mse.is_pressed("back") or kbe.is_pressed(is_autofill_key):
            mse.click("left")

        else:
            time.sleep(0.01)

        last_click_time = now