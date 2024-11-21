# Storefront

An Advanced Ecommerce Backend Built with Django 5 and Django REST Framework

## About the Project

Storefront is a robust and scalable ecommerce backend designed to handle a variety of ecommerce functionalities. It supports managing collections, products, customers, addresses, orders, carts, and reviews. The system also includes user authentication with JWT, permissions-based actions, and a customized admin interface using Jazzmin.

## Features

- CRUD Operations: Full support for creating, updating, and deleting resources with appropriate permissions.
- Filter and Sort: Flexible filtering and sorting options for collections, products, and more.
- Authentication: Secure user authentication using JWT, with user management provided by djoser.
- Nested Resources: Support for nested relationships via drf-nested-routers.
- Admin Panel: A beautifully customized admin interface using django-jazzmin.
- Scalable Architecture: Redis integration for caching and improved performance.

## Key Modules

1. **Collections:** Organize products into categories.
2. **Products:** Manage product details including tags, likes, and reviews.
3. **Customers:** Handle customer data including profiles and addresses.
4. **Orders and Carts:** Manage order processing, cart items, and checkout workflows.
5. **Authentication:** Secure endpoints using JWT and support for user profiles.

## Technologies Used

- Backend: Django 5, Django REST Framework
- Database: MySQL
- Authentication: JWT (via djangorestframework-simplejwt)
- Admin Customization: Jazzmin
- Caching: Redis
- Environment Variables: python-dotenv
- Static File Management: Whitenoise

## Dependencies

Core

- django
- djangorestframework
- mysqlclient
  Developer Tools
- django-debug-toolbar
- pytest
  Admin Customization
- django-jazzmin
  Additional Features
- redis
- django-cors-headers
- pillow
- whitenoise
- djangorestframework-simplejwt
- djoser
- django-filter
- drf-nested-routers

## Installation

### Prerequisites

1. Make sure you have Python 3.10 or later installed.
2. Install MySQL and ensure it is running.
3. Install Redis for caching.

## Steps to Install

1. Clone the repository:

```bash
git clone https://github.com/Sanzi87/storefront.git
cd storefront
```

2. Create a virtual environment:

Install and use pipenv:

```bash
pip install pipenv
pipenv shell
pipenv install
```

Or if you prefer to use venv instead, you can do so with the following commands:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install
```

3. Create a .env file and include the following:

```ini
# Development

DJANGO_DEV_DATABASE_NAME = ...
DJANGO_DEV_DATABASE_HOST = localhost
DJANGO_DEV_DATABASE_USER = ...
DJANGO_DEV_DATABASE_PASS = ...
DJANGO_DEV_DATABASE_PORT = ...

DJANGO_DEV_EMAIL_HOST = ...
DJANGO_DEV_EMAIL_HOST_USER = ''
DJANGO_DEV_EMAIL_HOST_PASSWORD = ''
DJANGO_DEV_EMAIL_PORT = 2525
DJANGO_DEV_FROM_EMAIL = '...'

# Production

DJANGO_DATABASE_NAME = ...
DJANGO_DATABASE_HOST = ...
DJANGO_DATABASE_USER = ...
DJANGO_DATABASE_PASS = ...
DJANGO_DATABASE_PORT = ...

DJANGO_EMAIL_HOST = localhost
DJANGO_EMAIL_HOST_USER = ''
DJANGO_EMAIL_HOST_PASSWORD = ''
DJANGO_EMAIL_PORT = 25
DJANGO_FROM_EMAIL = '...'
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser for admin access:

```bash
python manage.py createsuperuser
```

6. Start the development server:

```bash
python manage.py runserver
```

7. Open [http://localhost:8000](http://localhost:8000) to access the application.

## How to Run Tests

Run the tests using pytest:

```bash
pytest
```

## Admin Panel

The admin panel has been enhanced using Jazzmin for a modern UI. Access it at:
[http://localhost:8000/admin](http://localhost:8000/admin)

## Future Enhancements

- Add payment gateway integration.
- Add delivery integration.
- Implement advanced analytics and reporting features.
- Extend caching strategies for improved performance.

## APIs

Shop: [http://localhost:8000/admin](http://localhost:8000/shop)
Auth: [http://localhost:8000/auth](http://localhost:8000/auth)

For more info: [djoser JWT Endpoints](https://djoser.readthedocs.io/en/latest/jwt_endpoints.html)

## License

This project is open-source and available under the MIT License.

## Happy Coding! Build your ecommerce platform with Storefront! 🛍️
