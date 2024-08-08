import tkinter as tk
from tkinter import ttk, messagebox
import pygetwindow as gw
import screenshot_automation as sa

selected_window_title = None

def start_screenshots():
    interval = int(interval_entry.get())
    sa.set_parameters(selected_window_title.get(), interval)
    messagebox.showinfo("Started", f"Started taking screenshots every {interval} minutes.")

def refresh_window_list():
    window_titles = [window.title for window in gw.getAllWindows() if window.title]
    window_combobox['values'] = window_titles
    if window_titles:
        selected_window_title.set(window_titles[0])

# GUI setup
root = tk.Tk()
root.title("Screenshot Automation")

selected_window_title = tk.StringVar()

window_combobox = ttk.Combobox(root, textvariable=selected_window_title, state="readonly")
window_combobox.pack(pady=10)

refresh_button = tk.Button(root, text="Refresh Window List", command=refresh_window_list)
refresh_button.pack(pady=10)

interval_label = tk.Label(root, text="Set Interval (minutes):")
interval_label.pack(pady=5)

interval_entry = tk.Entry(root)
interval_entry.pack(pady=5)
interval_entry.insert(0, "5")

start_button = tk.Button(root, text="Start", command=start_screenshots)
start_button.pack(pady=20)

# Initial population of the window list
refresh_window_list()

root.mainloop()
