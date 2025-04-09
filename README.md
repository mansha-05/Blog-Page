# ✍️ Syntax & Soul – A Flask Blog Platform

Welcome to **Syntax & Soul**, a minimal and elegant blog application built using Flask. Users can register, log in, and read meaningful content. Admins can manage posts, and readers can leave comments — all in a sleek UI.

## Features

- 📝 Create, edit, and delete blog posts (admin-only)
- 👥 User authentication (Register/Login/Logout)
- 💬 Comment system with Gravatar integration
- 🔐 Role-based access using decorators
- 📧 Contact form with email support
- 🎨 Bootstrap styling with CKEditor for rich text

## 🛠️ Built With

- [Flask] – Web framework
- [Flask-Login] – Authentication
- [Flask-Bootstrap] – Frontend styling
- [Flask-CKEditor] – Rich text editor
- [SQLAlchemy] – ORM for database interaction
- [Jinja2] – Templating engine


# This is the folder structure of my project
.
├── main.py
├── models.py
├── decorators.py
├── forms.py
├── email_utils.py
├── /templates
├── /static
├── /instance
│   └── posts.db
├── .env
├── .gitignore
└── requirements.txt
