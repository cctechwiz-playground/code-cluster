@echo off
set path=%CD%

:FOLD
cls
set /p folder="Enter Folder Name: "

:RE1
cls
echo Create Sub?
echo y/n?
:SUBMAKE
set /p choice="Your choice?"
if %choice%==n goto MORE
if not %choice%==n goto CONT
:CONT
if %choice%==y goto NEXT
if not %choice%==y goto RE1
:NEXT
cls
set /p sub="Enter Sub Name: "
md "%path%\%folder%\%sub%"

:RE2
cls
echo Creat another sub?
echo y/n?
if %choice%==n goto MORE
if not %choice%==n goto CONT2
:CONT2
if %choice%==y goto SUBMAKE
if not %choice%==y goto RE2

:MORE
md "%path%\%folder%"
cls
echo Make Anoter Folder?
echo y/n?
set /p choice="Your choice?"
if %choice%==n goto EOF
if not %choice%==n goto CONT3
:CONT3
if %choice%==y goto FOLD
if not %choice%==y goto MORE