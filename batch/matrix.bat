@echo off
color 02
:start
echo %random% %random% %random% %random% %random% %random% %random% %random%
PING 1.1.1.1 -n 1 -w 1 >NUL
goto start