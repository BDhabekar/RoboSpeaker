# ui/app_window.py — Tkinter UI for RoboSpeaker

import tkinter as tk
from tkinter import ttk, messagebox
import threading

from core.tts_engine import TTSEngine
from utils.helpers import sanitize_text, chunk_text
from utils.logger import get_logger
from config import APP_NAME, APP_VERSION

logger = get_logger(__name__)


class RoboSpeakerApp:
    """Main application window."""

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title(f"{APP_NAME} v{APP_VERSION}")
        self.root.resizable(False, False)

        self.tts = TTSEngine()
        self._is_speaking = False

        self._build_ui()

    def _build_ui(self):
        """Assemble all UI widgets."""
        pad = {"padx": 12, "pady": 8}

        # Title label
        tk.Label(
            self.root,
            text="🤖 RoboSpeaker",
            font=("Helvetica", 18, "bold")
        ).pack(**pad)

        # Text input area
        tk.Label(self.root, text="Enter text to speak:", anchor="w").pack(fill="x", padx=12)
        self.text_box = tk.Text(self.root, height=6, width=50, wrap="word", font=("Helvetica", 11))
        self.text_box.pack(padx=12, pady=4)

        # Rate slider
        rate_frame = tk.Frame(self.root)
        rate_frame.pack(fill="x", **pad)
        tk.Label(rate_frame, text="Speed:").pack(side="left")
        self.rate_var = tk.IntVar(value=150)
        tk.Scale(
            rate_frame, from_=80, to=250, orient="horizontal",
            variable=self.rate_var, length=200,
            command=lambda v: self.tts.set_rate(int(v))
        ).pack(side="left", padx=8)

        # Volume slider
        vol_frame = tk.Frame(self.root)
        vol_frame.pack(fill="x", padx=12, pady=2)
        tk.Label(vol_frame, text="Volume:").pack(side="left")
        self.vol_var = tk.DoubleVar(value=1.0)
        tk.Scale(
            vol_frame, from_=0.1, to=1.0, resolution=0.1, orient="horizontal",
            variable=self.vol_var, length=200,
            command=lambda v: self.tts.set_volume(float(v))
        ).pack(side="left", padx=8)

        # Speak & Stop buttons
        btn_frame = tk.Frame(self.root)
        btn_frame.pack(**pad)
        self.speak_btn = tk.Button(
            btn_frame, text="▶  Speak", width=14,
            bg="#2ecc71", fg="white", font=("Helvetica", 11, "bold"),
            command=self._on_speak
        )
        self.speak_btn.pack(side="left", padx=6)

        self.stop_btn = tk.Button(
            btn_frame, text="■  Stop", width=14,
            bg="#e74c3c", fg="white", font=("Helvetica", 11, "bold"),
            command=self._on_stop, state="disabled"
        )
        self.stop_btn.pack(side="left", padx=6)

        # Status bar
        self.status_var = tk.StringVar(value="Ready")
        tk.Label(
            self.root, textvariable=self.status_var,
            fg="gray", font=("Helvetica", 9)
        ).pack(pady=4)

    def _on_speak(self):
        """Triggered when Speak button is clicked."""
        raw_text = self.text_box.get("1.0", "end")
        text = sanitize_text(raw_text)

        if not text:
            messagebox.showwarning("No text", "Please enter some text to speak.")
            return

        self._set_speaking(True)
        chunks = chunk_text(text)

        # Run TTS in a background thread to keep UI responsive
        threading.Thread(target=self._speak_chunks, args=(chunks,), daemon=True).start()

    def _speak_chunks(self, chunks: list):
        """Speak each chunk sequentially."""
        for i, chunk in enumerate(chunks):
            if not self._is_speaking:
                break
            self.status_var.set(f"Speaking... (chunk {i+1}/{len(chunks)})")
            self.tts.speak(chunk)

        self.root.after(0, lambda: self._set_speaking(False))

    def _on_stop(self):
        """Stop ongoing speech."""
        self._is_speaking = False
        self.tts.stop()
        self.status_var.set("Stopped.")

    def _set_speaking(self, is_speaking: bool):
        """Toggle button states based on speaking status."""
        self._is_speaking = is_speaking
        self.speak_btn.config(state="disabled" if is_speaking else "normal")
        self.stop_btn.config(state="normal" if is_speaking else "disabled")
        self.status_var.set("Speaking..." if is_speaking else "Ready")
