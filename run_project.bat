@echo off
echo Starting FreelancersConnect...
cd /d "%~dp0"

:: Activate the virtual environment
if exist "..\env\Scripts\activate.bat" (
    call "..\env\Scripts\activate.bat"
) else (
    echo Virtual environment not found at ..\env
    echo Attempting to run with system python...
)

:: Run the server
python manage.py runserver

pause
