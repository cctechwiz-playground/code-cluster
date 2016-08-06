:LAYER
echo Select the Default Layer by number:
echo 0. Lower
echo 1. Intermediate
echo 2. Upper

echo Enter Default Layer number here: 
set /p choice=""
if %choice%==0 set layer=0
goto PRINT
if not %choice%==0 goto ONE
:ONE
if %choice%==1 set layer =1
goto PRINT
if not %choice%==1 goto TWO
:TWO
if %choice%==1 set layer =2
goto PRINT
if not %choice%==1 goto ERROR

:ERROR
echo EEENOPE Try again 
goto LAYER

::Remove when complied together
:PRINT
echo 	default_layer = %layer%		>> %png%.dat