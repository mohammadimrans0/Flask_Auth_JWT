# 📝 Flask Auth API

A Flask Auth API Project with JWT authentication and authorization.

---

## 🚀 Features

- JWT-based authentication
- User registration and login
- Authenticated user can view their profile

---

## 🛠️ Tech Stack

- Python 3.x
- Flask
- Flask-JWT-Extended
- SQLite (default, easily swappable)

---

## ⚙️ Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/mohammadimrans0/Flask_Auth_JWT
cd Flask_Auth_JWT
```

### 2. Create a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # on Windows use: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Apply Migrations
```bash
# Initialize migrations folder (only needed once)
flask db init

# Generate migration script (based on model changes)
flask db migrate -m "Initial migration"

# Apply the migration to the database
flask db upgrade

```

### 5. Run the Development Server
```bash
python run.py
```

API will be available at: `http://localhost:5000/`

---

## 🔐 Authentication

This project uses JWT (JSON Web Tokens).


**Headers for Authenticated Requests:**
```http
Authorization: Bearer <your_access_token>
```

---

## 📬 API Endpoints

### 🔑 Auth

| Method | Endpoint                                | Description                  | Auth Required 
|--------|-----------------------------------------|------------------------------|--------------
| POST   | `http://localhost:5000/register/`       | Register a new user          | ❌            
| POST   | `http://localhost:5000/login/`          | Get JWT tokens (login)       | ❌            
| GET    | `http://localhost:5000/profile/`        | Get current user's profile   | ✅            


---

## ✅ Notes

- You can modify token expiration in your JWT configuration inside the Flask app.
- Feel free to swap SQLite with PostgreSQL or another DB engine.
- Make sure to configure `.env` or secret keys for production.
