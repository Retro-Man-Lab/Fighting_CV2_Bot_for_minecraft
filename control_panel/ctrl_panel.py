import tkinter as tk
from tkinter import ttk
import config as conf
from state import state
import ctypes
import webbrowser

cfg = conf.config

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

root = tk.Tk()
root.title("Training Bot")
root.geometry("350x360")

# ========= THEME =========
BG = "#0f172a"
CARD = "#1e293b"
TEXT = "#e2e8f0"
ACCENT = "#38bdf8"
HOVER = "#334155"

def hover(widget):
    widget.bind("<Enter>", lambda e: widget.config(bg=HOVER))
    widget.bind("<Leave>", lambda e: widget.config(bg=CARD))

root.configure(bg=BG)

# ========= STATE =========
waiting_for = None

# ========= VARIABLES =========
# KIT
macros_var = tk.BooleanVar(value=cfg.AUTO_CLICK)
autoheal_var = tk.BooleanVar(value=cfg.AUTO_HEAL)
kit_cps_var = tk.StringVar(value=str(cfg.KIT_CPS))

autoclick_key = tk.StringVar(value=cfg.AUTOCLICK_KEY.upper())
autoheal_key = tk.StringVar(value=cfg.AUTOFILL_KEY.upper())

# BEDWARS
bw_pvp_enabled = tk.BooleanVar(value=cfg.BW_PVP_ENABLED)
bw_pvp_key_var = tk.StringVar(value=cfg.BW_PVP_KEY.upper())
bw_pvp_slot = tk.StringVar(value=str(cfg.BW_PVP_SLOT))
bw_pvp_cps = tk.StringVar(value=str(cfg.BW_PVP_CPS))

bw_bridge_enabled = tk.BooleanVar(value=cfg.BW_BRIDGE_ENABLED)
bw_bridge_key_var = tk.StringVar(value=cfg.BW_BRIDGE_KEY.upper())
bw_bridge_slot = tk.StringVar(value=str(cfg.BW_BRIDGE_SLOT))
bw_bridge_cps = tk.StringVar(value=str(cfg.BW_BRIDGE_CPS))

# GLOBAL
mode_var = tk.StringVar(value=cfg.MODE)
message_spam_var = tk.BooleanVar(value=cfg.SPAM)

# ========= SYNC =========
def update_config(*args):
    # KIT
    cfg.AUTO_CLICK = macros_var.get()
    cfg.AUTO_HEAL = autoheal_var.get()
    cfg.SPAM = message_spam_var.get()
    cfg.BW_PVP_KEY = bw_pvp_key_var.get()
    cfg.BW_BRIDGE_KEY = bw_bridge_key_var.get()

    if kit_cps_var.get().isdigit():
        cfg.KIT_CPS = int(kit_cps_var.get())

    cfg.AUTOCLICK_KEY = autoclick_key.get()
    cfg.AUTOFILL_KEY = autoheal_key.get()

    # BEDWARS
    cfg.BW_PVP_ENABLED = bw_pvp_enabled.get()
    cfg.BW_BRIDGE_ENABLED = bw_bridge_enabled.get()

    if bw_pvp_slot.get().isdigit():
        cfg.BW_PVP_SLOT = int(bw_pvp_slot.get())

    if bw_bridge_slot.get().isdigit():
        cfg.BW_BRIDGE_SLOT = int(bw_bridge_slot.get())

    if bw_pvp_cps.get().isdigit():
        cfg.BW_PVP_CPS = int(bw_pvp_cps.get())

    if bw_bridge_cps.get().isdigit():
        cfg.BW_BRIDGE_CPS = int(bw_bridge_cps.get())

    cfg.MODE = mode_var.get()

# trace all
vars_to_track = [
    macros_var,
    autoheal_var,
    kit_cps_var,
    autoclick_key,
    autoheal_key,

    bw_pvp_enabled,
    bw_bridge_enabled,
    bw_pvp_slot,
    bw_bridge_slot,
    bw_pvp_cps,
    bw_bridge_cps,

    bw_pvp_key_var,
    bw_bridge_key_var,

    message_spam_var,
    mode_var
]

for v in vars_to_track:
    v.trace_add("write", update_config)

# ========= KEY CAPTURE =========
def set_key(target):
    global waiting_for
    waiting_for = target

def on_key(event):
    global waiting_for

    if waiting_for == "autoclick":
        autoclick_key.set(event.keysym.upper())

    elif waiting_for == "autoheal":
        autoheal_key.set(event.keysym.upper())
    
    elif waiting_for == "bw_pvp":
        bw_pvp_key_var.set(event.keysym.upper())

    elif waiting_for == "bw_bridge":
        bw_bridge_key_var.set(event.keysym.upper())

    waiting_for = None

root.bind("<KeyPress>", on_key)

# ========= UI =========
top = tk.Frame(root, bg=BG)
top.pack(fill="x")

