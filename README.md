# 🔐 Password Generator 

A **secure**, **simple**, and **clean** password generator built with Python and Tkinter.

Goal: quickly generate strong, reliable passwords compatible with most websites.

---

## ✨ Features

* 🔐 **Cryptographically secure** password generation (`secrets` module)
* ✔️ Guarantees **at least one character from each selected option**
* 🎚️ Custom password length (6 to 32 characters)
* 🔠 Configurable character sets:

  * Lowercase letters
  * Uppercase letters
  * Numbers
  * Safe symbols
* 📊 Visual **password strength indicator**
* 📋 Automatic copy to clipboard
* 🎨 Modern dark-mode interface

---

## 🧠 Security

This project **does NOT use `random`**.

It relies on Python’s `secrets` module, which is designed for:

* passwords
* tokens
* sensitive data

The symbol set is intentionally **restricted** to avoid characters commonly rejected by websites (such as spaces, backslashes, or quotes).

---

## 📦 Requirements

* Python **3.8+**
* No external dependencies

Tkinter is included by default with Python on Windows.

---

## ▶️ Run the application

```bash
python main.py
```

---

## 🖥️ User Interface

* Slider to control password length
* Checkboxes to select character types
* Generate button
* Read-only result field
* Color-coded strength bar:

  * 🔴 Weak
  * 🟡 Medium
  * 🟢 Strong

---

## 📊 Strength Calculation

Password strength is based on:

* total length
* number of character categories used

Simple scoring logic:

* +3 points per character
* +20 points per character type
* penalty if password length < 8

Final score is capped at 100.

---

## 🪟 Build a Windows .EXE

Install PyInstaller:

```bash
pip install pyinstaller
```

Create the executable:

```bash
pyinstaller --onefile --windowed main.py
```

The final `.exe` file will be located in the `dist/` folder.

---

## ⚠️ Warning

Windows Defender may show a security warning for unsigned executables.
This is normal for personal or unsigned projects.

---

## 🚀 Possible Improvements

* Light / dark theme toggle
* Ultra-secure mode (minimum 16 characters)
* Passphrase generation (Diceware-style)
* Encrypted local password history
* CustomTkinter UI

---

## 📄 License

Copyright © 2025 Taro

Free for personal and educational use.

You are free to modify, improve, and redistribute this project.

---

This project was created as a practical tool to generate clean, strong, and reliable passwords.



<img width="399" height="627" alt="image" src="https://github.com/user-attachments/assets/0884eeab-be18-4136-b908-7e4ed75bbfd6" />


<img width="405" height="604" alt="image" src="https://github.com/user-attachments/assets/fb769d0b-ea3b-4cba-bfc3-c0f3d2ab0e15" />





