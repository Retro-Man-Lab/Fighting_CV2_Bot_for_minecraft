import time
import config as conf

import events.keyboard_events as kb
import events.mouse_events as ms

cfg = conf.config

kbe = kb.Events()
mse = ms.Events()

last_click_time = 0

prev_forward = False
prev_back = False


def run_bedwars():
    global last_click_time, prev_forward, prev_back

    is_pvp_key = cfg.BW_PVP_KEY or False
    is_bridge_key = cfg.BW_BRIDGE_KEY or False

    forward = mse.is_pressed("forward") or kbe.is_pressed(is_pvp_key)
    back = mse.is_pressed("back") or kbe.is_pressed(is_bridge_key)

    if cfg.BW_PVP_ENABLED:
        if forward and not prev_forward:
            kbe.click(str(cfg.BW_PVP_SLOT))

    if cfg.BW_BRIDGE_ENABLED:
        if back and not prev_back:
            kbe.click(str(cfg.BW_BRIDGE_SLOT))

    prev_forward = forward
    prev_back = back

    now = time.perf_counter()
    
    delay = 1 / cfg.BW_PVP_CPS

    if now - last_click_time >= delay:

        if cfg.BW_PVP_ENABLED and forward:
            mse.click("left")

        elif cfg.BW_BRIDGE_ENABLED and back:
            mse.click("right")

        else:
            time.sleep(0.01)

        last_click_time = now