title = tk.Label(
    top,
    text="Kit PvP",
    bg=BG,
    fg=TEXT,
    font=("Segoe UI", 12, "bold")
)
title.pack(side="left", padx=10, pady=5)

settings_btn = tk.Label(
    top,
    text="⚙",
    bg=BG,
    fg=TEXT,
    font=("Segoe UI", 14),
    cursor="hand2"
)
settings_btn.pack(side="right", padx=10)

settings_btn.bind("<Button-1>", lambda e: show("settings"))
settings_btn.bind("<Enter>", lambda e: settings_btn.config(fg=ACCENT))
settings_btn.bind("<Leave>", lambda e: settings_btn.config(fg=TEXT))

container = tk.Frame(root)
container.pack(fill="both", expand=True)

frames = {}

def show(name):
    for f in frames.values():
        f.pack_forget()

    frames[name].pack(fill="both", expand=True)
    title.config(text=name.replace("_", " ").title())

    sizes = {
        "kit_pvp": "350x270",
        "bedwars": "350x450",
        "settings": "350x360"
    }

    if name in sizes:
        root.geometry(sizes[name])

def dark_check(parent, text, var):
    cb = tk.Checkbutton(
        parent,
        text=text,
        variable=var,
        bg=CARD,
        fg=TEXT,
        activebackground=CARD,
        activeforeground=TEXT,
        selectcolor=BG
    )
    return cb

def card(parent):
    frame = tk.Frame(parent, bg=CARD, bd=0)
    frame.pack(fill="x", padx=10, pady=8)
    return frame

# ===== KIT =====
kit = tk.Frame(container, bg=BG)

c = card(kit)

dark_check(c, "Macros", macros_var).pack(anchor="w")
dark_check(c, "Auto heal", autoheal_var).pack(anchor="w")

# CPS
row = tk.Frame(c, bg=CARD)
row.pack(fill="x", pady=5)

tk.Label(row, text="CPS", bg=CARD, fg=TEXT).pack(side="left")

tk.Entry(
    row,
    textvariable=kit_cps_var,
    width=6,
    bg=BG,
    fg=TEXT,
    insertbackground=TEXT
).pack(side="right")

# keys
keys = card(kit)

# даємо середині розтягуватись
keys.grid_columnconfigure(1, weight=1)

# ===== ROW 0 =====
tk.Label(keys, text="AutoClick", bg=CARD, fg=TEXT)\
    .grid(row=0, column=0, sticky="w")

tk.Label(keys, textvariable=autoclick_key, bg=CARD, fg=ACCENT)\
    .grid(row=0, column=1, sticky="w", padx=5)

btn1 = tk.Label(keys, text="Set", bg=CARD, fg=TEXT, cursor="hand2")
btn1.grid(row=0, column=2, sticky="e")  # 👈 вправо
hover(btn1)
btn1.bind("<Button-1>", lambda e: set_key("autoclick"))

# ===== ROW 1 =====
tk.Label(keys, text="AutoFilling", bg=CARD, fg=TEXT)\
    .grid(row=1, column=0, sticky="w", pady=5)

tk.Label(keys, textvariable=autoheal_key, bg=CARD, fg=ACCENT)\
    .grid(row=1, column=1, sticky="w", padx=5)

btn2 = tk.Label(keys, text="Set", bg=CARD, fg=TEXT, cursor="hand2")
btn2.grid(row=1, column=2, sticky="e")  # 👈 вправо
hover(btn2)
btn2.bind("<Button-1>", lambda e: set_key("autoheal"))

frames["kit_pvp"] = kit

# ===== BEDWARS =====
bw = tk.Frame(container, bg=BG)

# ===== PVP CARD =====
pvp_card = card(bw)

tk.Label(
    pvp_card,
    text="Auto atack",
    bg=CARD,
    fg=ACCENT,
    font=("Segoe UI", 10, "bold")
).pack(anchor="w")

dark_check(pvp_card, "Activate", bw_pvp_enabled).pack(anchor="w")

# ===== KEY =====
row_key = tk.Frame(pvp_card, bg=CARD)
row_key.pack(fill="x", pady=3)

tk.Label(row_key, text="Key", bg=CARD, fg=TEXT).pack(side="left")

tk.Label(row_key, textvariable=bw_pvp_key_var, bg=CARD, fg=ACCENT).pack(side="left", padx=5)

btn = tk.Label(row_key, text="Set", bg=CARD, fg=TEXT, cursor="hand2")
btn.pack(side="right")
hover(btn)
btn.bind("<Button-1>", lambda e: set_key("bw_pvp"))

# Slot
row1 = tk.Frame(pvp_card, bg=CARD)
row1.pack(fill="x", pady=3)

tk.Label(row1, text="Slot sword", bg=CARD, fg=TEXT).pack(side="left")

