@echo off
echo Starting AI Job Search Tracker Dashboard Server...
start "" cmd /k python tools/server.py
timeout /t 3
start chrome http://localhost:8000
exit
