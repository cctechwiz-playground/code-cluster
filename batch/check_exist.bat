@echo off
:LOOP
if exist :C:\folder\file.txt"(
echo "File Found"
pause
) else (
goto LOOP
)
