#!/bin/bash
# Development server startup script

echo "Starting FastAPI development server..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install dependencies
pip install -r requirements-dev.txt

# Run database migrations
alembic upgrade head

# Start the server with hot reload
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload --log-level info
