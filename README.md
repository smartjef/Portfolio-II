# Portfolio-II

Is a second Template for portfolio and resume website

Planning on building it to use API and data from the first portfolio

STEP 1: create an environment `python -m venv <env_name>` or `virtualenv <env_name>`

STEP 2: activate the environment windows: `<env_name>\Scripts\activate`, Linux: `source <env_name>/bin/activate`

STEP 3: install the requirements `pip install -r requirements.txt`

STEP 4: Start Project `django-admin startproject <project_name> .`

STEP 5: Start App `python manage.py startapp <app_name>`

STEP 6: Add app to settings.py 
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # add app here
    'app_name.apps.AppNameConfig',
]
```
STEP 7: Create a migration `python manage.py makemigrations`

STEP 8: Migrate `python manage.py migrate`

STEP 9: Create a superuser `python manage.py createsuperuser`

STEP 10: Run server `python manage.py runserver`

STEP 11: View in browser [127.0.0.1:8000](127.0.0.1:8000)
