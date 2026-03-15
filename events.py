import ctypes
import time

user32 = ctypes.windll.user32

def is_pressed(key):
    return bool(user32.GetAsyncKeyState(key) & 0x8000)

def click(key, delay):
	pass