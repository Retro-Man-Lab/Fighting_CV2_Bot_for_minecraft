import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Training Bot")
root.geometry("350x320")

# ========= TOP =========
top = tk.Frame(root)
top.pack(fill="x")

title_label = tk.Label(top, text="Kit PvP", font=("Arial", 12, "bold"))
title_label.pack(side="left", padx=10)

# ========= CONTAINER =========
container = tk.Frame(root)
container.pack(fill="both", expand=True)

frames = {}

def show_frame(name):
    for f in frames.values():
        f.pack_forget()

    frames[name].pack(fill="both", expand=True)

    titles = {
        "kit_pvp": "Kit PvP",
        "bedwars": "Bedwars",
        "settings": "Settings"
    }
    title_label.config(text=titles[name])

# ========= KIT PVP =========
frame_kit = tk.Frame(container)

tk.Checkbutton(frame_kit, text="Macros").pack(anchor="w")
tk.Checkbutton(frame_kit, text="Auto heal").pack(anchor="w")

kit_grid = tk.Frame(frame_kit)
kit_grid.pack(fill="x", pady=5)

tk.Label(kit_grid, text="CPS:").grid(row=0, column=0, sticky="w")
kit_cps = tk.Entry(kit_grid, width=7)
kit_cps.insert(0, "10")
kit_cps.grid(row=0, column=1, sticky="e")

macro = tk.Frame(frame_kit, bd=1, relief="solid")
macro.pack(pady=10, fill="x")

tk.Label(macro, text="A").pack(side="left")
tk.Button(macro, text="Set").pack(side="left", padx=5)

tk.Label(macro, text="H").pack(side="left", padx=10)
tk.Button(macro, text="Set").pack(side="left")

frames["kit_pvp"] = frame_kit

# ========= BEDWARS =========
frame_bw = tk.Frame(container)

# ===== PVP =====
pvp_frame = tk.Frame(frame_bw)
pvp_frame.pack(fill="x", pady=5)

tk.Label(pvp_frame, text="PVP", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)

pvp_state = tk.BooleanVar()
tk.Checkbutton(pvp_frame, text="Activate", variable=pvp_state).grid(row=1, column=0, columnspan=2, sticky="w")

tk.Label(pvp_frame, text="Slot sword:").grid(row=2, column=0, sticky="w")
slot_sword = tk.Spinbox(pvp_frame, from_=1, to=9, width=5)
slot_sword.delete(0, "end")
slot_sword.insert(0, "1")
slot_sword.grid(row=2, column=1, sticky="e")

tk.Label(pvp_frame, text="CPS:").grid(row=3, column=0, sticky="w")
pvp_cps = tk.Entry(pvp_frame, width=7)
pvp_cps.insert(0, "10")
pvp_cps.grid(row=3, column=1, sticky="e")

ttk.Separator(frame_bw, orient="horizontal").pack(fill="x", pady=10)

# ===== BRIDGING =====
bridge_frame = tk.Frame(frame_bw)
bridge_frame.pack(fill="x", pady=5)

tk.Label(bridge_frame, text="Bridging", font=("Arial", 10, "bold")).grid(row=0, column=0, columnspan=2)

bridge_state = tk.BooleanVar()
tk.Checkbutton(bridge_frame, text="Activate", variable=bridge_state).grid(row=1, column=0, columnspan=2, sticky="w")

tk.Label(bridge_frame, text="Slot blocks:").grid(row=2, column=0, sticky="w")
slot_blocks = tk.Spinbox(bridge_frame, from_=1, to=9, width=5)
slot_blocks.delete(0, "end")
slot_blocks.insert(0, "2")
slot_blocks.grid(row=2, column=1, sticky="e")

tk.Label(bridge_frame, text="CPS:").grid(row=3, column=0, sticky="w")
bridge_cps = tk.Entry(bridge_frame, width=7)
bridge_cps.insert(0, "15")
bridge_cps.grid(row=3, column=1, sticky="e")

frames["bedwars"] = frame_bw

# ========= SETTINGS =========
frame_settings = tk.Frame(container)

mode_var = tk.StringVar(value="kit_pvp")

def apply_settings():
    show_frame(mode_var.get())

tk.Label(frame_settings, text="Mode:").pack()

tk.Radiobutton(frame_settings, text="Kit PvP", variable=mode_var, value="kit_pvp").pack(anchor="w")
tk.Radiobutton(frame_settings, text="Bedwars", variable=mode_var, value="bedwars").pack(anchor="w")

tk.Checkbutton(frame_settings, text="Message spam").pack(anchor="w", pady=10)

tk.Button(frame_settings, text="Donate").pack(pady=5)

bottom = tk.Frame(frame_settings)
bottom.pack(pady=10)

tk.Button(bottom, text="Apply", command=apply_settings).pack(side="left", padx=5)
tk.Button(bottom, text="Cancel", command=lambda: show_frame("kit_pvp")).pack(side="left", padx=5)

frames["settings"] = frame_settings

# ========= SETTINGS BUTTON =========
tk.Button(top, text="⚙", command=lambda: show_frame("settings")).pack(side="right", padx=10)

# ========= START =========
show_frame("kit_pvp")

root.mainloop()