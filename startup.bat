@ECHO OFF
CLS
call "venv/Scripts/activate.bat"

:begin
CLS
ECHO 1.Full Setup (Run this if first time setup ONLY)
ECHO 2.Install requirements DNU
ECHO 3.Build DB DNU
ECHO 4.Run Application DNU
ECHO 5.Setup Enviroment DNU
ECHO.
CHOICE /C 12345 /M "Enter your choice:"

IF ERRORLEVEL 5 GOTO Envsetup
IF ERRORLEVEL 4 GOTO Run
IF ERRORLEVEL 3 GOTO Builddb
IF ERRORLEVEL 2 GOTO Install
IF ERRORLEVEL 1 GOTO Fullsetup

:Envsetup
ECHO Setting up enviroment
set FLASK_APP=CALCULATOR
set FLASK_DEBUG=1

:Fullsetup
ECHO Installing pip
py -m pip install --upgrade pip
ECHO Installing venv
py -m pip install --user virtualenv
ECHO Creating venv
py -m venv venv
ECHO Starting enviroment
.\venv\Scripts\activate
Echo Installing dependancy
pip install -r requirements.txt
set FLASK_APP=CALCULATOR
set FLASK_DEBUG=1

ECHO Setting up database
flask db init
ECHO Setup complete
pause
GOTO begin

:Install
Echo installing CALCULATOR dependancy
pip install -r requirements.txt
pause
GOTO begin

:Builddb
ECHO Setting up CALCULATOR database
flask db init
pause
GOTO begin

:Run
Echo Application will now start
flask run
if  errorlevel 1 goto ERROR

:exit
@exit

:ERROR
echo Failed
cmd /k
exit /b 1