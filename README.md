# Django Student Management System

A Django-based Student Management System that supports full CRUD operations, secure payment handling using atomic transactions, and API-level validations to maintain data integrity.

---

## Features

* Student Create, Read, Update, Delete (CRUD)
* Student payment management
* Atomic transactions for payment processing
* API-level validation
* Data integrity using Django transaction management
* SQLite database (db.sqlite3)
* Database inspection using SQLite Web Viewer
* Bootstrap-based UI

---

## Project Structure

```
STUDENT_MANAGE/
│
├── manage.py
├── db.sqlite3
│
├── std_manage/          # Main Django project folder
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   ├── wsgi.py
│
├── std/                 # Django application
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── tests.py
│
├── templates/           # HTML templates
│   └── (student pages)
│
└── venv/                # Virtual environment (not uploaded)
```

---

## Tech Stack

* Python
* Django
* SQLite
* Bootstrap
* HTML/CSS

---

## Setup Instructions

### 1. Clone the repository

```
git clone https://github.com/your-username/Django_Student_management.git
cd Django_Student_management
```

### 2. Create virtual environment

```
python -m venv venv
```

Activate it:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

---

### 3. Install dependencies

```
pip install django
```

(or if requirements.txt is added)

```
pip install -r requirements.txt
```

---

### 4. Apply migrations

```
python manage.py migrate
```

---

### 5. Run the server

```
python manage.py runserver
```

Open browser:

```
http://127.0.0.1:8000/
```

---

## Database

* Default Django SQLite database is used.
* File: `db.sqlite3`
* Data can be viewed using SQLite Web Viewer during development.

---

## Author

Developed as a Django learning project demonstrating CRUD operations, transaction handling, and backend data integrity.
