rem Created Thursday, May 13, 2010 - by Josh Maxwell, cctechwiz@hotmail.com

ECHO OFF
:MENU
CLS
ECHO.
ECHO .......................................................
ECHO .Welcome to the Automated ESRI Template Contoll Center.
ECHO .......................................................
ECHO.
ECHO 1 - Backup current ESRI settings.
ECHO 2 - Import saved settings into ESRI.
ECHO 3 - Restore to the default settings.
ECHO 4 - EXIT
ECHO.
SET /P M=Select 1, 2, 3 or 4, then press ENTER:
IF %M%==1 GOTO BACKUP
IF %M%==2 GOTO IMPORT
IF %M%==3 GOTO DEFAULT
IF %M%==4 GOTO EOF
:BACKUP
xcopy "C:\Documents and Settings\SUU\Application Data\ESRI" "ESRI"  /s /e /h /y
GOTO EOF
:IMPORT
xcopy "ESRI" "C:\Documents and Settings\SUU\Application Data\ESRI" /s /e /h /y
GOTO EOF
:DEFAULT
ECHO Are you sure you want to delete all the ESRI template files?
ECHO.
SET /P L= select y or n then press ENTER:
IF %L%==y GOTO YES
IF %L%==n GOTO MENU
:YES
Del "C:\Documents and Settings\SUU\Application Data\ESRI\*.*" /s /q
GOTO EOF 