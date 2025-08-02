# Salesforce-Inspired CRM Help Desk System

A lightweight, Flask-based CRM Help Desk web application that mimics key Salesforce CRM workflows like ticket creation, condition-based routing, and automated email notifications. This project demonstrates backend logic, automation, and process flows typically found in Salesforce Service Cloud.

### 🔗 Live Demo
[https://crm-helpdesk.onrender.com](https://crm-helpdesk.onrender.com)

---

## 📌 Features

- 🎫 Ticket creation with category, priority, and status
- 🧠 Controller-like logic simulating Salesforce Apex Triggers
- 📧 Automated email notifications (SMTP) when a ticket is created
- 🗃️ SQLite-based backend using SQLAlchemy ORM
- 🌐 Deployed live on Render
- 🧰 Modular, clean Flask architecture

---

## ⚙️ Tech Stack

- **Backend**: Flask, Flask-SQLAlchemy
- **Email Automation**: Python `smtplib` + Gmail SMTP
- **Deployment**: Render (Free Web Service)
- **Frontend**: HTML + Bootstrap
- **Version Control**: Git + GitHub
- **Other**: gunicorn, Jinja2, environment variables

---

## 🧩 Architecture Diagram

User → Web Form (/ticket/new)
↓
Flask App (app.py)
↓
Save to DB (SQLite via SQLAlchemy)
↓
Trigger: send_notification(ticket)
↓
Email Sent (SMTP)

## 🚀 Setup Locally

1. Clone the repo:
git clone https://github.com/mrbtk1802/crm-helpdesk.git
cd crm-helpdesk

3. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

4. Install dependencies:
pip install -r requirements.txt

5. Add Gmail App Password:
# utils.py
import os
password = os.environ.get('GMAIL_APP_PASSWORD')

5. Run locally:
flask run
