# 🚌 Smart Bus Tracking System

A web-based Smart Bus Tracking System built with **Django** that allows administrators, drivers, and students to track buses in real time. The system integrates GPS data from an ESP32 module to display the live location of buses and helps students monitor their assigned buses.

## 📌 Project Overview

The Smart Bus Tracking System is designed to improve transportation management for educational institutions. It enables administrators to manage buses, drivers, routes, and students while allowing students to view their assigned bus information and live bus location.

This project demonstrates full-stack web development using Django along with GPS-based vehicle tracking.

---

## ✨ Features

### 👨‍💼 Admin

- Secure admin login
- Manage buses
- Manage drivers
- Manage students
- Assign buses to drivers
- View live bus locations
- Dashboard with bus information

### 👨‍✈️ Driver

- Driver login
- Update current bus location
- View assigned route
- GPS location updates via ESP32

### 🎓 Student

- Student login
- View assigned bus
- Live bus location on map
- View driver information
- Track bus status

---

## 🚀 Planned Improvements

- ⏱ ETA (Estimated Time of Arrival)
- 📍 Route visualization
- 🔔 Arrival notifications
- 📱 Mobile-friendly dashboard
- 🟢 Live bus status (On Time / Delayed)
- 📊 Analytics Dashboard
- 📌 Multiple bus tracking
- 📈 Trip history

---

## 🛠 Tech Stack

### Backend

- Python
- Django

### Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript

### Database

- SQLite

### Maps

- Google Maps JavaScript API

*(Future enhancement: Leaflet + OpenStreetMap)*

### Hardware

- ESP32
- GPS Module

---

## 📂 Project Structure

```
Bus-Tracking-System/
│
├── custom_admin/
├── driver/
├── student/
├── esp32tracking/
├── store/
├── templates/
├── static/
├── media/
├── manage.py
└── requirements.txt
```

---

## 📸 Screenshots

### Admin Dashboard

![Admin Dashboard](screenshots/admin-dashboard.png)

### Student Dashboard

![Student Dashboard](screenshots/student-dashboard.png)

### Driver Dashboard

![Driver Dashboard](screenshots/driver-dashboard.png)

### Live Bus Tracking

![Live Tracking](screenshots/live-map.png)

> Add your screenshots inside a folder named `screenshots`.

---

## ⚙ Installation

### Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Smart-Bus-Tracking-System.git
```

### Navigate into the project

```bash
cd Smart-Bus-Tracking-System
```

### Create a virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Apply migrations

```bash
python manage.py migrate
```

### Run the server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📍 Future Scope

- Real-time ETA prediction
- AI-based traffic prediction
- Parent notification system
- RFID attendance integration
- Push notifications
- Android application
- Cloud deployment

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome.

Feel free to fork the repository and submit a pull request.

---

## 👩‍💻 Author

**Komalpreet**

GitHub: https://github.com/Komalpreet-kaur39

---

## ⭐ Show your support

If you found this project useful, please consider giving it a ⭐ on GitHub.
