# 🔐 Password Generator — Advanced Secure Password Utility

A blazing-fast, security-focused password generator built with Python. Supports both CLI and Web UI modes with cryptographically secure password generation, entropy calculation, brute-force crack-time estimation, and advanced randomness protection.

---

## 🚀 Features

- ✅ Cryptographically Secure Passwords (`secrets` module)
- ✅ CLI + Flask Web Interface
- ✅ Fisher–Yates Shuffle (eliminates positional bias)
- ✅ Entropy Calculator (`log₂(pool_size) × length`)
- ✅ GPU-Level Crack-Time Estimator
- ✅ Character Class Guarantees
- ✅ Ultra-fast Password Generation
- ✅ Custom Length & Bulk Generation
- ✅ Extra Symbols Mode
- ✅ Strength Classification System

---

## 🖥️ Demo Modes

### 1️⃣ CLI Mode

Run directly from terminal:

```bash
python password_generator.py
```

Generate 10 passwords of length 64:

```bash
python password_generator.py --length 64 --count 10
```

Disable symbols:

```bash
python password_generator.py --no-symbols
```

Enable extra symbols:

```bash
python password_generator.py --extra
```

---

### 2️⃣ Web Mode (Flask UI)

Install Flask:

```bash
pip install flask
```

Start the web server:

```bash
python password_generator.py --web
```

Open in browser:

```bash
http://localhost:5000
```

---

# 🔒 Security Architecture

## Cryptographically Secure Randomness

Uses Python’s built-in `secrets` module instead of `random`.

### Why?

- `random` is predictable
- `secrets` uses OS-level CSPRNG
- Suitable for:
  - Passwords
  - Tokens
  - API keys
  - Authentication systems

---

## Fisher–Yates Shuffle

Passwords are shuffled using the Fisher–Yates algorithm to eliminate positional bias.

### Benefits

- Prevents predictable character placement
- Improves entropy distribution
- Makes brute-force attacks harder

---

## Guaranteed Character Coverage

Ensures at least one character from every enabled category:

- Uppercase
- Lowercase
- Digits
- Symbols
- Extra Symbols (optional)

This prevents weak accidental generations.

---

# 📊 Entropy Calculation

Real entropy formula used:

```text
Entropy = log₂(character_pool_size) × password_length
```

### Example

- Pool Size: 94
- Length: 32

Entropy ≈ 209 bits

---

# ⚡ Crack-Time Estimation

Estimates brute-force crack time assuming:

```text
1 trillion guesses / second
```

(GPU cluster-level attack speed)

Displays realistic estimates like:

- Seconds
- Years
- Millions of years
- Heat death of universe 😅

---

# 🧠 Password Strength Tiers

| Entropy | Strength |
|---|---|
| < 40 | Weak |
| 40–60 | Fair |
| 60–80 | Strong |
| 80–120 | Very Strong |
| 120+ | Unbreakable |

---

# 📂 Project Structure

```text
password_generator.py
README.md
```

---

# 🛠️ Tech Stack

- Python 3
- Flask
- secrets
- math
- argparse

---

# 📦 Installation

Clone the repository:

```bash
git clone https://github.com/mrshrivasta/password-generator.git
```

Move into project folder:

```bash
cd password-generator
```

Run:

```bash
python password_generator.py
```

---

# 🌐 Use Cases

- Cybersecurity Projects
- Authentication Systems
- API Key Generation
- Secure Vault Applications
- Password Managers
- Penetration Testing Labs
- Ethical Hacking Practice

---

# 📈 SEO Keywords

Password Generator Python, Secure Password Generator, Flask Password Generator, Python Cybersecurity Project, Random Password Tool, Secure Password CLI, Password Entropy Calculator, Fisher Yates Shuffle Password Generator, GPU Crack Time Estimator, Cybersecurity Python Project

---

# 👨‍💻 Author

## Karanam Shrivasta

- GitHub: https://github.com/mrshrivasta
- LinkedIn: https://www.linkedin.com/in/karanam-shrivasta/

---

# ⭐ Support

If you like this project:

- ⭐ Star the repository
- 🍴 Fork the project
- 🔗 Share with developers & cybersecurity enthusiasts

---

# 📜 License

MIT License — free to use, modify, and distribute.