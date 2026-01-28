# Django Blog Application

A comprehensive **Django-based blog application** built as a complete learning and production-ready project.  
The project covers core Django fundamentals, advanced features, database integration with PostgreSQL, and SEO best practices.

This application demonstrates how to build a real-world Django blog from scratch — from project setup to advanced querying and search.

---

## 🚀 Features Overview

### 📝 Blog Functionality
- Create, publish, and manage blog posts
- SEO-friendly URLs for posts
- Canonical URLs for models
- Pagination for the post list view
- Tagging system using `django-taggit`
- Retrieve similar posts based on shared tags
- Comment system using model-based Django forms
- Share posts via email using Django forms
- Email sending via Django’s email framework

---

### 🔍 Advanced Content & SEO
- Sitemap generation for search engines
- RSS/Atom feeds for blog posts
- Full-text search using **Django + PostgreSQL**
- Custom template tags and filters:
  - Latest posts
  - Most commented posts

---

### 🗄 Database & Data Management
- PostgreSQL database integration
- Dockerized PostgreSQL setup
- Data export and import using fixtures (`dumpdata` / `loaddata`)
- Custom model managers and QuerySets
- Efficient querying and indexing

---

### 🧱 Architecture & Django Concepts Covered

This project covers **both fundamentals and advanced Django concepts**, including:

#### Django Fundamentals
- Installing Python
- Creating and managing virtual environments
- Installing and configuring Django
- Creating a Django project and applications
- Designing data models
- Creating and applying migrations
- Django admin site customization
- Understanding the Django request/response cycle
- URL routing and view handling
- Working with templates and context

#### Advanced Django
- Class-Based Views (CBVs)
- Function-Based Views (FBVs)
- Custom model managers
- QuerySet optimization
- Django forms and model forms
- Custom template tags and filters
- Email handling with Django
- PostgreSQL-specific features
- SEO and performance best practices

---

## 🛠 Tech Stack

- **Python 3.12**
- **Django 5.x**
- **PostgreSQL 16**
- **psycopg 3**
- **Docker**
- **WSL (Linux-based development environment)**
- **django-taggit**

---

## 📁 Project Structure

```
mysite/
├── blog/
│ ├── migrations/
│ ├── static/
│ ├── templates/
| ├── templatetags/
│ ├── admin.py
│ ├── apps.py
│ ├── feeds.py
│ ├── forms.py
│ ├── models.py
│ ├── sitemaps.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── my_env/
├── mysite/
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── manage.py
├── requirements.txt
├── mysite_data.json
└── README.md
```
---

## ⚙️ Local Setup Instructions

### 1️⃣ Clone the repository

```bash
git clone https://github.com/emmiduh93/mysite.git
cd the-repo-name
```

### 2️⃣ Create and activate a virtual environment
```bash
python3 -m venv my_env
source my_env/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run PostgreSQL using Docker
```bash
docker run -d \
  --name blog_db \
  -e POSTGRES_DB=blog \
  -e POSTGRES_USER=blog \
  -e POSTGRES_PASSWORD=secret \
  -p 5432:5432 \
  postgres:16.2
```

### 5️⃣ Environment variables
Create a .env file:
```env
DB_NAME=blog
DB_USER=blog
DB_PASSWORD=secret
DB_HOST=localhost
DB_PORT=5432
```

### 6️⃣ Apply migrations
```bash
python manage.py migrate
```

### 7️⃣ Load sample data (optional)
```bash
python manage.py loaddata mysite_data.json
```

### 8️⃣ Run the development server
```bash
python manage.py runserver
```
Visit:
```cpp
http://127.0.0.1:8000/
```
### 🔐 Admin Interface
Create an admin user:

```bash
python manage.py createsuperuser
Admin panel:
http://127.0.0.1:8000/admin/
```

### 📦 Data Management with Fixtures
Export data
```bash
python manage.py dumpdata --indent 2 --output=mysite_data.json
Import data
python manage.py loaddata mysite_data.json```
```
---
## 📌 Future Enhancements
Django REST Framework (API)

User authentication and profiles

Rich text editor for posts

Full Docker Compose setup

Cloud deployment (GCP / Azure / AWS)

## 👤 Author
Emmanuel Iduh
Django Developer

## 📄 License
This project is licensed under the MIT License.