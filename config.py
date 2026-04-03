import json
from dataclasses import dataclass, asdict
from pathlib import Path

CONFIG_PATH = Path.home() / "AppData" / "Local" / "Minecraft_PVP_Traning_Bot" / "config.json"


@dataclass
class Config:
    # ===== GLOBAL =====
    MODE: str = "kit_pvp"
    SPAM: bool = True

    # ===== KIT PVP =====
    AUTO_CLICK: bool = True
    AUTO_HEAL: bool = True
    KIT_CPS: int = 20

    AUTOCLICK_KEY: str = "C"
    AUTOFILL_KEY: str = "V"

    # ===== BEDWARS PVP =====
    BW_PVP_ENABLED: bool = True
    BW_PVP_KEY: str = "C"
    BW_PVP_SLOT: int = 1
    BW_PVP_CPS: int = 25

    # ===== BEDWARS BRIDGE =====
    BW_BRIDGE_ENABLED: bool = True
    BW_BRIDGE_KEY: str = "V"
    BW_BRIDGE_SLOT: int = 9
    BW_BRIDGE_CPS: int = 20

    # ===== AUTHOR =====
    AUTHOR: str = "Retro Man"


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
    CONFIG_PATH.parent.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_PATH, "w") as f:
        json.dump(asdict(config), f, indent=4)