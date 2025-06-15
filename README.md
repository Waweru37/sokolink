# 🌾 SokoLink: AgriTech USSD Platform

**SokoLink** is a USSD-based solution that digitizes Kenya’s agricultural value chain, enabling farmers, buyers, and agents to connect, trade, and thrive — all through simple mobile interactions.

## 🚀 Features

- **Farmer Registration**
- **Post/View Produce Listings**
- **Market Search**
- **Agent Support**
- **SMS Notifications (optional)**

## 📱 Sample USSD Flow

```
Welcome to SokoLink!
1. Register
2. View/Post Products
3. Search for Produce
4. Agent Login
```

## 🛠️ Tech Stack

- **Django** + Django REST Framework
- **Africa's Talking USSD API**
- **SQLite (default) / MySQL (for production)**

## 🧪 Setup & Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/sokolink.git
cd sokolink/sokolink_backend
```

### 2. Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

*(Create a `requirements.txt` using `pip freeze > requirements.txt` once setup is done.)*

### 4. Run migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Visit your USSD callback endpoint at:
```
http://localhost:8000/ussd/
```

---

## ☁️ Deploying to Render

1. Push code to GitHub.
2. Go to [Render](https://render.com/), create a new Web Service.
3. Use this **start command**:

```bash
gunicorn sokolink_backend.wsgi
```

4. Set environment variable:
```
DJANGO_SETTINGS_MODULE=sokolink_backend.settings
```

5. Use **Africa’s Talking** dashboard to point USSD requests to:
```
https://<your-render-url>/ussd/
```

---

## 🤝 License

MIT — open for innovation and deployment in Africa 🌍
