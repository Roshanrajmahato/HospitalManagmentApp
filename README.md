# 🏥 Hospital Management System with Discharge Billing

A Django-based Hospital Management System that manages:

* Patient Profiles
* Doctor Management
* Treatment Records
* Lab Tests
* Technician Dashboard
* Discharge Billing System
* Automated Payment Calculation

This project includes a **fully automated discharge billing engine** with room-based pricing and dynamic calculations.

---

# 🚀 Features

## 👨‍⚕️ Patient Management

* Patient profile creation
* Address and contact details
* Profile image support
* Appointment history

## 🩺 Doctor Management

* Doctor registration
* Treatment linking
* Appointment handling

## 🧪 Lab Technician Module

* Technician login
* Add lab tests
* Upload lab results
* Edit test reports

## 💳 Payment & Discharge System

### Automated Billing Includes:

* Total Days Calculation (DOA → DOD)
* Room-based Charges
* Nursing Charges
* Doctor Charges
* Misc Charges
* Food Charges (Optional)
* Medicine Charges (10%)
* Grand Total Generation

---

# 🏨 Room Charges (Hardcoded)

| Room Type      | Bed  | Nursing | Doctor | Misc |
| -------------- | ---- | ------- | ------ | ---- |
| Common ward    | 250  | 300     | 250    | 100  |
| Semi-private   | 1000 | 1000    | 550    | 250  |
| Private AC     | 1500 | 1250    | 650    | 350  |
| Private Non-AC | 1250 | 1150    | 650    | 300  |
| Deluxe         | 2000 | 1500    | 850    | 500  |

Additional:

* Food Per Day = ₹480
* Medicine = 10% of Room Total

---

# 🧰 Tech Stack

* Python 3.x
* Django 5.x
* SQLite3
* HTML
* Bootstrap
* Crispy Forms
* Django ORM

---

# 📂 Project Structure

```
project_root/
│
├── doctors/
│
├── learnapp/
│
├── payment/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│
├── templates/
│   ├── create_discharge.html
│   ├── discharge_bill.html
│   ├── discharge_list.html
│
├── db.sqlite3
├── manage.py
```

---

# ⚙️ Installation Guide

## Step 1 — Clone Project

```bash
git clone <your-repo-url>
cd project-folder
```

---

## Step 2 — Create Virtual Environment

Windows:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Step 3 — Install Requirements

```bash
pip install django
pip install django-crispy-forms
pip install crispy-bootstrap5
```

(Optional)

```bash
pip install pillow
```

---

## Step 4 — Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## Step 5 — Create Superuser

```bash
python manage.py createsuperuser
```

Enter:

```
Username:
Email:
Password:
```

---

## Step 6 — Run Server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

# 💳 Discharge Billing Workflow

1. Open:

```
/payment/create-discharge/
```
# Lab Techcian Workflow

1. Open:

```
/labreports/register_lab_technician/
```

# 🔧 Common Commands

## Run Server

```bash
python manage.py runserver
```

## Create App

```bash
python manage.py startapp payment
```

## Make Migrations

```bash
python manage.py makemigrations
```

## Apply Migrations

```bash
python manage.py migrate
```

## Open Django Shell

```bash
python manage.py shell
```

---

# 🧠 Future Improvements

* Online Payment Integration
* PDF Bill Generation
* Email Bill System
* Dynamic Room Pricing from Admin
* Patient Discharge Reports
* Insurance Billing Support

---

# 👨‍💻 Author

**Roshan Raj Mahato**

Project Type:

```
Full Stack Django Hospital Management System
with Automated Billing Engine
```

---

# 📜 License

This project is for **educational and learning purposes**.
