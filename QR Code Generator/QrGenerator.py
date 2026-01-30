import qrcode
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import  ImageTk


class Generator:
    def __init__(self):
        self.qr_image = None

    def generate(self, data: str):
        if not data:
            return None

        self.qr_image = qrcode.make(data)
        return self.qr_image

    def save(self, file_path: str):
        if self.qr_image and file_path:
            self.qr_image.save(file_path)


class UI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title('QR Code Generator')
        self.root.geometry('540x640')
        self.root.resizable(False, False)

        self.generator = Generator()
        self.qr_photo = None

        self.create_layout()

    def create_layout(self):
        self.preview_frame = ttk.Frame(self.root)
        self.preview_frame.pack(fill="both", expand=True)

        self.preview_label = ttk.Label(
            self.preview_frame,
            text="Waiting for QR code...",
            anchor="center",
            font=("Segoe UI", 24)
        )
        self.preview_label.pack(expand=True)


        self.bottom_frame = ttk.Frame(self.root)
        self.bottom_frame.pack(side="bottom", pady=20)

        self.entry = ttk.Entry(self.bottom_frame, width=86)
        self.entry.pack(pady=5)

        btn_frame = ttk.Frame(self.bottom_frame)
        btn_frame.pack()

        self.generate_btn = ttk.Button(
            btn_frame, text="Generate", command=self.on_generate, width=42
        )
        self.generate_btn.grid(row=0, column=0)

        self.save_btn = ttk.Button(
            btn_frame, text="Save", command=self.on_save, width=42
        )
        self.save_btn.grid(row=0, column=1)


    def on_generate(self):
        data = self.entry.get()

        qr_image = self.generator.generate(data)
        if qr_image is None:
            messagebox.showwarning("Warning", "Enter some text first!")
            return

        resized = qr_image.resize((512, 512))
        self.qr_photo = ImageTk.PhotoImage(resized)
        self.preview_label.config(image=self.qr_photo, text="")

    def on_save(self):
        if self.generator.qr_image is None:
            messagebox.showwarning("Warning", "Generate QR code first!")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )

        if file_path:
            self.generator.save(file_path)
            messagebox.showinfo("Saved", "QR code saved successfully!")


if __name__ == "__main__":
    app = UI()
    app.root.mainloop()