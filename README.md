# Secure Password Manager 🔐

A simple password manager written in Python using cryptographic encryption (`cryptography.fernet`).

## ✨ Features

- 🔒 Save and encrypt account passwords securely
- 👁️ View and decrypt stored passwords
- 🛡️ Protect data with a strong encryption key

## 🔍 How it works

- 🔑 The password manager uses a unique encryption key stored in `key.key`
- 📁 Passwords are stored in an encrypted format inside `passwords.txt`
- 💻 You can either **add** new passwords or **view** existing ones through a simple command-line interface

## 🛠️ Setup Requirements

* 🐍 Python 3.x
* 📦 `cryptography` library

Install the required package:

```bash
pip install cryptography
```

## 🚀 Usage

1. 🔑 **Generate a key** (Uncomment the `write_key()` function in the code and run it once)
2. 🏃‍♂️ **Run the program** and choose whether you want to add or view passwords:

```bash
python password_manager.py
```

## 🔐 Security Notes

- ⚠️ The encryption key should be kept secure and not shared
- 💡 For additional security, consider storing the key file separately from the password file
- 🛡️ This manager uses Fernet symmetric encryption, which provides authenticated encryption

## ⚠️ Disclaimer

This is a beginner project and should not be used for highly sensitive data in production environments.

## 🔮 Future Improvements

- 🖥️ GUI interface
- 💪 Password strength checking
- 👥 Multiple user support
- 🎲 Automatic password generation
