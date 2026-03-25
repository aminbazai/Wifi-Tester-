<div align="center">

# 🔐 WiFi Tester

```text
 ██████╗██╗      █████╗ ████████╗ ██████╗ ██████╗ ██╗   ██╗
██╔════╝██║     ██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
██║     ██║     ███████║   ██║   ██║   ██║██████╔╝ ╚████╔╝ 
██║     ██║     ██╔══██║   ██║   ██║   ██║██╔══██╗  ╚██╔╝  
╚██████╗███████╗██║  ██║   ██║   ╚██████╔╝██║  ██║   ██║   
 ╚═════╝╚══════╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   
```

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Platform](https://img.shields.io/badge/Platform-Windows-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)](https://www.microsoft.com/windows/)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/aminbazai/Wifi-Tester?style=for-the-badge)](https://github.com/aminbazai/Wifi-Tester/stargazers)

---

### A Python-based WiFi Tester tool that demonstrates dictionary-based password attacks for educational purposes.

</div>

---

## 📋 About

This project is created for **educational purposes** to help students understand basic cybersecurity concepts and password security. It demonstrates how dictionary-based password attacks work and the importance of using strong passwords.

---

## 👤 Author

**Muhummad Amin Khan**

Cybersecurity learner and content creator focused on ethical hacking and security awareness.

---

## 🛠️ Features

| Feature | Description |
|---------|-------------|
| 🔓 Dictionary Attack | Demonstrates the concept of password dictionary attacks |
| 📖 Educational | Learn about WiFi security vulnerabilities |
| 💻 Python Based | Simple Python implementation |
| ⌨️ CLI Based | Command line based tool |
| 🛡️ Safety First | Built-in attempt limits to prevent abuse |
| 🪟 Windows Only | Uses Windows netsh command |

---

## ⚠️ Disclaimer

> **This tool is for EDUCATIONAL PURPOSES only!**
> 
> - Use ONLY on networks you OWN
> - Use ONLY with explicit permission
> - The author is NOT responsible for any misuse
> - Unauthorized access is illegal and punishable by law

---

## 📦 Requirements

Before running the script, make sure you have the following installed:

- **Python 3** - [Download](https://www.python.org/downloads/)
- **Windows Operating System** - Windows 10/11
- **Active WiFi Adapter** - Internal or external
- **Wordlist File** - e.g., `rockyou.txt`

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Hasnain-Dark-Net/Wifi-Tester.git
```

### 2. Navigate to the project folder

```bash
cd Wifi-Tester
```

### 3. No additional dependencies needed!

---

## 📖 Usage

### Run the tool

```bash
python wifi.py
```

### Follow the prompts

```
1. Type "I HAVE PERMISSION" to confirm
2. Enter the target WiFi SSID (name)
3. Enter the wordlist file path
4. Set delay per attempt (recommended: 6-8 seconds)
```

The tool will attempt passwords from your wordlist until it finds a match or reaches the limit.

---

## 📂 Project Structure

```
Wifi-Tester/
├── wifi.py           # Main Python script
├── passwords.txt     # Sample password list
├── README.md         # This file
└── LICENSE           # MIT License
```

---

## 🔧 Configuration

You can modify these settings in `wifi.py`:

| Variable | Default | Description |
|----------|---------|-------------|
| `MAX_ATTEMPTS` | 50 | Maximum password attempts |

---

## 📝 Security Best Practices

This tool helps you understand:

- ✅ Why weak passwords are dangerous
- ✅ How dictionary attacks work
- ✅ Importance of strong, unique passwords
- ✅ Network security fundamentals

---

## 📜 License

This project is licensed under the **MIT License**.

---

<div align="center">

⭐ **Don't forget to star this repository if you found it useful!**

Made with ❤️ for educational purposes

</div>
