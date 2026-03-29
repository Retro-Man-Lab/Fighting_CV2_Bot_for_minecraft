class State():
    def __init__(self):
        self.RUNNING = True

        self.active_window = None
        self.is_active_window_minecraft = None
        self.win_geometry = {
            "left": None,
            "top": None,
            "width": None,
            "height": None
        }
        self.img = None

        self.player = {
            "hp": None,
            "heal": None
        }

        self.prev_state_back = False

state = State()