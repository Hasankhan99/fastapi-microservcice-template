#!/bin/bash
# Test runner script

echo "Running tests..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install test dependencies
pip install -r requirements-dev.txt

# Run tests with coverage
pytest tests/ -v --cov=app --cov-report=html --cov-report=term-missing

echo "Coverage report generated in htmlcov/index.html"
