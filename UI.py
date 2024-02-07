import tkinter as tk
from tkinter import scrolledtext

class AssistantUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("OpenAI Assistant")
        self.create_widgets()

    def create_widgets(self):
        self.text_area = scrolledtext.ScrolledText(self.window, wrap=tk.WORD, width=40, height=10)
        self.text_area.pack(padx=10, pady=10)

        self.button_run = tk.Button(self.window, text="Run Assistant", command=self.run_assistant)
        self.button_run.pack(pady=5)

        self.button_exit = tk.Button(self.window, text="Exit", command=self.window.destroy)
        self.button_exit.pack(pady=5)

    def run_assistant(self):
        user_input = self.text_area.get("1.0", tk.END)
        # You can replace the next line with your assistant logic
        ai(prompt=user_input)

if __name__ == '__main__':
    assistant_ui = AssistantUI()
    s = "Jai SHREE RAAM, I am Oam"
    print(s)
    speaker.speak(s)
    assistant_ui.window.mainloop()

