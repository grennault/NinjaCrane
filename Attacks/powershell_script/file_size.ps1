# Written by G. Renault
# This script get the file size

$path="path/to/malware.exe"

while(((Get-Item $path).length/1KB) -lt 41000){Start-Sleep -Seconds 3}Start-Sleep -Seconds 20;Start-Process -FilePath $path;