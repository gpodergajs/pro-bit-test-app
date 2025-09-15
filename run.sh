#!/bin/bash

# A simple script to manage the Docker environments for the Car App.

# Exit immediately if a command exits with a non-zero status.
set -e

# The first argument to the script determines the command to run.
COMMAND=$1

# --- Function Definitions ---

show_help() {
  echo "Usage: ./run.sh [command]"
  echo
  echo "Commands:"
  echo "  dev        - Start the development environment (with live-reload and debugger)."
  echo "  prod       - Start the production-like environment (Gunicorn, no debugger)."
  echo "  prod-d     - Start the production-like environment in detached mode."
  echo "  down       - Stop and remove all containers."
  echo "  logs       - Follow logs for all services (add a service name to filter, e.g., ./run.sh logs backend)."
}

# --- Command Logic ---

case "$COMMAND" in
  dev)
    echo "--> Starting development environment..."
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
    echo "--> Stopping and removing all containers..."
    docker-compose -f docker-compose.yml -f docker-compose.dev.yml down
    ;;
  seed)
    echo "--> Seeding the database..."
    # We execute the command on the container started by docker-compose.local.yml
    docker-compose exec backend flask seed_db # Assuming the 'backend' service is named in the compose file for this, which is not
    ;;
  logs)
    echo "--> Following logs..."
    # This allows passing an optional service name, e.g., ./run.sh logs backend
    docker-compose logs -f "${@:2}"
    ;;
  *)
    show_help
    exit 1
    ;;
esac