# /backend/run.py
from app import create_app

app = create_app()

if __name__ == "__main__":
    # Note: This is for local development without Docker
    # In Docker, Gunicorn will be the entry point.
    app.run(host='0.0.0.0', port=5000)