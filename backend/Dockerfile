# Backend Dockerfile (Django)
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /backend

# Copy the requirements file
COPY backend/dev.txt /backend/requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Django project
COPY backend /backend/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]
