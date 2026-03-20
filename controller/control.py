import events.keyboard_events as kb
import events.mouse_events as ms
from state import state

import time

kbe = kb.Events()
mse = ms.Events()

def controler():
    if state.is_active_window_minecraft and bool(state.player["hp"]):
        if state.player["hp"] <= 5 and state.player["heal"]:
            kbe.click(str(state.player["heal"][0]))
            time.sleep(0.05)

            mse.click("right")
            time.sleep(0.05)

            kbe.click("Q")
            time.sleep(0.05)

            kbe.click("1")