#!/bin/bash

# Script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
cd "$SCRIPT_DIR"

# Log file
LOG_FILE="$SCRIPT_DIR/api_server.log"

# Current date and time
DATE=$(date '+%Y-%m-%d %H:%M:%S')

# Check if PID file exists
if [ -f "$SCRIPT_DIR/api_server.pid" ]; then
    PID=$(cat "$SCRIPT_DIR/api_server.pid")
    
    # Check if process is running
    if ps -p $PID > /dev/null; then
        echo "[$DATE] Stopping API server with PID: $PID" >> "$LOG_FILE"
        kill $PID
        echo "API server with PID $PID has been stopped."
    else
        echo "[$DATE] API server with PID $PID is not running." >> "$LOG_FILE"
        echo "API server is not running."
    fi
    
    # Remove PID file
    rm "$SCRIPT_DIR/api_server.pid"
else
    echo "[$DATE] API server PID file not found." >> "$LOG_FILE"
    echo "API server PID file not found. Server may not be running."
    
    # Try to find and kill the process by name
    PID=$(pgrep -f "python3 api_server.py")
    if [ ! -z "$PID" ]; then
        echo "[$DATE] Found API server process with PID: $PID. Stopping..." >> "$LOG_FILE"
        kill $PID
        echo "API server with PID $PID has been stopped."
    fi
fi

echo "[$DATE] Stop command completed." >> "$LOG_FILE" 