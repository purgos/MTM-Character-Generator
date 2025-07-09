@echo off
echo Building MTM Character Sheet for Windows...

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt

REM Build the executable
echo Building Windows executable...
pyinstaller character_sheet_windows.spec

echo.
echo Build complete! The Windows executable is in the dist\ folder.
echo You can run it by double-clicking MTM_Character_Sheet_Windows.exe
pause 