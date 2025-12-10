# Image base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY scripts/wait-for-db.sh /wait-for-db.sh

RUN chmod +x /waint-for-db.sh 

# Copy project
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["/waint-for-db.sh", "python", "manage.py", "runserver", "0.0.0.0:8000" ]