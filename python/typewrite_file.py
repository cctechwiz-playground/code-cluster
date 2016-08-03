#python typewrite_file.py ipTablesRules.txt
#python typewrite_file.py user_process_del_script.txt
#pip install pyautogui  (i used python 2.7)
import pyautogui
import sys
if len(sys.argv) != 2:
    print 'Args passed (%d) does not match expected (1)' % (len(sys.argv)-1)
    sys.exit()
myFilename = sys.argv[1]
with open(myFilename) as f:
	ff = f.read()
pyautogui.typewrite('5..4..3..2..1\n\n\n', interval=0.3)
pyautogui.typewrite(ff, interval=.025)