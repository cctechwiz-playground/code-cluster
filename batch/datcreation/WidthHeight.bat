:WIDTH
echo Select the width in pixels:
echo Available widths:
echo 8
echo 16
echo 32
echo 64

set /p choice="Width = "
if %choice%==8 set width=8
goto HEIGHT
if not %choice%==8 goto N1
:N1
if %choice%==16 set width=16
goto HEIGHT
if not %choice%==16 goto N2
:N2
if %choice%==32 set width=32
goto HEIGHT
if not %choice%==32 goto N3
:N2
if %choice%==64 set width=64
goto HEIGHT
if not %choice%==64 goto WERROR

:WERROR
echo EEENOPE Try again 
goto WIDTH

:HEIGHT
cls
echo Select the height in pixels:
echo Available heights:
echo 8
echo 16
echo 32
echo 64

set /p choice="Height = "
if %choice%==8 set height=8
goto PRINT
if not %choice%==8 goto H1
:H1
if %choice%==16 set height=16
goto PRINT
if not %choice%==16 goto H2
:H2
if %choice%==32 set height=32
goto PRINT
if not %choice%==32 goto H3
:H2
if %choice%==64 set height=64
goto PRINT
if not %choice%==64 goto HERROR

:HERROR
echo EEENOPE Try again 
goto HEIGHT

::Remove when complied together
:PRINT
echo width = %width%		>> %png%.dat
echo height = %height%		>> %png%.dat