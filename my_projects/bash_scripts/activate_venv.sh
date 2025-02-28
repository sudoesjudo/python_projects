#!/bin/bash

# Define the project directory where the virtual environment should activate
PROJECT_DIR="/path/to/your/directory"
VENV_PATH="/path/to/your/venv/bin/activate"

# Function to manage virtual environment activation/deactivation
function manage_venv {
  if [[ "$PWD" == "$PROJECT_DIR" || "$PWD" == "$PROJECT_DIR"* ]]; then
    # If inside the project directory and venv is not activated, activate it
    if [[ -z "$VIRTUAL_ENV" ]]; then
      source "$VENV_PATH"
    fi
  else
    # If outside the project directory and venv is active, deactivate it
    if [[ -n "$VIRTUAL_ENV" ]]; then
      deactivate
    fi
  fi
}

# Set PROMPT_COMMAND to check the directory on every command execution
PROMPT_COMMAND="manage_venv; $PROMPT_COMMAND"
