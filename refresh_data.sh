#!/bin/bash

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Activate virtual environment if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Log file
LOG_FILE="$SCRIPT_DIR/refresh_data.log"

# Current date and time
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Refreshing data..." >> "$LOG_FILE"

# Call the API to refresh data
RESPONSE=$(curl -s http://localhost:5000/api/refresh)

# Log the response
echo "[$DATE] Response: $RESPONSE" >> "$LOG_FILE"

# If virtual environment was activated, deactivate it
if [ -n "$VIRTUAL_ENV" ]; then
    deactivate
fi

echo "[$DATE] Refresh complete." >> "$LOG_FILE"
echo "-----------------------------------" >> "$LOG_FILE" 