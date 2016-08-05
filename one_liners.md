**Identify all lines over 80 characters:**
> Bash

```
grep -rn '.\{80,\}'
```


**Get public IP address:**
> Bash

```
wget http://ipinfo.io/ip -qO -
(OR)
curl ipecho.net/plain; echo
```


**Pretty print json:**
> Python

```
python -m json.tool <input.json> <pretty_output.json>
```


**Use netcat node as proxy:**
> Bash

```
mkfifo fifo && nc -l 8080 <fifo | nc proxy.site.ip 8080 >fifo
```


**View file permissions in octal form:**
> Bash

```
stat -c "%A %a %n" <file || dir>
```


**Control recursion depth of ls:**
> Bash

```
find . -mindepth 2 -maxdepth 2 -type d -ls
```


**Extract all tar files in directory:**
> Bash

```
for filename in *.tar.gz; do tar zxf $filename; done;
```


**View/modify devices allowed to wake the computer:**
> Powershell

```
Powercfg -devicequery wake_armed
Powercfg -devicedisablewake "devicename"
Powercfg -deviceenablewake "devicename"
```
