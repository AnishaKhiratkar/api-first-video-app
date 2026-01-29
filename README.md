# 🎥 Video Dashboard – Full Stack Assignment

## 📌 Project Overview

This is a **full-stack Video Dashboard application** developed as part of a software development internship assessment.

* **Backend:** Flask (Python) + MongoDB
* **Frontend:** React (Vite)
* **Database:** MongoDB

The application allows users to **add videos** and **view all uploaded videos** using REST APIs.

---

## 🛠️ Tech Stack

### Backend

* Python
* Flask
* Flask-CORS
* PyMongo
* MongoDB

### Frontend

* React (Vite)
* JavaScript (ES6)
* Axios
* HTML & CSS

---

## 📂 Project Structure

```
Software Development/
│
├── backend/
│   ├── app.py
│   ├── routes/
│   │   ├── dashboard.py
│   │   └── videos.py
│   ├── venv/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── main.jsx
│   │   └── App.css
│   ├── index.html
│   ├── package.json
│   └── vite.config.js
│
└── README.md
```

---

## 🚀 How to Run the Project

### 1️⃣ Backend Setup

```bash
cd backend
python app.py
```

Backend will start at:

```
http://127.0.0.1:5000
```

---

### 2️⃣ Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Frontend will start at:

```
http://localhost:5173
```

---

## 🔗 API Endpoints

### ➕ Add Video

```
POST /videos
```

**Request Body (JSON):**

```json
{
  "title": "Python Tutorial",
  "description": "Python basics for beginners",
  "thumbnail_url": "https://img.youtube.com/vi/dQw4w9WgXcQ/hqdefault.jpg"
}
```

---

### 📄 Get All Videos

```
GET /videos
```

---

### 🎯 Get Video by ID

```
GET /video/<video_id>
```

---

## ✅ Features

* Add new videos
* Fetch and display all videos
* MongoDB data persistence
* REST API integration
* CORS-enabled frontend-backend communication

---

## 🧪 Testing

* APIs tested using **Thunder Client**
* Frontend tested on browser
* MongoDB verified via **MongoDB Compass**

---

## 📸 Submission Proof

* Backend running logs
* Frontend UI screenshots
* MongoDB collection screenshots

---

## 👩‍💻 Developer

**Name:** Anisha Khiratkar
**Role:** Software Development Intern Applicant

---

## 🏁 Conclusion

This project demonstrates end-to-end full stack development including backend APIs, frontend integration, and database connectivity.

✔ Ready for submission
