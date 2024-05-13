import os
import time
import tkinter as tk
from tkinter import ttk

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        for file_name in files:
            # Dosya yollarından "C:\\Program Files" kısmını kaldır
            file_path = os.path.relpath(os.path.join(root, file_name), startpath)
            print(file_path)


def on_pressCleanbutton():
    print("Virus Found Please start the Deleter.py")

print("Decompressing file, please wait...")

time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".")

print("\nacb.lib64 downloading...")

# Program Files dizinini tarayalım
program_files_path = os.environ.get("ProgramFiles")
print("Scanning files in Program Files directory...")
list_files(program_files_path)

print("Your files are scanned, your PC has a virus.")

root = tk.Tk()
root.configure(bg="red")  # Kırmızı arka planlı etiket oluştur
style = ttk.Style(root)
root.title("PyDefender")  # Başlık verme kısmı
root.geometry("321x230")  # Pencere boyutu

label = tk.LabelFrame(root, text="")
label.grid(row=0, column=0, padx=60, pady=60)

text = ttk.Label(label, text="Your Computer Has a Ransomware")
text.grid(row=1, column=0)

clean_button = tk.Button(root, text="Clean The Virus", command=on_pressCleanbutton)
clean_button.grid(row=1, column=0, padx=(20, 0), pady=0)

root.mainloop()
