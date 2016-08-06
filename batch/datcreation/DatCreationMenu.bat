::Created by CCTechWiz and RoughIngot
::For questions for support contact cctechwiz@gmail.com or RoughIngot@gmail.com
::This was intended to facilitate in the creation of .dat files for use in Solarus.
::This is completely open source feel free to modify this code for the better of the world.
::All code is written in windows BATCH Script using Notepad++.

@echo off
:GENESIS
echo Are you creating a new tile set or appending an existing one?
echo 1. New
echo 2. Appending
echo Please choose and press "Enter"

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
cls
echo Please insert tileset image name and press "Enter"...
echo The .dat file must have the same name as the .png file containing the tileset.
set /p png=""
set id=0
goto BACKGROUND

:BACKGROUND
cls
echo Please enter the background color in (r,g,b) format:
echo Remember valid numbers are from 0 - 255.
set /p r="r: "
set /p b="b: "
set /p g="g: "
cls
echo Is this correct?
echo background_color{ %r%, %b%, %g% }
echo Select y or n: 
set /p choice=""
if %choice%==y (
echo background_color{ %r%, %b%, %g% } >> %png%.dat
goto START
)
if not %choice%==y goto BNEXT
:BNEXT
if %choice%==n goto BACKGROUND
if not %choice%==n goto BERROR

:BERROR
echo Input not vaild,
pause 
goto BACKGROUND

:APPEND
echo Please insert tileset image name and press "Enter"...
set /p png=""
echo Where are we picking up?
set /p id="Please enter the last ID from the %png%.dat file. "
set id=%id%
goto START

:START

set /a id=%id%+1
goto GROUND

:GROUND
cls
echo %png%.dat 
echo.
echo Select the GROUND type by number:
echo 1. "traversable"
echo 2. "wall"
echo 3. "shallow_water"
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
if %choice%==1 (
set ground="traversable"
goto LAYER
)
if not %choice%==1 goto TWO
:TWO
if %choice%==2 (
set ground="wall"
goto LAYER
)
if not %choice%==2 goto THREE
:THREE
if %choice%==3 (
set ground="shallow_water"
goto LAYER
)
if not %choice%==3 goto FOUR
:FOUR
if %choice%==4 (
set ground="deep_water"
goto LAYER
)
if not %choice%==4 goto FIVE
:FIVE
if %choice%==5 (
set ground="wall_top_right_water"
goto LAYER
)
if not %choice%==5 goto SIX
:SIX
if %choice%==6 (
set ground="wall_top_left_water"
goto LAYER
)
if not %choice%==6 goto SEVEN
:SEVEN
if %choice%==7 (
set ground="wall_bottom_right_water"
goto LAYER
)
if not %choice%==7 goto EIGHT
:EIGHT
if %choice%==8 (
set ground="wall_bottom_left_water"
goto LAYER
)
if not %choice%==8 goto NINE
:NINE
if %choice%==9 (
set ground="wall_top_right"
goto LAYER
)
if not %choice%==9 goto TEN
:TEN
if %choice%==10 (
set ground="wall_top_left"
goto LAYER
)
if not %choice%==10 goto ELV
:ELV
if %choice%==11 (
set ground="wall_bottom_left"
goto LAYER
)
if not %choice%==11 goto TWL
:TWL
if %choice%==12 (
set ground="wall_bottom_right"
goto LAYER
)
if not %choice%==12 goto GERROR

:GERROR
echo Input not vaild,
pause 
goto GROUND

:LAYER
cls
echo %png%.dat 
echo id = %id%,
echo ground = %ground%,
echo.
echo Select the Default Layer by number:
echo 0. Lower
echo 1. Intermediate
echo 2. Upper

echo Enter Default Layer number here: 
set /p choice=""
if %choice%==0 (
set layer=0
goto XYPOS
)
if not %choice%==0 goto LONE
:LONE
if %choice%==1 (
set layer=1
goto XYPOS
)
if not %choice%==1 goto LTWO
:LTWO
if %choice%==2 (
set layer=2
goto XYPOS
)
if not %choice%==2 goto LERROR

:LERROR
echo Input not vaild,
pause 
goto LAYER

:XYPOS
echo Is there more than one image region related to this tile?
echo Select y or n:

set /p choice=""
if %choice%==y goto MULTI
if not %choice%==y goto XNEXT
:XNEXT
if %choice%==n goto SINGLE
if not %choice%==n goto ZERROR

:ZERROR
echo Input not vaild,
pause 
goto XYPOS

:SINGLE
echo please give the x,y coordinate of the related imagage region:
set /p x="x: "
set /p y="y: "
set x=%x%
set y=%y%
goto WIDTH

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
goto WIDTH

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
goto WIDTH

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
goto WIDTH

