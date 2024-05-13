import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet
import os

class FileEncryptorDecryptor:
    def __init__(self, master):
        self.master = master
        self.master.title("Virus Encryptor")
        self.master.geometry("400x200")
        self.master.config(bg="#2C3E50")  # Background color
        
        self.label = tk.Label(self.master, text="Encrypt/Decrypt", fg="#FFFFFF", bg="#2C3E50", font=("Arial", 16, "bold"))
        self.label.pack(pady=10)
        
        self.encrypt_button = tk.Button(self.master, text="Encrypt Virus (1 min)", command=self.encrypt_file, width=20, height=2, bg="#3498DB", fg="#FFFFFF", font=("Arial", 12))
        self.encrypt_button.pack(pady=10)
        
        self.decrypt_button = tk.Button(self.master, text="Release Virus (not recommended)", command=self.decrypt_file, width=25, height=2, bg="#E74C3C", fg="#FFFFFF", font=("Arial", 12))
        self.decrypt_button.pack(pady=5)
        
    def encrypt_file(self):
        file_to_encrypt = self.search_file("scanned_files.txt")
        if file_to_encrypt:
            key = Fernet.generate_key()
            key_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thekey.key")
            with open(key_file_path, "wb") as key_file:
                key_file.write(key)
            
            with open(file_to_encrypt, "rb") as f:
                data = f.read()
            
            fernet = Fernet(key)
            encrypted_data = fernet.encrypt(data)
            
            with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "encrypted_scanned_files.txt"), "wb") as encrypted_file:
                encrypted_file.write(encrypted_data)
                
            messagebox.showinfo("Success", "Virus Successfully Encrypted")
    
    def decrypt_file(self):
        file_path = filedialog.askopenfilename(initialdir="/", title="Select Encrypted File", filetypes=(("All Files", "*.*"),))
        if file_path:
            key_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "thekey.key")
            with open(key_file_path, "rb") as key_file:
                key = key_file.read()
                    
            fernet = Fernet(key)
                
            with open(file_path, "rb") as encrypted_file:
                encrypted_data = encrypted_file.read()
                    
            decrypted_data = fernet.decrypt(encrypted_data)
            
            output_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), os.path.basename(file_path)[:-10])
                
            with open(output_file_path, "wb") as decrypted_file:
                decrypted_file.write(decrypted_data)
                    
            os.remove(file_path)
            
            messagebox.showinfo("Success", "File successfully decrypted. Decrypted file: {}".format(output_file_path))
    
    def search_file(self, filename):
        for root, dirs, files in os.walk("C:\\"):
            if filename in files:
                return os.path.join(root, filename)
        messagebox.showerror("Error", "File not found.")

def main():
    root = tk.Tk()
    app = FileEncryptorDecryptor(root)
    root.mainloop()

if __name__ == "__main__":
    main()
