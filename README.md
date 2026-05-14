# AI Finance Credit Follow-Up Agent

An AI-powered finance workflow automation platform that helps businesses manage overdue invoices, generate intelligent payment reminder emails, track communication history, and visualize invoice analytics.

This project combines:

* React frontend
* FastAPI backend
* Google Gemini AI integration
* SQLite database
* SMTP email service
* Analytics dashboard

---

# Features

## Core Features

* Upload invoice CSV files
* Automatic overdue detection
* AI-generated payment reminder emails
* Dynamic follow-up stages
* Real email sending using SMTP
* Audit log tracking
* Invoice analytics dashboard
* Charts and visual reports
* Human-in-the-loop workflow

---

# AI Features

The system uses Google Gemini AI to:

* Generate personalized reminder emails
* Adjust tone based on overdue severity
* Create professional payment follow-ups
* Produce structured email responses

### Follow-Up Escalation Stages

| Stage               | Tone                     |
| ------------------- | ------------------------ |
| Stage 1 - Warm      | Friendly reminder        |
| Stage 2 - Polite    | Polite but firm          |
| Stage 3 - Formal    | Professional and serious |
| Stage 4 - Stern     | Urgent payment reminder  |
| Escalation Required | Escalation notice        |

---

# Tech Stack

## Frontend

* React
* Tailwind CSS
* Axios
* Recharts
* Vite

## Backend

* FastAPI
* SQLAlchemy
* SQLite
* Pandas
* Python Dotenv

## AI Integration

* Google Gemini API

## Email Service

* Gmail SMTP

## Deployment

* Vercel (Frontend)
* Render (Backend)

---

# Project Architecture

```text
React Frontend
       ↓
FastAPI Backend
       ↓
Gemini AI Engine
       ↓
SQLite Database
       ↓
SMTP Email Service
```

---

# Folder Structure

```text
finance-credit-agent/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   ├── models/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── database.py
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── requirements.txt
│   ├── .env
│   └── finance_agent.db
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── index.css
│   │
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

# Setup Instructions

## 1. Clone Repository

```bash
git clone YOUR_GITHUB_REPO_URL

cd finance-credit-agent
```

---

# Backend Setup

## 2. Create Virtual Environment

```bash
cd backend

python -m venv venv
```

Activate virtual environment:

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## 3. Install Backend Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Create .env File

Create:

```text
backend/.env
```

Add:

```env
GEMINI_API_KEY=your_gemini_api_key

EMAIL_ADDRESS=your_email@gmail.com

EMAIL_PASSWORD=your_gmail_app_password
```

---

## 5. Run Backend Server

```bash
uvicorn app.main:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Frontend Setup

## 6. Install Frontend Dependencies

Open new terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Install chart library:

```bash
npm install recharts
```

---

## 7. Run Frontend

```bash
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

# CSV Format

Upload CSV files with the following structure:

```csv
invoice_no,client_name,amount,due_date,email
INV-1001,Rajesh Kumar,12000,2024-05-01,rajesh@gmail.com
INV-1002,Priya Sharma,25000,2024-04-20,priya@gmail.com
```

---

# API Endpoints

| Method | Endpoint             | Description         |
| ------ | -------------------- | ------------------- |
| POST   | /upload-csv          | Upload invoice CSV  |
| GET    | /invoices            | Fetch all invoices  |
| GET    | /generate-email/{id} | Generate AI email   |
| POST   | /send-email/{id}     | Send email          |
| GET    | /audit-logs          | Fetch audit logs    |
| GET    | /analytics           | Dashboard analytics |
| GET    | /health              | Health check        |

---

# Dashboard Features

The dashboard includes:

* Invoice analytics cards
* Pie chart visualization
* Bar chart analytics
* Invoice table
* AI email preview
* Audit log table
* CSV upload system

---

# Email Workflow

```text
Upload CSV
      ↓
Invoices Stored
      ↓
Generate AI Email
      ↓
Preview Email
      ↓
Send Email
      ↓
Audit Log Created
      ↓
Dashboard Updated
```

---

# Security Features

* Environment variable protection
* Backend-only API key usage
* SMTP app password authentication
* Structured AI outputs
* Audit logging

---

# Deployment

## Frontend Deployment

Deploy frontend on Vercel.

## Backend Deployment

Deploy backend on Render.

---

# Render Backend Deployment

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port 10000
```

---

# Vercel Frontend Deployment

Set:

| Setting          | Value         |
| ---------------- | ------------- |
| Framework        | Vite          |
| Root Directory   | frontend      |
| Build Command    | npm run build |
| Output Directory | dist          |

---

# Screenshots

Add screenshots here:

* Dashboard
* AI Email Preview
* Charts
* Audit Logs
* CSV Upload

---

# Future Improvements

Possible future enhancements:

* JWT authentication
* PostgreSQL integration
* Redis queue system
* APScheduler automation
* PDF report generation
* Multi-user access
* Role-based permissions
* Docker support
* Kubernetes deployment

---

# Learning Outcomes

This project demonstrates:

* Full-stack development
* AI integration
* Prompt engineering
* FastAPI backend architecture
* React frontend development
* Database design
* API development
* SMTP email integration
* Data visualization
* Production deployment

---

# Author

```text
Name: YOUR_NAME
College: YOUR_COLLEGE
Role: Full Stack + AI Developer
```

---

# License

This project is for educational and internship demonstration purposes.