:WIDTH
cls
echo %png%.dat 
echo id = %id%,
echo ground = %ground%,
echo default_layer = %layer%,
echo x = %x%,
echo y = %y%,
echo.
echo Select the width in pixels:
echo Available widths:
echo 8
echo 16
echo 32
echo 64

set /p choice="Width is "
if %choice%==8 (
set width=8
goto HEIGHT
)
if not %choice%==8 goto N1
:N1
if %choice%==16 (
set width=16
goto HEIGHT
)
if not %choice%==16 goto N2
:N2
if %choice%==32 (
set width=32
goto HEIGHT
)
if not %choice%==32 goto N3
:N3
if %choice%==64 (
set width=64
goto HEIGHT
)
if not %choice%==64 goto WERROR

:WERROR
echo Input not vaild,
pause
goto WIDTH

:HEIGHT
cls
echo %png%.dat 
echo id = %id%,
echo ground = %ground%,
echo default_layer = %layer%,
echo x = %x%,
echo y = %y%,
echo width = %width%,
echo.
echo Select the height in pixels:
echo Available heights:
echo 8
echo 16
echo 32
echo 64

set /p choice="Height is "
if %choice%==8 (
set height=8
goto SCROLLING
)
if not %choice%==8 goto H1
:H1
if %choice%==16 (
set height=16
goto SCROLLING
)
if not %choice%==16 goto H2
:H2
if %choice%==32 (
set height=32
goto SCROLLING
)
if not %choice%==32 goto H3
:H3
if %choice%==64 (
set height=64
goto SCROLLING
)
if not %choice%==64 goto HERROR

:HERROR
echo Input not vaild,
pause
goto HEIGHT

:SCROLLING
cls
echo %png%.dat 
echo id = %id%,
echo ground = %ground%,
echo default_layer = %layer%,
echo x = %x%,
echo y = %y%,
echo width = %width%,
echo height = %height%,
echo.
echo Select the Scrolling type by number:
echo 0. None
echo 1. Parallax

echo Enter Scrolling type number here: 
set /p choice=""
if %choice%==0 (
set scrolling=NONE;
goto CHECK
)
if not %choice%==0 goto SONE
:SONE
if %choice%==1 (
set scrolling="parallax"
goto CHECK
)
if not %choice%==1 goto SERROR

:SERROR
echo Input not vaild,
pause
goto SCROLLING

:CHECK
cls
echo Line1: id = %id%,
echo Line2: ground = %ground%,
echo Line3: default_layer = %layer%,
echo Line4: x = %x%,
echo Line5: y = %y%,
echo Line6: width = %width%,
echo Line7: height = %height%,
echo Line8: scrolling = %scrolling%,
echo.
echo Please validate the entry.
echo Select a line number to edit.
echo If no edits are needed type 0.
set /p choice=""
if %choice%==1 goto EDITID
if not %choice%==1 goto EC2
:EC2
if %choice%==2 goto EDITGROUND
if not %choice%==2 goto EC3
:EC3
if %choice%==3 goto EDITLAYER
if not %choice%==3 goto EC4
:EC4
if %choice%==4 goto EDITX
if not %choice%==4 goto EC5
:EC5
if %choice%==5 goto EDITY
if not %choice%==5 goto EC6
:EC6
if %choice%==6 goto EDITWIDTH
if not %choice%==6 goto EC7
:EC7
if %choice%==7 goto EDITHEIGHT
if not %choice%==7 goto EC8
:EC8
if %choice%==8 goto EDITSCROLLING
if not %choice%==8 goto EC0
:EC0
if %choice%==0 (
if %scrolling%==NONE goto SKIP
if not %scrolling%==NONE goto PRINT
)
if not %choice%==0 goto CHERROR

:CHERROR
echo Input not vaild,
pause
goto CHECK

:PRINT
echo tile_pattern{>> %png%.dat
echo id = %id%,>> %png%.dat
echo ground = %ground%,>> %png%.dat
echo default_layer = %layer%,>> %png%.dat
echo x = %x%,>> %png%.dat
echo y = %y%,>> %png%.dat
echo width = %width%,>> %png%.dat
echo height = %height%,>> %png%.dat
echo scrolling = %scrolling%,>> %png%.dat
echo }>> %png%.dat
echo.>> %png%.dat
goto REPEAT

:SKIP
echo tile_pattern{>> %png%.dat
echo id = %id%,>> %png%.dat
echo ground = %ground%,>> %png%.dat
echo default_layer = %layer%,>> %png%.dat
echo x = %x%,>> %png%.dat
echo y = %y%,>> %png%.dat
echo width = %width%,>> %png%.dat
echo height = %height%,>> %png%.dat
echo }>> %png%.dat
echo.>> %png%.dat
goto REPEAT

