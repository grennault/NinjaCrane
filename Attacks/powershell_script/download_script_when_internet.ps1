# Written by G. Renault
# This script waits that computer has an internet access and download a file given url


# 1. Command to check internet connection : 
## if (0 -lt ((Get-NetRoute | ? DestinationPrefix -eq '0.0.0.0/0' | Get-NetIPInterface | Where ConnectionState -eq 'Connected') | measure -Line).Lines) {echo "You are connected to internet !"}

# 2. Command to download file given an url ($url) and save somewhere ($path)
$url = "https://download.wetransfer.com/eugv/c2...wM&cf=y"
$path = "path\to\file"

## SOLUTION 1
### $WebClient = New-Object System.Net.WebClient
### $WebClient.DownloadFile($url,$path)
## OR SOLUTION 2
### Invoke-WebRequest -Uri $url -OutFile $path


# Putting everything together :
# MAIN PROGRAM:
while (-not (0 -lt ((Get-NetRoute | ? DestinationPrefix -eq '0.0.0.0/0' | Get-NetIPInterface | Where ConnectionState -eq 'Connected') | measure -Line).Lines)) {
	Start-Sleep -Seconds 3
}
Invoke-WebRequest -Uri $url -OutFile $path

# ALTERNATIVE (putting everything in one line):
$url='https://bit.ly/AAAAAAA';$path='path\to\file';while(-not(0-lt((Get-NetRoute|? DestinationPrefix -eq '0.0.0.0/0'|Get-NetIPInterface|Where ConnectionState -eq 'Connected')|measure -Line).Lines)){Start-Sleep -Seconds 3}Invoke-WebRequest -Uri $url -OutFile $path