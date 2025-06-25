#!/bin/bash
# Database migration script

echo "Running database migrations..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Create migration if message provided
if [ ! -z "$1" ]; then
    echo "Creating new migration: $1"
    alembic revision --autogenerate -m "$1"
fi

# Run migrations
echo "Applying migrations..."
alembic upgrade head

echo "Database migrations complete!"
