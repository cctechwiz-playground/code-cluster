echo "BLKSave", %CD%\working\block.blk > E:\FireMapperData\Macro\lps.csv
@echo off 
set INPUT = 
set /p INPUT=Please enter AOG: %=%
echo "AOG", %INPUT% >> E:\FireMapperData\Macro\lps.csv
@echo off 
set ZONE = 
set /p ZONE=Please enter UTM ZONE: %=%
echo "UTMZone", %ZONE% >> E:\FireMapperData\Macro\lps.csv
echo "DAT", %CD%\working\3aux.dat >> E:\FireMapperData\Macro\lps.csv
echo "RawDir", %CD%\raw\*.raw >> E:\FireMapperData\Macro\lps.csv
start E:\FireMapperData\Macro\lps.csv
start E:\FireMapperData\Macro\lps.exe
