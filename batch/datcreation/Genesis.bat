:GENESIS
echo Are you creating a new tile set or appending an existing one?
echo 1. New
echo 2. Appending

set /p choice=""
if %choice%==1 goto NEW
if not %choice%==1 goto QNEXT
:QNEXT
if %choice%==2 goto APPEND
if not %choice%==2 goto QERROR

:QERROR
echo Input not vaild,
pause 
goto GENESIS

:NEW
echo Please insert tileset image name and press "Enter"...
set /p png=""
echo background_color{ %v1%, %v2%, %v3% } >> %png%.dat
set id=0
goto START


:APPEND
echo Please insert tileset image name and press "Enter"...
set /p png=""
echo Where are we picking up?
set /p id="Please enter the last ID from the %png%.dat file. "
set id=%id%
goto START