@echo off
echo Please type something below and press "Enter"...
set /p string=""
echo %string% >InputOutput.txt

:Menu
cls
echo Would you like to type something else?
echo 1. Yes
echo 2. No

set /p choice="What is your command? "
if %choice%==1 goto MORE
if not %choice%==1 goto NEXT
:NEXT
if %choice%==2 goto CLOSE
if not %choice%==2 goto BAD

:MORE
cls
echo Please type something below and press "Enter"...
set /p string1=""
echo %string1% >>InputOutput.txt
goto MENU

:BAD
cls
echo Sorry, That was not an option. Try again...
SLEEP 2
goto MENU

:CLOSE
start InputOutput.txt
exit