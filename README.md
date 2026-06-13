# Tourism and Travel Web Platform

A Django-based tourism and travel website featuring a blog system and user
authentication. This project focused on backend development — the
frontend templates were provided, and the work involved building
the server-side logic, database models, URL routing, and deployment
configuration.

Developed as a hands-on project to apply backend web development
concepts learned during my computer engineering studies.



## Features

- Blog system with create, read, and manage posts
- User authentication — register, login, logout
- Media file handling for post images


## Project Structure

Mysite/
├── accounts/          user authentication (register, login, logout)
├── blog/              blog application (posts, views, models)
├── website/           main landing page
├── mysite/            project settings and URL configuration
├── templates/         HTML templates (frontend provided)
├── statics/           CSS, SCSS, JavaScript (frontend provided)
├── staticfiles/       collected static files for deployment
├── media/             uploaded media files
├── manage.py
├── requirements.txt
├── liara.json         Liara deployment configuration
└── liara_nginx.conf   Nginx server configuration



## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python, Django |
| Frontend | HTML, CSS, SCSS, JavaScript (pre-built) |
| Database | SQLite (development) |
| Version control | Git, GitHub |


## How to Run Locally

```bash
git clone https://github.com/RealAriya/Mysite.git
cd Mysite
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open your browser at http://127.0.0.1:8000



## What I Learned

Building the backend of this project gave me practical experience
with Django's MVT architecture, database modeling with the Django ORM,
user authentication flows, and configuring a Django application for
cloud deployment with Nginx.

---

## Author

Ariya Tahmasebi Abr
GitHub: [@RealAriya](https://github.com/RealAriya)

---

## License

MIT License — free to use and build on for educational purposes.

