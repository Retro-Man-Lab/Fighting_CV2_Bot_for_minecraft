import ctypes
import time

user32 = ctypes.windll.user32

class Events:

    KEYEVENTF_KEYUP = 0x0002

    KEYMAP = {
        "A": 0x41,
        "B": 0x42,
        "C": 0x43,
        "D": 0x44,
        "E": 0x45,
        "F": 0x46,
        "G": 0x47,
        "H": 0x48,
        "I": 0x49,
        "J": 0x4A,
        "K": 0x4B,
        "L": 0x4C,
        "M": 0x4D,
        "N": 0x4E,
        "O": 0x4F,
        "P": 0x50,
        "Q": 0x51,
        "R": 0x52,
        "S": 0x53,
        "T": 0x54,
        "U": 0x55,
        "V": 0x56,
        "W": 0x57,
        "X": 0x58,
        "Y": 0x59,
        "Z": 0x5A,

        "0": 0x30,
        "1": 0x31,
        "2": 0x32,
        "3": 0x33,
        "4": 0x34,
        "5": 0x35,
        "6": 0x36,
        "7": 0x37,
        "8": 0x38,
        "9": 0x39,

        "SPACE": 0x20,
        "SHIFT": 0x10,
        "CTRL": 0x11,
        "ALT": 0x12,
        "TAB": 0x09,
        "ENTER": 0x0D,
        "ESC": 0x1B
    }

    def _get_vk(self, key):
        key = key.upper()
        return self.KEYMAP[key]

    def is_pressed(self, key):
        vk = self._get_vk(key)
        return bool(user32.GetAsyncKeyState(vk) & 0x8000)

    def key_down(self, key):
        vk = self._get_vk(key)
        user32.keybd_event(vk, 0, 0, 0)

    def key_up(self, key):
        vk = self._get_vk(key)
        user32.keybd_event(vk, 0, self.KEYEVENTF_KEYUP, 0)

    def click(self, key):
        self.key_down(key)
        self.key_up(key)

    def hold(self, key, duration=0.1):
        self.key_down(key)
        time.sleep(duration)
        self.key_up(key)