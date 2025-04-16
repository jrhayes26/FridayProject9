# gui_app.py (Styled ChatGPT GUI with Blue/Green Theme)
import tkinter as tk
from tkinter import messagebox
import urllib.request
import json
import os

# -------------------------
# 1. Load API Key from .env
# -------------------------
def load_api_key():
    try:
        with open(".env", "r") as f:
            for line in f:
                if line.startswith("OPENAI_API_KEY="):
                    return line.strip().split("=")[1]
    except FileNotFoundError:
        raise ValueError(".env file not found. Please create one with your API key.")

API_KEY = load_api_key()

# -------------------------
# 2. Call Chat Completion API
# -------------------------
def call_openai_api(prompt):
    data = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }).encode("utf-8")

    req = urllib.request.Request("https://api.openai.com/v1/chat/completions", data=data)
    req.add_header("Content-Type", "application/json")
    req.add_header("Authorization", f"Bearer {API_KEY}")

    try:
        with urllib.request.urlopen(req) as response:
            result = json.loads(response.read())
            return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# -------------------------
# 3. GUI Setup with Blue/Green Theme
# -------------------------
COLORS = {
    "bg": "#e0f7fa",         # Light aqua background
    "highlight": "#00796b",  # Teal accent
    "button": "#80cbc4",     # Soft teal button
    "entry_bg": "#ffffff",   # White input boxes
    "text": "#004d40"         # Deep green text
}

FONT = ("Segoe UI", 11)
TITLE_FONT = ("Segoe UI", 14, "bold")

def run_gui():
    window = tk.Tk()
    window.title("AI Prompt Generator")
    window.geometry("700x500")
    window.configure(bg=COLORS["bg"])

    # Title
    tk.Label(window, text="AI Completion App", font=TITLE_FONT,
             bg=COLORS["bg"], fg=COLORS["highlight"]).pack(pady=10)

    # Prompt Label & Entry
    tk.Label(window, text="Enter your prompt:", font=FONT, bg=COLORS["bg"], fg=COLORS["text"]).pack()
    prompt_entry = tk.Text(window, height=6, font=FONT, bg=COLORS["entry_bg"], wrap="word")
    prompt_entry.pack(padx=20, pady=(5, 10), fill="x")

    # Output Box Label
    tk.Label(window, text="AI Response:", font=FONT, bg=COLORS["bg"], fg=COLORS["text"]).pack()
    output_box = tk.Text(window, height=12, font=FONT, bg=COLORS["entry_bg"], wrap="word", state="disabled")
    output_box.pack(padx=20, pady=(5, 15), fill="both", expand=True)

    # Submit Button
    def generate_completion():
        prompt = prompt_entry.get("1.0", tk.END).strip()
        if not prompt:
            messagebox.showwarning("Input Needed", "Please enter a prompt.")
            return

        completion = call_openai_api(prompt)
        output_box.config(state="normal")
        output_box.delete("1.0", tk.END)
        output_box.insert(tk.END, completion)
        output_box.config(state="disabled")

    tk.Button(window, text="Generate Response", font=FONT, bg=COLORS["button"], fg=COLORS["text"],
              relief="flat", activebackground=COLORS["highlight"], command=generate_completion).pack(pady=10)

    window.mainloop()

if __name__ == "__main__":
    run_gui()
