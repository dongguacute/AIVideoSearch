#!/bin/bash

# Check if the virtual environment exists
if [ -d ".venv" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate
else
    echo "Virtual environment (.venv) not found. Please run 'uv venv' or 'python3 -m venv .venv' to create it and install dependencies."
    exit 1
fi

# Run the application
python3 -m src.main