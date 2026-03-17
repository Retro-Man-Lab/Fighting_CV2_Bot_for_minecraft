from state import state

import win32gui
import mss
import numpy as np

import time

def update_active_window():
    hwnd = win32gui.GetForegroundWindow()
    state.active_window = win32gui.GetWindowText(hwnd)


def is_minecraft_active():
    update_active_window()

    if not state.active_window:
        return False

    state.is_active_window_minecraft = "minecraft" in state.active_window.lower()
    return state.is_active_window_minecraft


def update_window_geometry():

    if not is_minecraft_active():
        return False

    hwnd = win32gui.GetForegroundWindow()

    left, top, right, bottom = win32gui.GetClientRect(hwnd)
    x, y = win32gui.ClientToScreen(hwnd, (left, top))

    state.win_geometry["left"] = x
    state.win_geometry["top"] = y
    state.win_geometry["width"] = right - left
    state.win_geometry["height"] = bottom - top

    return True


def capture():

    if not update_window_geometry():
        return False
    
    if state.win_geometry["width"] <= 0 or state.win_geometry["height"] <= 0:
        return False

    monitor = {
        "left": state.win_geometry["left"],
        "top": state.win_geometry["top"],
        "width": state.win_geometry["width"],
        "height": state.win_geometry["height"]
    }

    with mss.mss() as sct:
        time.sleep(2)
        state.img = np.array(sct.grab(monitor))

    return True