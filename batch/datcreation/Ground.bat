:GROUND
echo Select the GROUND type by number:
echo 1. "traversable"
echo 2. "shallow_water"
echo 3. "wall"
echo 4. "deep_water"
echo 5. "wall_top_right_water"
echo 6. "wall_top_left_water"
echo 7. "wall_bottom_right_water"
echo 8. "wall_bottom_left_water"
echo 9. "wall_top_right"
echo 10."wall_top_left"
echo 11."wall_bottom_left"
echo 12."wall_bottom_right"

echo Enter GROUND number here: 
set /p choice=""
if %choice%==1 set ground="traversable"
goto PRINT
if not %choice%==1 goto TWO
:TWO
if %choice%==2 set ground ="shallow_water"
goto PRINT
if not %choice%==2 goto THREE
:THREE
if %choice%==3 set ground ="wall"
goto PRINT
if not %choice%==3 goto FOUR
:FOUR
if %choice%==4 set ground ="deep_water"
goto PRINT
if not %choice%==4 goto FIVE
:FIVE
if %choice%==5 set ground ="wall_top_right_water"
goto PRINT
if not %choice%==5 goto SIX
:SIX
if %choice%==6 set ground ="wall_top_left_water"
goto PRINT
if not %choice%==6 goto SEVEN
:SEVEN
if %choice%==7 set ground ="wall_bottom_right_water"
goto PRINT
if not %choice%==7 goto EIGHT
:EIGHT
if %choice%==8 set ground ="wall_bottom_left_water"
goto PRINT
if not %choice%==8 goto NINE
:NINE
if %choice%==9 set ground ="wall_top_right"
goto PRINT
if not %choice%==9 goto TEN
:TEN
if %choice%==10 set ground ="wall_top_left"
goto PRINT
if not %choice%==10 goto ELV
:ELV
if %choice%==11 set ground ="wall_bottom_left"
goto PRINT
if not %choice%==11 goto TWL
:TWL
if %choice%==12 set ground ="wall_bottom_right"
goto PRINT
if not %choice%==12 goto ERROR

:ERROR
echo EEENOPE Try again 
goto GROUND

::Remove when complied together
:PRINT 
echo 	ground = %ground%		>> %png%.dat









