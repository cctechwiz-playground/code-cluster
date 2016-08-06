@rem Usefull Websites
:: http://ss64.com/nt/
:: http://academic.evergreen.edu/projects/biophysics/technotes/program/batch.htm
:: http://en.wikipedia.org/wiki/Batch_file
:: http://www.infionline.net/~wtnewton/batch/batguide.html


@rem Start of Code


@echo off
set string1=Hello World... Again

@echo Hello World
@echo off
pause >nul

cls
@echo %string1%
pause

cls
@echo That wasn't the "any key"...
@echo Press the any key to continue . . .
pause >nul

cls
@echo There you go!
@echo Bye bye...
SLEEP 1

exit