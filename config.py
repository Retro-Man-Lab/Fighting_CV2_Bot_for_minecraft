import json

# ---- default values ----
RUNNING = True

AUTO_CLICK = True
AUTO_HEAL = True
clicks_per_second = 20

AUTOCLICK_KEY = "X"
AUTOFILL_KEY = "H"


def load():
    global AUTO_CLICK, AUTO_HEAL, clicks_per_second
    global AUTOCLICK_KEY, AUTOFILL_KEY

    try:
        with open("bd.json", "r") as f:
            data = json.load(f)

        AUTO_CLICK = data["AUTO_CLICK"]
        AUTO_HEAL = data["AUTO_HEAL"]
        clicks_per_second = data["clicks_per_second"]

        AUTOCLICK_KEY = data["AUTOCLICK_KEY"]
        AUTOFILL_KEY = data["AUTOFILL_KEY"]

    except FileNotFoundError:
        save()


def save():
    data = {
        "AUTO_CLICK": AUTO_CLICK,
        "AUTO_HEAL": AUTO_HEAL,
        "clicks_per_second": clicks_per_second,
        "AUTOCLICK_KEY": AUTOCLICK_KEY,
        "AUTOFILL_KEY": AUTOFILL_KEY
    }

    with open("bd.json", "w") as f:
        json.dump(data, f, indent=4)