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


#### 3. Dynamic main menu with template tags Part 1 - File separtions

        modified:   README.md
        new file:   templates/shared/canvas_menu_tpl.html
        modified:   templates/shared/header.html
        new file:   templates/shared/navbar-tpl.html
        new file:   templates/shared/navbar.html


#### 4. Dynamic main menu with template tags Part 2 - Create template-library

        modified:   README.md
        new file:   apps/blog/templatetags/__init__.py
        new file:   apps/blog/templatetags/template-library.py


#### 5. Dynamic main menu with template tags Part 3 - Create template_library, show_menu method and Use show_menu to display menu

        Steps:

        1. Define logic in template library
        2. Loop menu
        3. Load template_library
        4. Use show_menu to display menu

        modified:   README.md
        deleted:    apps/blog/templatetags/template-library.py
        new file:   apps/blog/templatetags/template_library.py
        modified:   templates/shared/canvas-menu.html
        modified:   templates/shared/header.html
        deleted:    templates/shared/navbar-tpl.html
        renamed:    templates/shared/canvas_menu_tpl.html -> templates/shared/tpl/canvas_menu_tpl.html
        new file:   templates/shared/tpl/menu_tpl.html


#### 5. Dynamic post - Modified model and insert some posts

        modified:   README.md
        new file:   apps/blog/migrations/0002_auto_20220122_1437.py
        new file:   apps/blog/migrations/0003_auto_20220122_1441.py
        new file:   apps/blog/migrations/0004_alter_post_post_type.py
        new file:   apps/blog/migrations/0005_alter_post_post_type.py
        modified:   apps/blog/models.py
        ...
        new file:   media/photos/2022/01/22/featured-lg.jpg