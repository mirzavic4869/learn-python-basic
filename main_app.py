# GUI
# Install tkinter dulu


import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# Init
window = tk.Tk()
window.configure(bg="violet")
window.geometry("200x400")
window.resizable(False, False)

# variabel dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()


def handle_click():
    print(f'{NAMA_DEPAN.get()} {NAMA_BELAKANG.get()}')
    showinfo(title="salam", message="Assalamu'alaikum")


# frame
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10, pady=10, fill="x", expand=True)


# Komponen
# 1. Label Nama depan
nama_depan_label = ttk.Label(input_frame, text="Nama Depan:")
nama_depan_label.pack(padx=10, fill="x", expand=True)
# 2. Entry Nama depan
nama_depan_entry = ttk.Entry(input_frame, textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10, fill="x", expand=True)
# 3. Label Nama Belakang
nama_belakang_label = ttk.Label(input_frame, text="Nama belakang:")
nama_belakang_label.pack(padx=10, fill="x", expand=True)
# 4. Entry Nama Belakang
nama_belakang_entry = ttk.Entry(input_frame, textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10, fill="x", expand=True)
# 5. Tombol
tombol = ttk.Button(input_frame, text="Submit", command=handle_click)
tombol.pack(padx=10, pady=10, fill='x', expand=True)

# Mainloop
window.mainloop()
