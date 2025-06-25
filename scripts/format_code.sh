#!/bin/bash
# Code formatting script

echo "Formatting code..."

# Activate virtual environment if it exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Install formatting tools
pip install black isort flake8

# Format with black
black app/ tests/ --line-length 100

# Sort imports
isort app/ tests/ --profile black

# Check with flake8
flake8 app/ tests/ --max-line-length 100 --extend-ignore E203,W503

echo "Code formatting complete!"
