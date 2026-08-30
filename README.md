
# 🌐 Shadowx-web-ss

> *Website Screenshot Generator - Capture any website instantly*

---

## ✨ Features

- 🚀 *Instant screenshots* - Just enter URL and click
- 📱 *Multiple sizes* - Default, Resized, Full Page, Custom
- 🎨 *Cool dark theme* - Low green cyberpunk style
- 📋 *History tracking* - See all your captures
- 🔌 *REST API* - Use it in your own apps
- ⚡ *Fast & reliable* - Powered by Thum.io

---

## 🛠️ Tech Stack

- **Backend** - Flask (Python)
- **Frontend** - HTML, CSS, JavaScript
- **Screenshot** - Thum.io API

---

## 📦 Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/eshitax/shadowx-web-ss.git
cd shadowx-web-ss
```

2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

3️⃣ Run the app

```bash
python app.py
```

4️⃣ Open browser

```
http://localhost:5000
```

---

🚀 Usage

Web Interface

1. Enter URL (e.g., https://github.com)
2. Choose size: Default | Resized | Full Page | Custom
3. Click CAPTURE or press Ctrl+Enter
4. View your screenshot instantly!

API Endpoints

Endpoint Description
/ss?url=URL&size=SIZE Capture screenshot
/api/history View history
/api/clear-history Clear history

API Examples

```bash
# Default size
/ss?url=https://github.com

# Resized (400x300)
/ss?url=https://python.org&size=resized

# Full page
/ss?url=https://example.com&size=full

# Custom size
/ss?url=https://google.com&size=custom&width=800&height=600
```

---

👨‍💻 Developers

Mueid Mursalin Rifat ✕ Eshita

📌 GitHub: @eshitax

---

📝 License

MIT License - Free to use and modify

---

🙏 Credits

· Screenshot API - Thum.io

---

<div align="center">

⭐ Star this repo if you like it!

Made with ❤️ by Mueid Mursalin Rifat & Eshita

</div>
```

