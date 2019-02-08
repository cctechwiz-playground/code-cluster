**Identify all lines over 80 characters:**
> Bash

```bash
grep -rn '.\{80,\}'

#easy access: (add to ~/.bash_aliases)
alias over80="grep -rn '.\{80,\}'"
```


**Get public IP address:**
> Bash

```bash
wget http://ipinfo.io/ip -qO -
(OR)
curl ipecho.net/plain; echo
```


**Pretty print json:**
> Python

```python
python -m json.tool <input.json> <pretty_output.json>
```


**Use netcat node as proxy:**
> Bash

```bash
mkfifo fifo && nc -l 8080 <fifo | nc proxy.site.ip 8080 >fifo
```


**View file permissions in octal form:**
> Bash

```bash
stat -c "%A %a %n" <file || dir>
```


**Control recursion depth of ls:**
> Bash

```bash
find . -mindepth 2 -maxdepth 2 -type d -ls
```


**Extract all tar files in directory:**
> Bash

```bash
for filename in *.tar.gz; do tar zxf $filename; done;
```


**Rename all files/directories to lowercase:**
> Bash

```bash
rename -f 'y/A-Z/a-z/' *
```


**View/modify devices allowed to wake the computer:**
> Powershell

```powershell
Powercfg -devicequery wake_armed
Powercfg -devicedisablewake "devicename"
Powercfg -deviceenablewake "devicename"
```


**Search for text in files in current directory:**
> Bash

```bash
grep --color -rni . -e "search text"

#easy access: (add to ~/.bash_aliases)
alias search="grep --color -rni . -e "
```


**Convert code file to pdf:**
> Bash (with vim)

```bash
vim -c 'hardcopy > output.ps' -c quit <input_file> && ps2pdf output.ps
```


**Serve up pwd files via HTTP:**
> Python

```python
python -m SimpleHTTPServer 8000
```


**Replace text recursively in all files from pwd down:**
> Bash

```bash
ag -l "search string" | xargs sed -i '' -e 's/from/to/g'
```



**Recursively update nested git repositories:**
> Bash

```bash
find . -type d -name .git -exec sh -c "cd \"{}\"/../ && pwd && git pull" \;
```



**Print the current time to the terminal:**
>Bash

```bash
while true; do tput clear; date +"%H : %M" | figlet -c -f big; sleep 1; done
```
