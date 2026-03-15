from rich.console import Console
from rich.live import Live
from rich.table import Table

import config
import time

console = Console()

def create_panel():

    table = Table(title="BOT PANEL")

    table.add_column("Key")
    table.add_column("Function")
    table.add_column("State")

    table.add_row("1", "AutoClick", "ON" if config.AUTO_CLICK else "OFF")
    table.add_row("2", "AutoHeal", "ON" if config.AUTO_HEAL else "OFF")
    table.add_row("Q", "Exit", "")

    return table

def panel_task():

    with Live(create_panel(), refresh_per_second=10) as live:

        while config.RUNNING:

            live.update(create_panel())
            time.sleep(0.1)

import msvcrt


def get_key():

    while True:
        if msvcrt.kbhit():
            return msvcrt.getch().decode("utf-8")
        time.sleep(0.01)

def keyboard_task():

    while config.RUNNING:

        key = get_key()

        if key == "1":
            config.AUTO_CLICK = not config.AUTO_CLICK

        elif key == "2":
            config.AUTO_HEAL = not config.AUTO_HEAL

        elif key.lower() == "q":
            config.RUNNING = False