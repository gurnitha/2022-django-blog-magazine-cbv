# 2022-django-blog-magazine-cbv
Building a Blog Magazine Using Django 3.2.7 with CBV
https://github.com/gurnitha/2022-django-blog-magazine-cbv


#### 1. Complete basics setup with Postgres database

        .
        ├── LICENSE
        ├── README.md
        ├── apps
        │   ├── accounts
        │   └── blog
        ├── config
        │   ├── __init__.py
        │   ├── __pycache__
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── static
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        ├── manage.py
        ├── requirements.txt
        └── templates
            ├── base.html
            ├── haed.html
            └── shared

        modified:   .gitignore
        modified:   README.md

        NOTE: Static files are ignored by git


#### 2. Create models: Author, Category, Tag and Post

        modified:   README.md
        modified:   apps/accounts/admin.py
        new file:   apps/accounts/migrations/0001_initial.py
        modified:   apps/accounts/models.py
        modified:   apps/blog/admin.py
        new file:   apps/blog/migrations/0001_initial.py
        modified:   apps/blog/models.py

