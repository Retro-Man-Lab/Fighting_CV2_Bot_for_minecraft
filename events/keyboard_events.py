import ctypes
import time

user32 = ctypes.windll.user32

class Events:

    KEYEVENTF_KEYUP = 0x0002

    KEYMAP = {
        # letters
        **{chr(i): i for i in range(65, 91)},

        # numbers
        **{str(i): 0x30 + i for i in range(10)},

         # special
        "space": 0x20,
        "Return": 0x0D,
        "Escape": 0x1B,
        "Tab": 0x09,

        # modifiers
        "Shift_L": 0x10,
        "Shift_R": 0x10,
        "Control_L": 0x11,
        "Control_R": 0x11,
        "Alt_L": 0x12,
        "Alt_R": 0x12,
    }

    def _get_vk(self, key):
        key = key.upper()
        try:
            return self.KEYMAP[key]
        except KeyError:
            return False

    def is_pressed(self, key):
        if not key:
            return False
        if self._get_vk(key):
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