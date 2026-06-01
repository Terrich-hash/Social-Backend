# Social Media Backend (FastAPI)

A production-ready social media backend built with FastAPI, PostgreSQL, SQLAlchemy, and JWT authentication.

This project demonstrates modern backend engineering practices including authentication, authorization, database relationships, social interactions, rate limiting, Docker containerization, and cloud deployment readiness.

---

## Features

### Authentication & Security

* JWT Authentication
* User Registration
* User Login
* Password Hashing with bcrypt
* Protected Routes
* Environment Variable Configuration

### Social Features

* Create Posts
* Like Posts
* Comment on Posts
* Follow Users
* Notification System
* User Feed

### Backend Features

* FastAPI REST API
* PostgreSQL Database
* SQLAlchemy ORM
* Pydantic Validation
* Rate Limiting
* Docker Support
* Cloud Deployment Ready
* Swagger Documentation

---

## Tech Stack

### Backend

* FastAPI
* Python 3.11+

### Database

* PostgreSQL (Neon)
* SQLAlchemy ORM

### Authentication

* JWT (python-jose)
* Passlib + bcrypt

### Deployment

* Docker
* Docker Compose
* Render
* Neon PostgreSQL

---

## Project Structure

```text
social-backend/
│
├── app/
│   ├── core/
│   │   ├── security.py
│   │   ├── exceptions.py
│   │   └── rate_limiter.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── post_routes.py
│   │   └── social_routes.py
│   │
│   ├── db.py
│   ├── models.py
│   ├── schemas.py
│   └── main.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Database Models

### User

* id
* username
* email
* password
* created_at

### Post

* id
* user_id
* image_url
* caption
* created_at

### Like

* id
* user_id
* post_id

### Comment

* id
* user_id
* post_id
* content

### Follow

* follower_id
* following_id

### Notification

* id
* user_id
* message
* is_read

---

## Environment Variables

Create a `.env` file:

```env
SECRET_KEY=your_secret_key_here

DATABASE_URL=postgresql://username:password@host/database?sslmode=require
```

---

## Local Setup

### Clone Repository

```bash
git clone git@github.com:Terrich-hash/Social-Backend.git

cd Social-Backend
```

### Create Virtual Environment

```bash
python -m venv venv

source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python -m uvicorn app.main:app --reload
```

---

## Docker Setup

### Build & Run

```bash
docker compose up --build
```

### Stop Containers

```bash
docker compose down
```

---

## API Documentation

After starting the server:

```text
http://localhost:8000/docs
```

Swagger UI provides interactive API testing.

---

## Authentication Flow

### Register

```http
POST /auth/register
```

### Login

```http
POST /auth/login
```

Response:

```json
{
  "access_token": "your_jwt_token"
}
```

### Authorize

Click the **Authorize** button in Swagger UI and paste:

```text
Bearer YOUR_JWT_TOKEN
```

---

## API Endpoints

### Auth

| Method | Endpoint       |
| ------ | -------------- |
| POST   | /auth/register |
| POST   | /auth/login    |

### Posts

| Method | Endpoint    |
| ------ | ----------- |
| POST   | /posts      |
| GET    | /posts/feed |

### Social

| Method | Endpoint                  |
| ------ | ------------------------- |
| POST   | /social/like/{post_id}    |
| POST   | /social/comment/{post_id} |
| POST   | /social/follow/{user_id}  |

---

## Deployment

### Backend

* Render

### Database

* Neon PostgreSQL

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

---

## Future Improvements

* Feed Ranking Algorithm
* User Profiles
* Search Functionality
* Redis Caching
* Alembic Migrations
* CI/CD Pipeline
* WebSocket Notifications
* Unit & Integration Tests

---

## Author

**Terrich**

Backend Engineer | FastAPI | PostgreSQL | Docker | Linux

GitHub:
https://github.com/Terrich-hash

---

## License

MIT License

---

If you found this project useful, consider giving it a ⭐ on GitHub.

