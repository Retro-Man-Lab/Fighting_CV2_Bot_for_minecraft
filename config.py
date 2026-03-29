import json
from dataclasses import dataclass, asdict

CONFIG_PATH = "bd.json"


@dataclass
class Config:
    # ===== GLOBAL =====
    MODE: str = "kit_pvp"
    SPAM: bool = True

    # ===== KIT PVP =====
    AUTO_CLICK: bool = True
    AUTO_HEAL: bool = True
    KIT_CPS: int = 20

    AUTOCLICK_KEY: str = "X"
    AUTOFILL_KEY: str = "H"

    # ===== BEDWARS PVP =====
    BW_PVP_ENABLED: bool = False
    BW_PVP_KEY: str = "X"
    BW_PVP_SLOT: int = 1
    BW_PVP_CPS: int = 10

    # ===== BEDWARS BRIDGE =====
    BW_BRIDGE_ENABLED: bool = False
    BW_BRIDGE_KEY: str = "C"
    BW_BRIDGE_SLOT: int = 2
    BW_BRIDGE_CPS: int = 15


config = Config()


def load():
    global config

    try:
        with open(CONFIG_PATH, "r") as f:
            data = json.load(f)

        config = Config(**data)

    except FileNotFoundError:
        save()


def save():
    with open(CONFIG_PATH, "w") as f:
        json.dump(asdict(config), f, indent=4)