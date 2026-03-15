import events.keyboard_events as kb
import events.mouse_events as ms
from state import state

import time

kbe = kb.Events()
mse = ms.Events()

def check_pause_game():
    if state.active_window:
        if not state.player['hp'] or not bool(state.player['heal']):
            return False
    
    return True

def controler():
    if check_pause_game():
        if state.player["hp"] <= 4 and state.player["heal"]:
            kbe.click(str(state.player["heal"][0]))
            time.sleep(0.05)

            mse.click("right")
            time.sleep(0.05)

            kbe.click("Q")
            time.sleep(0.05)

            kbe.click("1")