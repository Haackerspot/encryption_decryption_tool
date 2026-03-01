# encryption_decryption_tool
import os
from tkinter import *
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet


# -----------------------------
# KEY MANAGEMENT FUNCTIONS
# -----------------------------
def generate_key():
    """Generate a new encryption key and save it."""
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    messagebox.showinfo("Key Generated", "A new key has been saved as 'secret.key'.")


def load_key():
    """Load the encryption key from secret.key"""
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        messagebox.showerror("Error", "No key found! Generate a key first.")
        return None


# -----------------------------
# ENCRYPT / DECRYPT FUNCTIONS
# -----------------------------
def encrypt_text():
    """Encrypt the message entered by the user."""
    key = load_key()
    if key is None:
        return
    text = text_input.get("1.0", END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to encrypt.")
        return
    fernet = Fernet(key)
    encrypted = fernet.encrypt(text.encode())
    text_output.delete("1.0", END)
    text_output.insert(END, encrypted.decode())


def decrypt_text():
    """Decrypt the message entered by the user."""
    key = load_key()
    if key is None:
        return
    text = text_input.get("1.0", END).strip()
    if not text:
        messagebox.showwarning("Warning", "Please enter text to decrypt.")
        return
    try:
        fernet = Fernet(key)
        decrypted = fernet.decrypt(text.encode()).decode()
        text_output.delete("1.0", END)
        text_output.insert(END, decrypted)
    except Exception:
        messagebox.showerror("Error", "Invalid encrypted text or wrong key.")


def encrypt_file():
    """Encrypt a selected file."""
    key = load_key()
    if key is None:
        return
    filename = filedialog.askopenfilename(title="Select File to Encrypt")
    if not filename:
        return
    with open(filename, "rb") as file:
        original = file.read()
    fernet = Fernet(key)
    encrypted = fernet.encrypt(original)
    with open(filename, "wb") as encrypted_file:
        encrypted_file.write(encrypted)
    messagebox.showinfo("Success", f"File '{os.path.basename(filename)}' encrypted successfully!")


def decrypt_file():
    """Decrypt a selected file."""
    key = load_key()
    if key is None:
        return
    filename = filedialog.askopenfilename(title="Select File to Decrypt")
    if not filename:
        return
    with open(filename, "rb") as file:
        encrypted = file.read()
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(encrypted)
        with open(filename, "wb") as decrypted_file:
            decrypted_file.write(decrypted)
        messagebox.showinfo("Success", f"File '{os.path.basename(filename)}' decrypted successfully!")
    except Exception:
        messagebox.showerror("Error", "Decryption failed! Invalid key or corrupted file.")


# -----------------------------
# GUI SETUP
# -----------------------------
root = Tk()
root.title("🔐 Encryption & Decryption Tool")
root.geometry("720x500")
root.config(bg="#1e1e1e")
title_label = Label(root, text="ENCRYPTION & DECRYPTION TOOL", bg="#1e1e1e", fg="white", font=("Arial", 18, "bold"))
title_label.pack(pady=10)
# Frame for Text Encryption
frame = Frame(root, bg="#252526")
frame.pack(pady=10, padx=20, fill=X)
Label(frame, text="Enter Text Below:", bg="#252526", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", padx=10,
                                                                                                  pady=5)
text_input = Text(frame, height=5, wrap=WORD, font=("Arial", 12))
text_input.pack(padx=10, pady=5, fill=X)
button_frame = Frame(frame, bg="#252526")
button_frame.pack(pady=5)
Button(button_frame, text="Encrypt Text", bg="#007acc", fg="white", font=("Arial", 11, "bold"), width=15,
       command=encrypt_text).grid(row=0, column=0, padx=5)
Button(button_frame, text="Decrypt Text", bg="#3a96dd", fg="white", font=("Arial", 11, "bold"), width=15,
       command=decrypt_text).grid(row=0, column=1, padx=5)
Label(frame, text="Output:", bg="#252526", fg="white", font=("Arial", 12, "bold")).pack(anchor="w", padx=10, pady=5)
text_output = Text(frame, height=5, wrap=WORD, font=("Arial", 12), fg="#00ff9f")
text_output.pack(padx=10, pady=5, fill=X)
# Frame for File Encryption
file_frame = Frame(root, bg="#252526")
file_frame.pack(pady=10, padx=20, fill=X)
Label(file_frame, text="File Encryption / Decryption:", bg="#252526", fg="white", font=("Arial", 12, "bold")).pack(
    anchor="w", padx=10, pady=5)
file_btn_frame = Frame(file_frame, bg="#252526")
file_btn_frame.pack(pady=5)
Button(file_btn_frame, text="Encrypt File", bg="#007acc", fg="white", font=("Arial", 11, "bold"), width=15,
       command=encrypt_file).grid(row=0, column=0, padx=5)
Button(file_btn_frame, text="Decrypt File", bg="#3a96dd", fg="white", font=("Arial", 11, "bold"), width=15,
       command=decrypt_file).grid(row=0, column=1, padx=5)
Button(file_btn_frame, text="Generate Key", bg="#00aa00", fg="white", font=("Arial", 11, "bold"), width=15,
       command=generate_key).grid(row=0, column=2, padx=5)
footer = Label(root, text="Developed with ❤️ in Python", bg="#1e1e1e", fg="gray", font=("Arial", 10))
footer.pack(side=BOTTOM, pady=10)
root.mainloop()
