import tkinter as tk
from tkinter import filedialog
import difflib
import sys

# ---------------- LOGIC ----------------
class Logic:
    def __init__(self):
        self.text_widgets = {}

    def set_text_widgets(self, text1, text2):
        self.text_widgets["text1"] = text1
        self.text_widgets["text2"] = text2

    def load_file(self, textbox):
        path = filedialog.askopenfilename(filetypes=[("*TXT files", "*.txt")])
        if path:
            with open(path, "r", encoding="utf-8") as f:
                textbox.delete("1.0", tk.END)
                textbox.insert(tk.END, f.read())
            self.highlight_differences()

    def highlight_differences(self):
        text1 = self.text_widgets["text1"]
        text2 = self.text_widgets["text2"]

        text1.tag_remove("diff", "1.0", tk.END)
        text2.tag_remove("diff", "1.0", tk.END)

        matcher = difflib.SequenceMatcher(None, text1.get("1.0", tk.END), text2.get("1.0", tk.END))

        for tag, i1, i2, j1, j2 in matcher.get_opcodes():
            if tag != "equal":
                text1.tag_add("diff", f"1.0 + {i1} chars", f"1.0 + {i2} chars")
                text2.tag_add("diff", f"1.0 + {j1} chars", f"1.0 + {j2} chars")

# ---------------- CUSTOM COMPONENTS ----------------
class CustomText(tk.Text):
    def __init__(self, *args, **kwargs):
        tk.Text.__init__(self, *args, **kwargs)
        self.bind("<<Modified>>", self.on_change)

    def on_change(self, event):
        self.event_generate("<<Change>>", when="tail")
        self.edit_modified(False)

class LineNumbers(tk.Canvas):
    def __init__(self, master, text_widget, **kwargs):
        super().__init__(master, **kwargs)
        self.text_widget = text_widget
        self.configure(bg="#1e1e1e", highlightthickness=0)

        self.text_widget.bind("<<Change>>", self.update_numbers)
        self.text_widget.bind("<Configure>", self.update_numbers)
        self.text_widget.bind("<KeyRelease>", self.update_numbers)
        self.text_widget.bind("<MouseWheel>", self.update_numbers)
        self.text_widget.bind("<Button-1>", self.update_numbers)

    def update_numbers(self, event=None):
        self.delete("all")
        i = self.text_widget.index("@0,0")
        while True:
            dline = self.text_widget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            line_num = str(i).split(".")[0]
            self.create_text(35, y, anchor="ne", text=line_num, fill="#888")
            i = self.text_widget.index(f"{i}+1line")

# ---------------- GUI ----------------
class Gui:
    def __init__(self, root):
        self.root = root
        self.root.title("TXT Comparison")
        self.root.configure(bg="#1e1e1e")

        if hasattr(sys, 'frozen') and sys.platform.startswith("win"):
            self.root.iconbitmap(sys.executable)

        self.logic = Logic()

        # text boxes
        self.box1, self.text1, self.ln1 = self.create_textbox(root)
        self.box1.pack(padx=10, pady=5, fill="x")

        self.box2, self.text2, self.ln2 = self.create_textbox(root)
        self.box2.pack(padx=10, pady=5, fill="x")

        #buttons
        self.frame = tk.Frame(root, bg="#1e1e1e")
        self.frame.pack(pady=10)

        self.btn1 = tk.Button(self.frame, text="Load first file ",
                              command=lambda: self.load_file(self.text1), bg="#333", fg="#fff")
        self.btn1.grid(row=0, column=0, padx=5)

        self.btn2 = tk.Button(self.frame, text="Load second file",
                              command=lambda: self.load_file(self.text2), bg="#333", fg="#fff")
        self.btn2.grid(row=0, column=1, padx=5)


        self.logic.set_text_widgets(self.text1, self.text2)


    def create_textbox(self, parent):
        wrapper = tk.Frame(parent, bg="#ffffff")

        textbox = CustomText(
            wrapper,
            width=80,
            height=20,
            bg="#111",
            fg="#eee",
            insertbackground="#fff",
            font=("Consolas", 11),
            wrap="none",
            undo=True
        )

        line_numbers = LineNumbers(wrapper, textbox, width=40)
        line_numbers.grid(row=0, column=0, sticky="ns")

        textbox.grid(row=0, column=1, sticky="nsew")

        scroll = tk.Scrollbar(wrapper, command=textbox.yview)
        textbox.config(yscrollcommand=scroll.set)
        scroll.grid(row=0, column=2, sticky="ns")

        wrapper.grid_columnconfigure(1, weight=1)
        wrapper.grid_rowconfigure(0, weight=1)

        textbox.tag_config("diff", background="#660000")

        return wrapper, textbox, line_numbers

    def load_file(self, textbox):
        self.logic.load_file(textbox)


# ---------------- Main ----------------
if __name__ == "__main__":
    window = tk.Tk()
    app = Gui(window)
    window.mainloop()


#pyinstaller command
#pyinstaller --onefile --windowed --icon=icon.ico --name "Txt Comparison/icon.ico" "TxtComparation.py"