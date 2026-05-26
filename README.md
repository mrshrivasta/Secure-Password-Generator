# 🔐 Secure Password Generator

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-Web%20UI-black?style=for-the-badge&logo=flask)
![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Secure-green?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-CSPRNG-red?style=for-the-badge)
![CLI](https://img.shields.io/badge/CLI-Supported-success?style=for-the-badge)
![Open Source](https://img.shields.io/badge/Open%20Source-GitHub-181717?style=for-the-badge&logo=github)

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=24&pause=1000&color=1A6FD4&center=true&vCenter=true&width=1000&lines=Secure+Password+Generator;Cryptographically+Secure+Passwords;Python+%2B+Flask+Cybersecurity+Project;Entropy+Calculator+%2B+Crack+Time+Estimator;Modern+Password+Generator+Dashboard" />

### ⚡ Advanced Secure Password Generator Built With Python + Flask

### 🔥 CSPRNG • Entropy Calculator • Crack-Time Estimator • Web Dashboard

</div>

---

# 📌 Overview

Secure Password Generator is a modern cybersecurity-focused password generation utility built using:

- Python
- Flask
- secrets module
- cryptographic randomness
- entropy mathematics

The project provides both:

✅ CLI mode  
✅ Web dashboard mode  

with advanced security features such as:

- cryptographically secure password generation
- Fisher–Yates shuffle
- entropy calculation
- brute-force crack-time estimation
- customizable character pools
- strength classification system

---

# 🚀 Features

# 🔐 Cryptographically Secure Passwords

Uses Python's:

```python
secrets
```

module instead of insecure pseudo-random generators.

This ensures:

✅ OS-level cryptographic randomness  
✅ unpredictable passwords  
✅ secure token generation  
✅ authentication-grade randomness  

---

# ⚡ Web Dashboard

- Modern Flask web interface
- Real-time password generation
- Live entropy calculation
- Crack-time estimation
- Responsive UI
- Smooth animations
- Copy-to-clipboard support

---

# 🖥️ CLI Support

Generate passwords directly from terminal:

```bash
python password_generator.py
```

---

# 🧠 Entropy Calculator

Real entropy formula:

```text
Entropy = log₂(pool_size) × password_length
```

Provides:

- realistic entropy calculations
- password strength evaluation
- brute-force resistance estimates

---

# 🔥 Crack-Time Estimator

Estimates cracking difficulty assuming:

```text
1 trillion guesses/second
```

Displays estimates such as:

- minutes
- years
- millions of years
- effectively uncrackable

---

# 🎲 Fisher–Yates Shuffle

Implements:

```text
Fisher–Yates shuffle
```

to eliminate positional bias.

Benefits:

✅ stronger randomness distribution  
✅ less predictable character placement  
✅ improved entropy quality  

---

# 📊 Password Strength Classification

| Entropy | Strength |
|---|---|
| < 40 | Weak |
| 40–60 | Fair |
| 60–80 | Strong |
| 80–120 | Very Strong |
| 120+ | Unbreakable |

---

# 🔧 Password Customization

Supports:

- uppercase letters
- lowercase letters
- digits
- symbols
- extra symbols
- custom lengths
- bulk generation

---

# 🌐 Web Dashboard Features

# 🎨 UI Features

- Modern responsive design
- Live updates
- Animated strength bar
- Real-time calculations
- Mobile-friendly interface
- Interactive controls
- Cybersecurity-inspired styling

---

# 📊 Dashboard Metrics

- entropy bits
- pool size
- crack-time estimate
- password strength
- real-time updates

---

# 📋 Copy Features

- One-click copy
- Clipboard API support
- Instant copy confirmation

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend |
| Flask | Web server |
| secrets | Cryptographic randomness |
| math | Entropy calculations |
| argparse | CLI parsing |
| HTML5 | Frontend |
| CSS3 | Styling |
| JavaScript | Live UI updates |

---

# 📥 Installation Guide

# 🐍 Step 1 — Install Python

Download Python:

🔗 https://www.python.org/downloads/

### IMPORTANT

During installation:

✅ Enable:

```txt
Add Python to PATH
```

---

# 📦 Step 2 — Install Flask

Open:

```txt
Command Prompt
```

Run:

```bash
pip install flask
```

---

# 📂 Step 3 — Clone Repository

```bash
git clone https://github.com/mrshrivasta/Secure-Password-Generator.git
```

---

# 📁 Step 4 — Open Folder

```bash
cd Secure-Password-Generator
```

---

# 🚀 Step 5 — Run CLI Mode

```bash
python password_generator.py
```

---

# 🌐 Step 6 — Run Web Dashboard

```bash
python password_generator.py --web
```

---

# 🌍 Step 7 — Open Browser

Open:

```txt
http://localhost:5000
```

---

# ⚡ Quick Start

```bash
pip install flask
python password_generator.py --web
```

---

# 🖥️ CLI Usage

# Basic Generation

```bash
python password_generator.py
```

---

# Generate Multiple Passwords

```bash
python password_generator.py --length 64 --count 10
```

---

# Disable Symbols

```bash
python password_generator.py --no-symbols
```

---

# Enable Extra Symbols

```bash
python password_generator.py --extra
```

---

# Full Example

```bash
python password_generator.py --length 48 --count 5 --extra
```

---

# 🔒 Security Architecture

# 🧠 Why `secrets` Module?

Unlike:

```python
random
```

Python's:

```python
secrets
```

module provides:

✅ cryptographic randomness  
✅ OS-level secure entropy  
✅ unpredictable generation  
✅ security-grade random values  

---

# 🎲 Fisher–Yates Shuffle

The project uses Fisher–Yates shuffling for:

- unbiased randomization
- better entropy spread
- stronger randomness distribution

---

# 🔥 Guaranteed Character Coverage

The generator guarantees inclusion of enabled character classes:

- uppercase
- lowercase
- digits
- symbols

This prevents weak accidental outputs.

---

# 📊 Entropy Mathematics

Formula used:

```text
Entropy = log₂(pool_size) × password_length
```

Example:

```text
Pool Size: 94
Length: 32
Entropy ≈ 209 bits
```

---

# ⚡ Crack-Time Estimation

Assumption:

```text
1 trillion guesses/sec
```

Displays realistic attack resistance estimates.

---

# 🌐 SEO Keywords

Secure Password Generator, Python Password Generator, Flask Password Generator, Cryptographically Secure Password Generator, Entropy Calculator, Password Strength Checker, Password Generator Python Project, Cybersecurity Python Project, CSPRNG Password Generator, Fisher Yates Shuffle Password Generator, GPU Crack Time Estimator, Secure Password Utility

---

# 📂 Project Structure

```txt
password_generator.py
README.md
```

---

# ⚡ Why This Project?

Most beginner projects are:

- calculator
- to-do app
- weather app

This project demonstrates:

✅ cybersecurity concepts  
✅ cryptographic randomness  
✅ entropy calculations  
✅ Flask development  
✅ CLI engineering  
✅ password security principles  
✅ modern dashboard design  
✅ secure generation systems  

---

# 📜 API Features

The web dashboard dynamically generates passwords using Flask API endpoints. :contentReference[oaicite:0]{index=0}

---

# 🔥 Example Output

```txt
Length     : 32 characters
Pool size  : 94 characters
Entropy    : 209.7 bits
Strength   : Unbreakable
Crack time : ∞ (effectively uncrackable)
```

---

# ⚠ Disclaimer

```txt
This project is for educational and defensive security purposes only.

Do not rely solely on generated passwords without:
- MFA
- secure storage
- password managers
- proper security practices
```

---

# 🔒 Security Recommendations

Always use:

✅ MFA  
✅ unique passwords  
✅ password managers  
✅ secure authentication systems  

Never:

❌ reuse passwords  
❌ share credentials  
❌ store passwords in plaintext  

---

# 🛠️ Troubleshooting

# ❌ pip not recognized

Run:

```bash
python -m pip install flask
```

---

# ❌ Python not recognized

Reinstall Python and enable:

```txt
Add Python to PATH
```

---

# ❌ Flask module not found

Run:

```bash
pip install flask
```

---

# ❌ Port 5000 already in use

Change:

```python
app.run(port=5000)
```

to:

```python
app.run(port=5050)
```

---

# 📈 Performance Notes

- Lightweight backend
- Fast password generation
- Real-time UI updates
- Minimal memory usage
- Efficient entropy calculations

---

# 🧠 Learning Concepts

This project helps learn:

- cryptographic randomness
- entropy mathematics
- Flask development
- password security
- secure authentication
- UI engineering
- CLI application development

---

# 🚀 Future Improvements

- password history
- dark mode
- API key generation
- token generation
- QR export
- password manager integration
- offline desktop app
- Docker support

---

# 🤝 Contributing

Pull requests are welcome.

Steps:

1. Fork repository
2. Create branch
3. Commit changes
4. Push updates
5. Open pull request

---

# ⭐ Support

If you like this project:

⭐ Star the repository  
🍴 Fork the repository  
📢 Share the project  

---

# 👨‍💻 Author

# Karanam Shrivasta

### 🌐 GitHub

:contentReference[oaicite:1]{index=1}

### 💼 LinkedIn

:contentReference[oaicite:2]{index=2}

---

# 📜 License

MIT License

---

# 🔥 Fun Fact

This advanced password generation system runs from:

```txt
One Python file.
```

---

<div align="center">

# 🔐 Secure Password Generator

### ⚡ Cryptographically Secure Password Utility

### 🚀 Built With Python + Flask

<img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=20&pause=1000&color=1A6FD4&center=true&vCenter=true&width=900&lines=Made+By+Karanam+Shrivasta;Cybersecurity+Inspired+Project;Secure+Password+Generator;Python+%2B+Flask+Application" />

</div>
