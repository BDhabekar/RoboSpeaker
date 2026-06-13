# main.py — Entry point for RoboSpeaker

import tkinter as tk
from ui.app_window import RoboSpeakerApp


def main():
    root = tk.Tk()
    app = RoboSpeakerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
