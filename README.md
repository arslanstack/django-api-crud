# API CRUD with Django Rest Framework

# Environments
| Environment | URL | Branch |
| :---------- | :-- | :----- |
| Development  | https://drfs.arslanstack.com/ | `main` |

# Features
- RESTful API CRUD for Blogs
- JWT State-less Authentication

# Technologies
- Django
- Django Rest Framework
- SQLite
- WhiteNoise
- Slugify

# Setup
```sh
$ git clone https://github.com/arslanstack/django-api-crud.git

$ cd django-api-crud

$ venv/bin/activate

$ pip install -r requirements.txt

$ ./manage.py migrate

$ ./manage.py createsuperuser

$ ./manage.py runserver
```

# API Endpoints
| URL | Description |
| :-- | :---------- |
| /api/user/ | For Authentication and Profile Management |
| /api/blogs/ | For Blogs CRUD |


# Author
- Muhammad Arslan <