tk.Spinbox(
    row1,
    from_=1,
    to=9,
    textvariable=bw_pvp_slot,
    width=5,
    bg=BG,
    fg=TEXT,
    insertbackground=TEXT
).pack(side="right")

# CPS
row2 = tk.Frame(pvp_card, bg=CARD)
row2.pack(fill="x", pady=3)

tk.Label(row2, text="CPS", bg=CARD, fg=TEXT).pack(side="left")

tk.Entry(
    row2,
    textvariable=bw_pvp_cps,
    width=6,
    bg=BG,
    fg=TEXT,
    insertbackground=TEXT
).pack(side="right")


# ===== BRIDGE CARD =====
bridge_card = card(bw)

tk.Label(
    bridge_card,
    text="Bridging",
    bg=CARD,
    fg=ACCENT,
    font=("Segoe UI", 10, "bold")
).pack(anchor="w")

dark_check(bridge_card, "Activate", bw_bridge_enabled).pack(anchor="w")

row_key2 = tk.Frame(bridge_card, bg=CARD)
row_key2.pack(fill="x", pady=3)

tk.Label(row_key2, text="Key", bg=CARD, fg=TEXT).pack(side="left")

tk.Label(row_key2, textvariable=bw_bridge_key_var, bg=CARD, fg=ACCENT).pack(side="left", padx=5)

btn2 = tk.Label(row_key2, text="Set", bg=CARD, fg=TEXT, cursor="hand2")
btn2.pack(side="right")
hover(btn2)
btn2.bind("<Button-1>", lambda e: set_key("bw_bridge"))

# Slot
row3 = tk.Frame(bridge_card, bg=CARD)
row3.pack(fill="x", pady=3)

tk.Label(row3, text="Slot blocks", bg=CARD, fg=TEXT).pack(side="left")

tk.Spinbox(
    row3,
    from_=1,
    to=9,
    textvariable=bw_bridge_slot,
    width=5,
    bg=BG,
    fg=TEXT,
    insertbackground=TEXT
).pack(side="right")

# CPS
row4 = tk.Frame(bridge_card, bg=CARD)
row4.pack(fill="x", pady=3)

tk.Label(row4, text="CPS", bg=CARD, fg=TEXT).pack(side="left")

tk.Entry(
    row4,
    textvariable=bw_bridge_cps,
    width=6,
    bg=BG,
    fg=TEXT,
    insertbackground=TEXT
).pack(side="right")


frames["bedwars"] = bw

# ===== SETTINGS =====
settings = tk.Frame(container, bg=BG)

# ===== MODE =====
c = card(settings)

tk.Label(c, text="Mode", bg=CARD, fg=TEXT, font=("Segoe UI", 10, "bold")).pack(anchor="w")

tk.Radiobutton(
    c,
    text="Kit PvP",
    variable=mode_var,
    value="kit_pvp",
    bg=CARD,
    fg=TEXT,
    selectcolor=BG,
    activebackground=CARD
).pack(anchor="w")

tk.Radiobutton(
    c,
    text="Bedwars",
    variable=mode_var,
    value="bedwars",
    bg=CARD,
    fg=TEXT,
    selectcolor=BG,
    activebackground=CARD
).pack(anchor="w")


# ===== MESSAGE SPAM =====
spam_card = card(settings)

dark_check(spam_card, "Message spam", message_spam_var).pack(anchor="w")


# ===== DONATE =====
donate_card = card(settings)

donate_btn = tk.Label(
    donate_card,
    text="💎 Donate",
    bg=CARD,
    fg=ACCENT,
    font=("Segoe UI", 10, "bold"),
    padx=10,
    pady=6,
    cursor="hand2"
)
donate_btn.pack(fill="x")

hover(donate_btn)

# можна потім додати відкриття лінка
donate_btn.bind("<Button-1>", lambda e: webbrowser.open("https://ko-fi.com/retroman"))


# ===== BOTTOM BUTTONS =====
bottom = tk.Frame(settings, bg=BG)
bottom.pack(side="bottom", fill="x", pady=10)

apply_btn = tk.Label(bottom, text="Apply", bg=CARD, fg=TEXT, padx=10, pady=5, cursor="hand2")
apply_btn.pack(side="left", padx=20)
hover(apply_btn)
apply_btn.bind("<Button-1>", lambda e: show(mode_var.get()))

cancel_btn = tk.Label(bottom, text="Cancel", bg=CARD, fg=TEXT, padx=10, pady=5, cursor="hand2")
cancel_btn.pack(side="right", padx=20)
hover(cancel_btn)
cancel_btn.bind("<Button-1>", lambda e: show(cfg.MODE))

frames["settings"] = settings

# tk.Button(top, text="⚙", command=lambda: show("settings")).pack(side="right")

# ========= CLOSE =========
def on_close():
    state.RUNNING = False
    conf.save()
    root.destroy()

root.protocol("WM_DELETE_WINDOW", on_close)

# ========= START =========
# show(cfg.MODE)

# root.mainloop()