# URL Shortener API 😄🚀

Welcome to the URL Shortener API project. This is a simple Django REST framework application that allows users to shorten long URLs.

## Features 🌟

- **URL Shortening**: Convert your long URLs into short ones.
- **URL Expansion**: Expand the shortened URL back to its original form.

## Getting Started 🏃

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites 📋

- Python 3.8 or higher
- Poetry
- Django 3.1
- Django Rest Framework
- drf-yasg (for Swagger docs)

### Installation 🔧

1. Clone this repository
    ```
    git clone https://github.com/oskarissimus/urlshortener.git
    ```
2. Navigate into the repo directory
    ```
    cd urlshortener
    ```
3. Install dependencies using Poetry
    ```
    poetry install
    ```
4. Navigate into the django directory
    ```
    cd urlshortener
    ```
5. Apply migrations
    ```
    poetry run python manage.py migrate
    ```
6. Create .env file based on .example.env and fill in the required values
    ```
    cp .example.env .env
    ```

### Running the Server 💻

Run the Django development server

```bash
poetry run dotenv run python manage.py runserver
```

You can now access the API at http://localhost:8000/shortener and the Swagger docs at http://localhost:8000/swagger/.

## Running the Tests 🧪

You can run the test suite using the following command:

```bash
poetry run dotenv run python manage.py test
```