:REPEAT
cls
echo Would you like to create another entry in the %png%.dat file?
echo Select y or n:

set /p choice="Make a selection and press Enter: "
if %choice%==y goto START
if not %choice%==y goto NEXT
:NEXT
if %choice%==n goto CLOSE
if not %choice%==n goto CERROR

:CERROR
echo Input not vaild,
pause
goto REPEAT

:CLOSE
start %png%.dat
exit

:EDITGROUND
cls
echo %png%.dat 
echo.
echo Select the GROUND type by number:
echo 1. "traversable"
echo 2. "wall"
echo 3. "shallow_water"
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
if %choice%==1 (
set ground="traversable"
goto CHECK
)
if not %choice%==1 goto CTWO
:CTWO
if %choice%==2 (
set ground="wall"
goto CHECK
)
if not %choice%==2 goto CTHREE
:CTHREE
if %choice%==3 (
set ground="shallow_water"
goto CHECK
)
if not %choice%==3 goto CFOUR
:CFOUR
if %choice%==4 (
set ground="deep_water"
goto CHECK
)
if not %choice%==4 goto CFIVE
:CFIVE
if %choice%==5 (
set ground="wall_top_right_water"
goto CHECK
)
if not %choice%==5 goto CSIX
:CSIX
if %choice%==6 (
set ground="wall_top_left_water"
goto CHECK
)
if not %choice%==6 goto CSEVEN
:CSEVEN
if %choice%==7 (
set ground="wall_bottom_right_water"
goto CHECK
)
if not %choice%==7 goto CEIGHT
:CEIGHT
if %choice%==8 (
set ground="wall_bottom_left_water"
goto CHECK
)
if not %choice%==8 goto CNINE
:CNINE
if %choice%==9 (
set ground="wall_top_right"
goto CHECK
)
if not %choice%==9 goto CTEN
:CTEN
if %choice%==10 (
set ground="wall_top_left"
goto CHECK
)
if not %choice%==10 goto CELV
:CELV
if %choice%==11 (
set ground="wall_bottom_left"
goto CHECK
)
if not %choice%==11 goto CTWL
:CTWL
if %choice%==12 (
set ground="wall_bottom_right"
goto CHECK
)
if not %choice%==12 goto GEERROR

:GEERROR
echo Input not vaild,
pause 
goto GROUNDEDIT

:EDITLAYER
cls
echo %png%.dat
echo.
echo Enter Default Layer number here: 
set /p choice=""
if %choice%==0 (
set layer=0
goto CHECK
)
if not %choice%==0 goto ELONE
:ELONE
if %choice%==1 (
set layer=1
goto CHECK
)
if not %choice%==1 goto ELTWO
:ELTWO
if %choice%==2 (
set layer=2
goto CHECK
)
if not %choice%==2 goto ELERROR

:ELERROR
echo Input not vaild,
pause 
goto EDITLAYER

:EDITWIDTH
cls
echo %png%.dat 
echo.
echo Select the width in pixels:
echo Available widths:
echo 8
echo 16
echo 32
echo 64

set /p choice="Width is "
if %choice%==8 (
set width=8
goto CHECK
)
if not %choice%==8 goto EN1
:EN1
if %choice%==16 (
set width=16
goto CHECK
)
:EN2
if %choice%==32 (
set width=32
goto CHECK
)
if not %choice%==32 goto EN3
:EN3
if %choice%==64 (
set width=64
goto CHECK
)
if not %choice%==64 goto EWERROR

:EWERROR
echo Input not vaild,
pause
goto EDITWIDTH

:EDITHEIGHT

cls
echo %png%.dat 
echo.
echo Select the height in pixels:
echo Available heights:
echo 8
echo 16
echo 32
echo 64

set /p choice="Height is "
if %choice%==8 (
set height=8
goto CHECK
)
if not %choice%==8 goto EH1
:EH1
if %choice%==16 (
set height=16
goto CHECK
)
if not %choice%==16 goto EH2
:EH2
if %choice%==32 (
set height=32
goto CHECK
)
if not %choice%==32 goto EH3
:EH3
if %choice%==64 (
set height=64
goto CHECK
)
if not %choice%==64 goto EHERROR

:EHERROR
echo Input not vaild,
pause
goto EDITHEIGHT

:EDITSCROLLING
cls
echo %png%.dat 
echo.
echo Select the Scrolling type by number:
echo 0. None
echo 1. Parallax

echo Enter Scrolling type number here: 
set /p choice=""
if %choice%==0 (
set scrolling=NONE;
goto CHECK
)
if not %choice%==0 goto ESONE
:ESONE
if %choice%==1 (
set scrolling="parallax"
goto CHECK
)
if not %choice%==1 goto ESERROR

:ESERROR
echo Input not vaild,
pause
goto EDITSCROLLING