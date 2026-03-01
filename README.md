🔐 Encryption & Decryption Tool (Python GUI)

A simple yet powerful Encryption & Decryption Tool built using Python, Tkinter, and Fernet symmetric encryption from the cryptography library.

This tool allows users to:
  Encrypt & decrypt text messages
  Encrypt & decrypt files
  Generate and manage encryption keys
  Use a clean and modern dark-themed GUI

📌 Features


🔑 Key Management

    Generate a secure encryption key (secret.key)
    Automatically load the key for encryption/decryption
    Error handling if key is missing

📝 Text Encryption & Decryption

    Encrypt plain text into secure cipher text
    Decrypt cipher text back into readable text
    Real-time output display inside GUI
    Validation and error handling

📂 File Encryption & Decryption

    Encrypt selected files securely
    Decrypt encrypted files
    Works with any file type (text, images, PDFs, etc.)
    Overwrites the selected file after encryption/decryption

🎨 User Interface

    Built with Tkinter
    Dark theme UI
    Interactive message boxes
    Clean layout design


🛠️ Technologies Used

    Python 3.x
    Tkinter (GUI)
    cryptography library
    Fernet symmetric encryption


🔐 About Fernet Encryption

This tool uses Fernet symmetric encryption provided by the cryptography library.
Fernet guarantees:

    Confidentiality
    Integrity
    Authentication
    Secure key generation

Encryption type used:

    Symmetric Key Encryption
    Same key is used for encryption and decryption
    

📦 Installation
Step 1: Clone the Repository
git clone https://github.com/Haackerspot/encryption_decryption_tool
cd encryption-decryption-tool

Step 2: Install Required Library
pip install cryptography

Tkinter is pre-installed with Python in most systems.

🚀 How to Run
python encryption_decryption_tool.py
🖥️ How It Works
1️⃣ Generate Key

    Click Generate Key
    A file named secret.key will be created
    This key is required for encryption & decryption

⚠️ Keep this file safe. If lost, encrypted data cannot be recovered.


2️⃣ Encrypt Text

    Enter text in input box
    Click Encrypt Text
    Encrypted output appears below

3️⃣ Decrypt Text

    Paste encrypted text
    Click Decrypt Text
    Original message will appear

4️⃣ Encrypt File

    Click Encrypt File
    Select a file
    File will be encrypted

5️⃣ Decrypt File

    Click Decrypt File
    Select encrypted file
    File will be restored

📁 Project Structure
encryption-decryption-tool/
│
├── encryption_decryption_tool.py
├── secret.key (generated after key creation)
└── README.md


⚠️ Important Notes

    The tool overwrites files during encryption and decryption.
    Always keep a backup of important files.
    Do NOT share your secret.key file.
    If the key is lost, encrypted files cannot be recovered.

🔒 Security Considerations

    Uses industry-standard Fernet encryption
    Secure random key generation
    Error handling for invalid keys
    Safe exception management

💡 Future Improvements (Optional Ideas)

    Add password-based key generation
    Add drag & drop file support
    Add file backup before encryption
    Convert into executable (.exe)
    Add progress bar for large files
    Add key export/import system
    

📸 Preview

 GUI includes:
    Text input area
    Encrypt/Decrypt buttons
    File encryption section
    Key generation option
    Dark-themed modern interface


🤝 Contributing

Contributions are welcome!
   Fork the repository
   Create a new branch
   Commit your changes
   Submit a Pull Request
   

📜 License
   This project is open-source and available under the MIT License.

👨‍💻 Developer

Developed with ❤️ in Python.
