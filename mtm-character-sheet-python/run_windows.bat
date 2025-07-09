@echo off
echo Starting MTM Character Sheet (Windows)...

REM Check if the executable exists
if exist "dist\MTM_Character_Sheet_Windows.exe" (
    echo Launching MTM Character Sheet...
    start "" "dist\MTM_Character_Sheet_Windows.exe"
) else (
    echo Error: MTM_Character_Sheet_Windows.exe not found!
    echo Please build the executable first by running build_windows.bat
    pause
) 