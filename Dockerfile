# Base
FROM python:3.10-slim-bookworm
WORKDIR /app

# Install system packages
RUN apt-get update && apt-get install -y nginx supervisor && rm -rf /var/lib/apt/lists/*

# Python packages
ENV POETRY_VERSION=1.5.1 
ENV POETRY_VIRTUALENVS_CREATE=false
RUN pip install "poetry==$POETRY_VERSION"
COPY ./pyproject.toml ./poetry.lock /app/
RUN poetry install --no-root

# Copy application code
COPY . /app

# Install Python packages
RUN poetry install

# Collect static files
RUN python manage.py collectstatic --noinput
RUN python manage.py migrate

# Copy Nginx and supervisor configurations
COPY nginx.conf /etc/nginx/sites-available/default
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# Expose ports
EXPOSE 80

# Start processes
CMD ["/usr/bin/supervisord"]
