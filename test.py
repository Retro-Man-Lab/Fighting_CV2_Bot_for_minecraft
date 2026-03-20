import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Minecraft PvP Trainer Bot")
root.geometry("320x240")
root.resizable(False, False)

# ---- Variables ----
macros_var = tk.BooleanVar()
autoheal_var = tk.BooleanVar()
cps_var = tk.IntVar(value=10)

autoclick_key = tk.StringVar(value="None")
autoheal_key = tk.StringVar(value="None")

waiting_for = None

# ---- Key capture ----
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
title = ttk.Label(root, text="Bot Settings", font=("Arial", 14))
title.pack(pady=10)

ttk.Checkbutton(root, text="Macros", variable=macros_var).pack(anchor="w", padx=20)
ttk.Checkbutton(root, text="Auto Heal", variable=autoheal_var).pack(anchor="w", padx=20)

# ---- CPS ----
cps_frame = ttk.Frame(root)
cps_frame.pack(pady=10)

ttk.Label(cps_frame, text="CPS:").pack(side="left")
ttk.Entry(cps_frame, textvariable=cps_var, width=5).pack(side="left", padx=5)

# ---- AutoClick key ----
click_frame = ttk.Frame(root)
click_frame.pack(pady=5)

ttk.Label(click_frame, text="AutoClick:").pack(side="left")
ttk.Label(click_frame, textvariable=autoclick_key, width=8).pack(side="left", padx=5)

ttk.Button(
    click_frame,
    text="Set",
    command=lambda: set_key("autoclick")
).pack(side="left")

# ---- AutoHeal key ----
heal_frame = ttk.Frame(root)
heal_frame.pack(pady=5)

ttk.Label(heal_frame, text="AutoHeal:").pack(side="left")
ttk.Label(heal_frame, textvariable=autoheal_key, width=8).pack(side="left", padx=5)

ttk.Button(
    heal_frame,
    text="Set",
    command=lambda: set_key("autoheal")
).pack(side="left")

# ---- Start button ----
def start_bot():
    print("Macros:", macros_var.get())
    print("AutoHeal:", autoheal_var.get())
    print("CPS:", cps_var.get())
    print("AutoClick key:", autoclick_key.get())
    print("AutoHeal key:", autoheal_key.get())

ttk.Button(root, text="Start Bot", command=start_bot).pack(pady=15)

root.mainloop()