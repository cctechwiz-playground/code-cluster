@echo off
echo What would you like to do?
echo 1. Hello World
echo 2. Input Output
echo 3. Exit

:MENU
set /p choice="What is your command? "
if %choice%==1 goto HELLO
if not %choice%==1 goto NEXT
:NEXT
if %choice%==2 goto INPUT
if not %choice%==2 goto NEXT2
:NEXT2
if %choice%==3 goto EOF
if not %choice%==3 goto BAD

:BAD
cls
echo Sorry, That was not an option. Try again...
SLEEP 2
goto MENU

:HELLO
start HelloWorld.bat
goto EOF

:INPUT
start InputOutput.bat
goto EOF