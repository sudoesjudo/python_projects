#!/bin/bash

# Function to activate you virtual environment automagically when you cd to a specified directory
function activate_venv {
  if [ "$PWD" == "/path/to/your/directory" ]; then # This should be the path where you want your virtual env. to automatically be activated when you cd to the directory
    source /path/to/your/venv/bin/activate # This should be the path to the venv you want activated
  fi
}

# Set the PROMPT_COMMAND to activate the venv when entering the project directory
PROMPT_COMMAND="activate_venv; $PROMPT_COMMAND"
