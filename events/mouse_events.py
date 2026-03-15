import ctypes

user32 = ctypes.windll.user32

class Events:

    BUTTONS = {
        "left": 0x01,
        "right": 0x02,
        "middle": 0x04,
        "forward": 0x06,
        "back": 0x05
    }

    EVENTS = {
        "left_down": 0x0002,
        "left_up": 0x0004,
        "right_down": 0x0008,
        "right_up": 0x0010,
        "middle_down": 0x0020,
        "middle_up": 0x0040,
        "move": 0x0001
    }

    def is_pressed(self, button):
        vk = self.BUTTONS[button]
        return bool(user32.GetAsyncKeyState(vk) & 0x8000)

    def down(self, button):
        user32.mouse_event(self.EVENTS[f"{button}_down"], 0, 0, 0, 0)

    def up(self, button):
        user32.mouse_event(self.EVENTS[f"{button}_up"], 0, 0, 0, 0)

    def click(self, button="left"):
        self.down(button)
        self.up(button)

    def move(self, x, y):
        user32.SetCursorPos(x, y)

    def get_pos(self):
        pt = ctypes.wintypes.POINT()
        user32.GetCursorPos(ctypes.byref(pt))
        return pt.x, pt.y