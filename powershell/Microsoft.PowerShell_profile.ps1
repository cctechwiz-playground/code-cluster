New-Item alias:sb -value "C:\Program Files\Sublime Text 3\sublime_text.exe"
Clear-Host

Function sock_secure_coding {
	& 'C:\Program Files (x86)\Mozilla Firefox\firefox.exe' -P SecureCoding -no-remote
	ssh -D 8123 -C -q -N ctfsocks@ctf.martincarlisle.com
}

Function open($file) {
	ii $file
}

# From: https://github.com/mikemaccana/powershell-profile/blob/master/Microsoft.PowerShell_profile.ps1
function findfile($name) {
	ls -recurse -filter "*${name}*" -ErrorAction SilentlyContinue | foreach {
		$place_path = $_.directory
		echo "${place_path}\${_}"
	}
}