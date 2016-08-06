@echo off

:XYPOS
echo Is there more than one image region related to this tile?
echo 1. Yes
echo 2. No

set /p choice=""
if %choice%==1 goto MULTI
if not %choice%==1 goto XNEXT
:XNEXT
if %choice%==2 goto SINGLE
if not %choice%==2 goto BAD

:BAD
echo Input not vaild,
pause 
goto XYPOS

:SINGLE
echo please give the x,y coordinate of the related imagage region:
set /p x="x: "
set /p y="y: "
set x=%x%
set y=%y%
goto PRINT

:MULTI
echo How many image regions are related to this tile?
echo Please enter a number 2-4: 
set /p choice=""
if %choice%==2 goto XTWO
if not %choice%==2 goto MNEXT
:MNEXT
if %choice%==3 goto XTHREE
if not %choice%==3 goto MNEXT2
:MNEXT2
if %choice%==4 goto XFOUR
if not %choice%==4 goto MERROR

:MERROR
echo input not valid,
pause
goto MULTI

:XTWO
echo please give the x,y coordinate of the first image region.
set /p x1="x: "
set /p y1="y: "
echo please give the x,y coordinate of the second image region.
set /p x2="x: "
set /p y2="y: "
set x={%x1%, %x2%}
set y={%y1%, %y2%}
goto PRINT

:XTHREE
echo please give the x,y coordinate of the first image region.
set /p x1="x: "
set /p y1="y: "
echo please give the x,y coordinate of the second image region.
set /p x2="x: "
set /p y2="y: "
echo please give the x,y coordinate of the third image region.
set /p x3="x: "
set /p y3="y: "
set x={%x1%, %x2%, %x3%}
set y={%y1%, %y2%, %y3%}
goto PRINT

:XFOUR
echo please give the x,y coordinate of the first image region.
set /p x1="x: "
set /p y1="y: "
echo please give the x,y coordinate of the second image region.
set /p x2="x: "
set /p y2="y: "
echo please give the x,y coordinate of the third image region.
set /p x3="x: "
set /p y3="y: "
echo please give the x,y coordinate of the fourth image region.
set /p x4="x: "
set /p y4="y: "
set x={%x1%, %x2%, %x3%, %x4%}
set y={%y1%, %y2%, %y3%, %y4%}
goto PRINT

:PRINT
echo x = %x%,
echo y = %y%,
pause