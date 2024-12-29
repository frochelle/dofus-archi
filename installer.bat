REM Create a virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists.
)

REM Activate the virtual environment
call venv\Scripts\activate.bat

REM Install dependencies from requirements.txt
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

REM Keep the command window open after execution
pause