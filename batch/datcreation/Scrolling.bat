:SCROLLING
echo Select the Scrolling type by number:
echo 0. None
echo 1. Parallax

echo Enter Scrolling type number here: 
set /p choice=""
if %choice%==0 goto SKIP
if not %choice%==0 goto ONE
:ONE
if %choice%==1 set scrolling ="parallax"
goto PRINT
if not %choice%==1 goto ERROR

:ERROR
echo EEENOPE Try again 
goto SCROLLING

::Remove when complied together
:PRINT
echo scrolling = %scrolling%		>> %png%.dat

:SKIP