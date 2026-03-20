import tkinter as tk
from tkinter import ttk
import config as cfg

root = tk.Tk()
root.title("Bot Settings")
root.geometry("320x240")

# ---- Tk variables (беремо з cfg) ----
macros_var = tk.BooleanVar(value=cfg.AUTO_CLICK)
autoheal_var = tk.BooleanVar(value=cfg.AUTO_HEAL)

cps_var = tk.StringVar(value=cfg.clicks_per_second)

autoclick_key = tk.StringVar(value=cfg.AUTOCLICK_KEY)
autoheal_key = tk.StringVar(value=cfg.AUTOFILL_KEY)

waiting_for = None


# ---- sync UI -> cfg ----
def update_config(*args):
    cfg.AUTO_CLICK = macros_var.get()
    cfg.AUTO_HEAL = autoheal_var.get()
    value = cps_var.get()

    if value.isdigit():
        cfg.clicks_per_second = int(value)

    cfg.AUTOCLICK_KEY = autoclick_key.get()
    cfg.AUTOFILL_KEY = autoheal_key.get()


# кожна зміна автоматично оновлює cfg
macros_var.trace_add("write", update_config)
autoheal_var.trace_add("write", update_config)
cps_var.trace_add("write", update_config)
autoclick_key.trace_add("write", update_config)
autoheal_key.trace_add("write", update_config)


# ---- key capture ----
def set_key(target):
    global waiting_for
    waiting_for = target


def on_key(event):
    global waiting_for

    if waiting_for == "autoclick":
        autoclick_key.set(event.keysym)

    elif waiting_for == "autoheal":
        autoheal_key.set(event.keysym)

    waiting_for = None


root.bind("<KeyPress>", on_key)


# ---- UI ----

ttk.Checkbutton(root, text="Macros", variable=macros_var).pack(anchor="w", padx=20)
ttk.Checkbutton(root, text="Auto Heal", variable=autoheal_var).pack(anchor="w", padx=20)

# CPS
frame_cps = ttk.Frame(root)
frame_cps.pack(pady=10)

ttk.Label(frame_cps, text="CPS").pack(side="left")
ttk.Entry(frame_cps, textvariable=cps_var, width=5).pack(side="left", padx=5)

# AutoClick key
frame_click = ttk.Frame(root)
frame_click.pack(pady=5)

ttk.Label(frame_click, text="AutoClick").pack(side="left")
ttk.Label(frame_click, textvariable=autoclick_key, width=8).pack(side="left", padx=5)

ttk.Button(
    frame_click,
    text="Set",
    command=lambda: set_key("autoclick")
).pack(side="left")


# AutoHeal key
frame_heal = ttk.Frame(root)
frame_heal.pack(pady=5)

ttk.Label(frame_heal, text="AutoHeal").pack(side="left")
ttk.Label(frame_heal, textvariable=autoheal_key, width=8).pack(side="left", padx=5)

ttk.Button(
    frame_heal,
    text="Set",
    command=lambda: set_key("autoheal")
).pack(side="left")


# debug button
# def show_cfg():
#     print(cfg.AUTO_CLICK, cfg.AUTO_HEAL, cfg.clicks_per_second, cfg.AUTOCLICK_KEY, cfg.AUTOFILL_KEY)


# ttk.Button(root, text="Print cfg", command=show_cfg).pack(pady=10)

def on_close():
    cfg.RUNNING = False
    cfg.save()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)