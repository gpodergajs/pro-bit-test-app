# /backend/Dockerfile

# Stage 1: Use the official Python image
FROM python:3.9-slim

# Stage 2: Set the working directory
WORKDIR /app

# Stage 3: Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Stage 4: Copy the rest of the application code
COPY . .

# Stage 5: Expose the port Gunicorn will run on
EXPOSE 5000

# Stage 6: Command to run the application using Gunicorn
# This is more robust for production than Flask's built-in server.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--reload", "wsgi:app"]
