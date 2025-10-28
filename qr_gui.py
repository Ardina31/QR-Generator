import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk, Image
import os
from qr_utils import generate_qr

def on_generate():
    data = entry.get().strip()
    if not data:
        messagebox.showwarning("Input Error", "Please enter text or URL.")
        return

    filename = "assets/qr_code.png"
    os.makedirs("assets", exist_ok=True)
    generate_qr(data, filename)

    img = Image.open(filename)
    img = img.resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk
    messagebox.showinfo("Success", f"QR code saved as {filename}")

# GUI setup
root = tk.Tk()
root.title("QR Code Generator")
root.geometry("400x400")
root.resizable(False, False)

tk.Label(root, text="Enter text or URL:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

tk.Button(root, text="Generate QR", command=on_generate, font=("Arial", 12)).pack(pady=10)
qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()