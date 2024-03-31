# Demo: Testing Django using Playwright

This is a very simple Django app that makes use of the following tools:

- HTMX 
- AlpineJS 
- Tailwind CSS 
- https://github.com/django-crispy-forms/crispy-tailwind

The app is tested using Playwright. 

## KISS

The default Django settings were used as much as possible. This is because the goal of this app is to demonstrate the use of Playwright.

## Running the demo code 

To get the demo running:

### Install 

```
python3 -m venv venv 
pip install -r requirements.txt 
playwright install-deps
playwright install
```

### Run migrations 

```
Python manage.py migrate
```

### Runserver 

```
python manage.py runserver
```

### Running the tests 

```
pytest
```

