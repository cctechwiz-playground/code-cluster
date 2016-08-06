:: output text to files


::Simple output
echo Hello >OutputSimple.txt


::Output with variable
set string=This is my string!

echo %string% >>OutputSimple.txt


::Output with 2 variables
set part1=Hello
set part2=World

echo %part1% %part2% >>OutputSimple.txt