🔐 Advanced Password Encryption & Decryption Tool

A production-style Python security tool that demonstrates secure password encryption, hashing, and cryptographic best practices used in real-world authentication systems.

📌 About The Project

This project is built to demonstrate:

     Secure password encryption using industry-standard cryptography

     Secure password hashing using strong hashing algorithms

     Key generation and management concepts

     Defensive security programming practices

The tool is designed for educational, cybersecurity training, and portfolio purposes.

🚀 Features
🔐 Encryption Module

    AES-based symmetric encryption (Fernet)
    Secure key generation
    Base64 encoded ciphertext
    Safe decryption process

🔑 Hashing Module

    Secure password hashing using bcrypt
    Automatic salting
    Secure password verification
    Resistant to brute-force attacks

🛡 Security-Focused Design

    No plain-text password storage
    Modular architecture
    Proper error handling
    Clean CLI interface

🧠 Security Concepts Demonstrated

    Symmetric Encryption (AES)
    Hashing vs Encryption
    Salting
    Secure Key Management
    Credential Protection  
    Authentication Security Principles

📂 Project Structure
password-crypto-tool/
│
├── main.py
├── encryption.py
├── hashing.py
├── key_manager.py
└── README.md


⚙️ Installation
   1️⃣ Clone Repository
       git clone https://github.com/Haackerspot/encryption_decryption_too)/
       cd password-crypto-tool
       
   2️⃣ Install Dependencies
       pip install cryptography bcrypt
       
   3️⃣ Run Application
       python main.py
       
📊 Example Output
    Encryption
    Enter password to encrypt: SecurePass@123
    Encrypted Password: gAAAAABmX...
Hashing
    Enter password to hash: SecurePass@123
    Hashed Output: $2b$12$...
    password Verified Successfully

    
🔍 Encryption vs Hashing
      Purpose	                        Recommended Method
      
      Secure data storage (reversible)	Encryption
      Password authentication	        Hashing
      Database credential storage	    Hashing (bcrypt)
      Secure communication              Encryption

      
🛡 Security Best Practices Followed

    Uses trusted cryptographic libraries
    Avoids custom cryptographic algorithms
    Strong hashing (bcrypt)
    No hardcoded secrets (recommended practice)
    Clear separation of encryption and hashing logic

⚠ Important Security Notes

    Never expose encryption keys publicly.
    Do not hardcode keys in production.
    Use environment variables or secure vaults for key storage.
    For enterprise systems, use HSM or managed key services.
    
📈 Future Improvements

    Add Argon2 hashing
    Implement RSA (asymmetric encryption)
    Add GUI interface
    Create REST API version
    Integrate database support
    Docker deployment
    Add automated security tests

🎯 Ideal For

    Cybersecurity students
    Ethical hacking beginners
    Python security developers
    Internship portfolios
    Final-year projects
