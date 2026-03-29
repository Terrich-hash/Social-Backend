# Social Media Backend (FastAPI)

A scalable and modular backend for a social media platform built using FastAPI.
This project implements authentication, post management, social interactions, and a structured API architecture.

---

##  Features

*  JWT Authentication (Login / Register)
*  User Management
*  Create Posts (with image URLs)
*  Like System (with duplicate prevention)
*  Comment System
*  Follow / Unfollow Users
*  Notification System (basic)
*  Rate Limiting (optional)
*  API Documentation (Swagger UI)

---

## 🛠 Tech Stack

* **Backend Framework:** FastAPI
* **Database:** MySQL
* **ORM:** SQLAlchemy
* **Validation:** Pydantic
* **Authentication:** JWT (python-jose)
* **Password Hashing:** Passlib (bcrypt)

---

##  Project Structure

```
social-backend/
│
├── app/
│   ├── core/           # security, config, middleware
│   ├── routes/         # API routes
│   ├── models.py       # database models
│   ├── schemas.py      # request/response validation
│   ├── db.py           # database connection
│   └── main.py         # app entry point
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

##  Setup Instructions

### 1️. Clone Repository

```bash
git clone https://github.com/Terrich-hash/Social-Backend.git
cd Social-Backend
```

---

### 2️. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
```

---

### 3️. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️. Setup Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key
DATABASE_URL=mysql+pymysql://username:password@localhost:3306/social_db
```

---

### 5️. Run Server

```bash
python -m uvicorn app.main:app --reload
```

---

## 📌 API Documentation

Once server is running:

👉 http://127.0.0.1:8000/docs

---

## 🔑 Authentication Flow

1. Register user
2. Login → get JWT token
3. Click **Authorize 🔒** in Swagger
4. Enter:

```
YOUR_TOKEN
```

---

## 📡 Sample Endpoints

| Method | Endpoint           | Description   |
| ------ | ------------------ | ------------- |
| POST   | /auth/register     | Register user |
| POST   | /auth/login        | Login         |
| POST   | /posts/            | Create post   |
| POST   | /like/{post_id}    | Like post     |
| POST   | /comment/{post_id} | Comment       |
| POST   | /follow/{user_id}  | Follow user   |

---

## ⚠️ Important Notes

* `.env` is ignored for security
* Passwords are hashed using bcrypt
* MySQL requires string lengths (handled in models)

---

## 🚀 Future Improvements

* Feed algorithm (posts from followed users)
* Notifications system enhancement
* Image upload integration (Cloudinary)
* Pagination & optimization
* Deployment (Docker + Cloud)

---

##  Author

Built by **Terrich**
Backend Developer | FastAPI | Systems

---

##  If you found this useful

Give it a ⭐ on GitHub!
