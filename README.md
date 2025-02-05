# Blog Django Project

## Introduction
This is a Django-based blogging platform that allows users to register, create, and manage blog posts.

## Features
- User authentication (login/register/logout)
- Create, update, and delete blog posts
- User profiles and account management
- Admin panel for managing content

## Installation
### Prerequisites
- Python 3.x
- pip (Python package manager)
- Virtual environment (recommended)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/pariyaaf/blog-django.git
   cd blog-django-main
   ```
2. Create a virtual environment and activate it:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```sh
   python manage.py migrate
   ```
5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
6. Run the development server:
   ```sh
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`
- Log in or register to create and manage blog posts.
- Use the Django admin panel at `http://127.0.0.1:8000/admin/` for content management.

## Project Structure
```
blog-django-main/
│── .gitignore
│── requirements.txt
│── manage.py
│── pariya_blog/
│   ├── accounts/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   ├── blog/
│   │   ├── models.py
│   │   ├── views.py
│   │   ├── urls.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
```
