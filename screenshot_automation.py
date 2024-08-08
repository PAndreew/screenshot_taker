import pyautogui
import schedule
import time
from datetime import datetime
import os
import pygetwindow as gw
import threading

# Directory to save screenshots
screenshot_dir = "screenshots"

# Ensure the directory exists
if not os.path.exists(screenshot_dir):
    os.makedirs(screenshot_dir)

selected_window_title = None
interval = 5

def take_screenshot():
    global selected_window_title
    try:
        window = gw.getWindowsWithTitle(selected_window_title)[0]
        window.activate()
        # Generate a filename with the current date and time
        filename = os.path.join(screenshot_dir, datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".png")
        # Take a screenshot
        screenshot = pyautogui.screenshot()
        # Save the screenshot
        screenshot.save(filename)
        print(f"Screenshot saved as {filename}")
    except Exception as e:
        print(f"An error occurred while taking a screenshot: {e}")

def start_screenshot_schedule():
    global interval
    schedule.every(interval).minutes.do(take_screenshot)
    while True:
        schedule.run_pending()
        time.sleep(1)

def set_parameters(window_title, interval_minutes):
    global selected_window_title, interval
    selected_window_title = window_title
    interval = interval_minutes
    threading.Thread(target=start_screenshot_schedule).start()
