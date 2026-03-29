import config as conf

from macros.kitpvp import run_kitpvp
from macros.bedwars import run_bedwars
from macros.send_message import run_spam

cfg = conf.config

def macros():
    if cfg.MODE == "kit_pvp":
        run_kitpvp()

    elif cfg.MODE == "bedwars":
        run_bedwars()

    run_spam()