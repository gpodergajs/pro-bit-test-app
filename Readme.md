# Car Overview Application

This is a single-page web application for managing automobiles, built with a Python/Flask backend and a separate frontend service, all managed with Docker.

All Docker and development tasks are managed via the `./run.sh` helper script.

## Table of Contents
- [Prerequisites](#prerequisites)
- [**Workflow 1: Hybrid Development (Recommended for Speed)**](#workflow-1-hybrid-development-recommended-for-speed)
  - [One-Time Setup](#one-time-setup)
  - [Daily Workflow](#daily-workflow)
- [**Workflow 2: Fully-Containerized Development (for Consistency)**](#workflow-2-fully-containerized-development-for-consistency)
  - [Daily Workflow](#daily-workflow-1)
- [Getting Help](#getting-help)

---

## Prerequisites
- **Docker & Docker Compose:** Required for running services. [Get Docker](https://docs.docker.com/get-docker/).
- **Python 3.9+:** Required for the Hybrid Workflow.
- **Visual Studio Code (Recommended)**
  - **Python Extension**
  - **Docker Extension**

---

## Workflow 1: Hybrid Development (Recommended for Speed)
**Use this for the fastest day-to-day development.** The database runs in Docker, but the Flask app runs directly on your machine for instant restarts and effortless debugging.

### One-Time Setup
You only need to do this once.

**1. Create a Local Docker Compose File:**
Create a file named `docker-compose.local.yml` in the project root. This file *only* defines the database service.

```yaml
# docker-compose.local.yml
version: '3.8'
services:
  db:
    image: mysql:8.0
    environment:
      - MYSQL_DATABASE=cardb
      - MYSQL_USER=user
      - MYSQL_PASSWORD=password
      - MYSQL_ROOT_PASSWORD=rootpassword
    ports:
      - "3306:3306"
    volumes:
      - mysql-data:/var/lib/mysql
volumes:
  mysql-data:
```

**2. Create a Local Environment Configuration:**
Create a file named `.env` inside the `backend/` directory. This tells your local Flask app how to connect to the database.

```
# backend/.env
FLASK_APP=run.py
FLASK_DEBUG=1
DB_TYPE=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_NAME=cardb
DB_USER=user
DB_PASSWORD=password
```

**3. Set Up a Python Virtual Environment:**
Run these commands from the project's root directory.

```bash
# Create the virtual environment
python -m venv venv

# Activate it (macOS/Linux)
source venv/bin/activate
# On Windows: .\venv\Scripts\activate

# Install the required Python packages
pip install -r backend/requirements.txt
```

### Daily Workflow
**Step 1: Start the Database**
This starts the database container in the background.
```bash
./run.sh start-db
```

**Step 2: Run the Flask App**
Activate your virtual environment and run the Flask server. For instructions, you can run `./run.sh local-help`.
```bash
# Activate the virtual environment
source venv/bin/activate

# Navigate to the backend folder
cd backend

# Run the Flask development server
flask run```
Your API is now running on `http://localhost:5000`.

**Step 3: Manage the Database (Locally)**
When you change a model, run these commands from the `backend/` directory (with your `venv` active).
```bash
# Generate a new migration
flask db migrate -m "Your descriptive message"

# Apply the migration
flask db upgrade

# Seed the database
flask seed_db
```

**Step 4: Stop the Database**
When you are done, stop the database container.
```bash
./run.sh stop-db
```
To completely reset the database, run `./run.sh reset-db`.

---

## Workflow 2: Fully-Containerized Development (for Consistency)
**Use this to guarantee your code runs in an identical environment to your teammates and CI/CD pipelines.** All commands are run via the script, which executes them inside the Docker container.

### Running with Nginx and Frontend Build
This setup uses Nginx to serve the frontend and proxy requests to the backend. The frontend is automatically built as part of the Nginx Docker image.

1.  **Build and Start All Services:**
    This command builds the frontend, backend, and Nginx services, and starts them.
    ```bash
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
    ```
    The frontend will be accessible via Nginx, and the backend will be running with `debugpy` enabled, waiting for a debugger to attach.

2.  **Access the Application:**
    Once all services are up, you can access the application in your browser at `http://localhost`.

3.  **Attach the Debugger (VS Code):**
    If you want to debug the backend, go to the "Run and Debug" view in VS Code (Ctrl+Shift+D), select the "Python: Attach to Docker" configuration, and click the "Start Debugging" button.

### Daily Workflow
**Step 1: Start All Containers**
This builds and starts all services, including the backend.
```bash
./run.sh dev
```
The backend will pause and wait for a debugger to attach. You can connect VS Code now or just proceed to the next steps.

**Step 2: Manage the Database (via Script)**
When you change a model, open a **new terminal** and use the `run.sh` script.

```bash
# Generate a new migration script
./run.sh migrate "A descriptive message about the change"

# Apply the migration to the database
./run.sh upgrade
```

**Step 3: Seed the Database**
To populate the database with initial data, run:
```bash
./run.sh seed
```

**Step 4: Stop Everything**
This command stops and removes all containers related to this workflow.
```bash
./run.sh down
```

---

## Getting Help
To see a full list of available commands and their descriptions, run the script with no arguments:
```bash
./run.sh
```
