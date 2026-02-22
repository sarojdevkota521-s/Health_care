# Healthcare Backend System

##  Overview

This project is a Healthcare Backend System built using **Django**, **Django REST Framework (DRF)**, and **PostgreSQL**.  
It provides secure JWT-based authentication and RESTful APIs to manage:

- User registration and login
- Patient records
- Doctor records
- Patient–Doctor mappings

The system ensures that authenticated users can only access and manage their own patient data.

---

##  Tech Stack

- Python
- Django
- Django REST Framework (DRF)
- PostgreSQL
- JWT Authentication (`djangorestframework-simplejwt`)
- psycopg2 (PostgreSQL driver)

---

##  Features

- Custom User Model (Email-based authentication)
- JWT Authentication
- CRUD APIs for Patients
- CRUD APIs for Doctors
- Patient–Doctor Mapping
- Secure access control
- PostgreSQL database integration
- Environment variable configuration

---

##  Project Structure

* healthcare
    * accounts(Custom user and authentication) 
    * core 
        * Patients
        * Doctors
        * Mappings
    * healthcare(Project settings) 
* manage.py
* README.md
* requirements.txt

---

##  Setup Instructions

### 1. Clone Repository

```bash
git clone <repository-url>
cd Health_care bash 
```

### 2. Clone Repository

```bash
git clone <repository-url>
cd Health_care
```
### 3. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3. Install Dependencies

```bash
pip install -r requirements.txt
```
### 3. PostgreSQL Configuration
Create PostgreSQL database:

```bash
CREATE DATABASE healthcare_db;
```
Update settings.py:
```bash
from decouple import config

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}
```
### 3. Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```
Create superuser
```bash
python manage.py createsuperuser
```
### 3. Run Server

```bash
python manage.py runserver

```
---
##  Authentication APIs

Authentication APIs are as  ***same as the Task***
