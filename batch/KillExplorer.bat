::Ends the "explorer.exe" process and restarts it

@ECHO off
set path1=%CD%

taskkill /IM explorer.exe /F
sleep 1
start explorer.exe
sleep 1

echo Would you like to open your folder again?
echo 1. Yes
echo 2. No

set /p choice="What is your command? "
if %choice%==1 goto OPEN
if %choice%==2 goto CLOSE

:OPEN
start explorer.exe %path1%

:CLOSE
::echo All done!
::pause >nul
exit