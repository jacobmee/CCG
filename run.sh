#!/bin/bash

# Get the absolute path of the script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

echo "Running time control script from: $SCRIPT_DIR"
# Create the virtual environment in the script directory
python3 -m venv "$SCRIPT_DIR/venv"

# Activate it
source "$SCRIPT_DIR/venv/bin/activate"

# Set the working directory to the script's location
cd "$SCRIPT_DIR"

# Install dependencies
#pip install -r "requirements.txt"
#pip install --upgrade openai

# Run the time control script
python3 "$SCRIPT_DIR/app.py"

# Deactivate when done
deactivate