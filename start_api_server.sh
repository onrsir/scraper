#!/bin/bash

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Activate virtual environment if exists
if [ -d "venv" ]; then
    source venv/bin/activate
fi

# Log file
LOG_FILE="$SCRIPT_DIR/api_server.log"

# Current date and time
DATE=$(date '+%Y-%m-%d %H:%M:%S')

echo "[$DATE] Starting API server..." >> "$LOG_FILE"

# Start the API server
nohup python3 api_server.py >> "$LOG_FILE" 2>&1 &

# Save the process ID
PID=$!
echo "[$DATE] API server started with PID: $PID" >> "$LOG_FILE"
echo "$PID" > "$SCRIPT_DIR/api_server.pid"

echo "API server started with PID: $PID"
echo "Logs are being written to: $LOG_FILE" 