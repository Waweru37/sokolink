# 🌾 SokoLink — Empowering Farmers Through USSD AgriTech

**SokoLink** is a simple yet powerful USSD platform that connects small-scale Kenyan farmers to the digital marketplace — no smartphone required.

---

## 🚀 Features

- 📱 USSD-based interface (works on all phones)
- 👨‍🌾 Farmer registration & verification
- 📦 Post and view produce listings
- 🔍 Real-time market search
- 🔒 Secure data flow, lightweight design
- 🌍 Built for rural-first accessibility

---

## 🧠 Tech Stack

| Layer         | Stack                                |
|---------------|---------------------------------------|
| Backend       | Django (Python)                      |
| USSD Gateway  | Africa’s Talking                     |
| Database      | SQLite (Local) / MySQL (Prod Ready)  |
| Hosting       | Render / Heroku / VPS                |

---

## 💻 Local Development

### ⚙️ Prerequisites

- Python 3.9+
- pip
- virtualenv (optional but recommended)

### 🛠 Setup Instructions

```bash
# Clone the repo
git clone https://github.com/YOUR_USERNAME/sokolink.git
cd sokolink/sokolink_backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py makemigrations
python manage.py migrate

# Start development server
python manage.py runserver
```

---

## 🧪 Test the USSD Flow

Simulate requests using `curl`:

```bash
curl -X POST http://127.0.0.1:8000/ussd/   -d "sessionId=12345"   -d "serviceCode=*384#"   -d "phoneNumber=+254712345678"   -d "text="
```

→ You’ll get a response like:

```
CON Welcome to SokoLink!
1. Register
2. View/Post Products
3. Search Market
```

---

## 🌍 Deployment

### Deploy to [Render](https://render.com/)

1. Push code to GitHub
2. Create a new Web Service on Render
3. Set:
   - Build command: `pip install -r requirements.txt`
   - Start command: `gunicorn sokolink_backend.wsgi`
   - Environment variable: `DJANGO_SETTINGS_MODULE=sokolink_backend.settings`
4. Point your Africa's Talking USSD sandbox to:  
   `https://your-app-name.onrender.com/ussd/`

---

## 🧠 Next Features (Planned)

- Voice support for non-literate farmers (IVR)
- Geo-filtered market searches
- Agent dashboard & leaderboard
- Integration with Mpesa & co-ops

---

## 🤝 Contributing

PRs are welcome. Let’s build inclusive African tech!

---

## 📜 License

MIT — free to use, expand, remix, deploy.

> Empower farmers. Strengthen communities. One line of USSD at a time.