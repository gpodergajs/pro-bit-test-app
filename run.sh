#!/bin/bash

# A helper script to manage all Docker and development tasks for the Car App.

# Exit immediately if a command exits with a non-zero status.
set -e

# The first argument to the script determines the command to run.
COMMAND=$1

# --- Function Definitions ---

show_help() {
  echo "Usage: ./run.sh [command]"
  echo
  echo "--- Hybrid Workflow Commands (Fastest for local coding) ---"
  echo "  start-db      - Starts only the database container in the background."
  echo "  stop-db       - Stops the database container."
  echo "  reset-db      - STOPS the DB container and DELETES ALL DATA in its volume."
  echo "  local-help    - Shows instructions for running the Flask app and local commands."
  echo
  echo "--- Fully-Containerized Workflow Commands (Consistent & Reproducible) ---"
  echo "  dev           - Starts the full dev environment with debugger support."
  echo "  prod          - Starts the production-like environment in the foreground."
  echo "  prod-d        - Starts the production-like environment in the background (detached)."
  echo "  down          - Stops and removes all containers for the dev/prod environments."
  echo
  echo "--- Database Commands (For the Fully-Containerized Workflow) ---"
  echo "  migrate \"msg\" - Generates a new database migration script."
  echo "  upgrade       - Applies pending migrations to the database."
  echo "  seed          - Seeds the database with initial data."
  echo
  echo "--- Utility Commands ---"
  echo "  logs [service] - Follows the logs of running services (e.g., ./run.sh logs backend)."
}

# --- Command Logic ---

case "$COMMAND" in
  # --- Hybrid Workflow ---
  start-db)
    echo "--> Starting database container for local development..."
    docker-compose -f docker-compose.local.yml up -d
    ;;
  stop-db)
    echo "--> Stopping local development database container..."
    docker-compose -f docker-compose.local.yml down
    ;;
  seed-db)
    echo "--> Seeding the local development database..."
    # TODO - add seed for local dev
    ;;
  reset-db)
    echo "--> WARNING: STOPPING container and REMOVING database volume..."
    docker-compose -f docker-compose.local.yml down -v
    ;;
  local-help)
    echo "--> To run the Flask app locally (after starting the DB with './run.sh start-db'):"
    echo "1. Activate your virtual environment: source venv/bin/activate"
    echo "2. Navigate into the backend:       cd backend"
    echo "3. Run the Flask server:            flask run"
    echo "4. To manage the DB, use 'flask db migrate', 'flask db upgrade', and 'flask seed_db' in the backend directory."
    ;;

  # --- Fully-Containerized Workflow ---
  dev)
    echo "--> Starting fully-containerized development environment..."
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml up --build
    ;;
  prod)
    echo "--> Starting production-like environment..."
    docker-compose up --build
    ;;
  prod-d)
    echo "--> Starting production-like environment in detached mode..."
    docker-compose up -d --build
    ;;
  down)
    echo "--> Stopping and removing all dev/prod containers..."
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml down
    ;;

  # --- Database Commands (for containerized workflow) ---
  migrate)
    if [ -z "${@:2}" ]; then
      echo "ERROR: Please provide a migration message."
      echo "Usage: ./run.sh migrate \"Your descriptive message\""
      exit 1
    fi
    echo "--> Generating new migration script inside the container..."
    docker-compose exec backend flask db migrate -m "${@:2}"
    ;;
  upgrade)
    echo "--> Applying migrations inside the container..."
    docker-compose exec backend flask db upgrade
    ;;
  seed)
    echo "--> Seeding the database inside the container..."
    docker-compose exec backend flask seed_db
    ;;

  # --- Utility ---
  logs)
    echo "--> Following logs..."
    docker-compose logs -f "${@:2}"
    ;;
  *)
    show_help
    exit 1
    ;;
esac