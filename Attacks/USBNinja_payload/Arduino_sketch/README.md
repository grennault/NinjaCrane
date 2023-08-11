# Arduino_sketch

This folder contains Arduino sketch to upload on USB Ninja cable.

## Structure

- `NinjaBLESetup_MySetup_name_pwd`: Arduino sketch to set the name and the password of the USB Ninja cable with "CompromisedCable" and "5972" respectively.
  
- `BLERemoteKeyboard_activate_bluetooth_powershell`: Arduino sketch for the USB Ninja cable. Payload A: activates the bluetooth of the computer by writing and executing a powershell.

- `BLERemoteKeyboard_dump_arduin_PRGRM_mem`: Arduino sketch for the USB Ninja cable. Payload A dumps the inner memory of the USB Ninja cable into a file.

- `BLERemoteKeyboard_attack_process_no_wifi`: Arduino sketch for the USB Ninja cable. Payload A: executes the malware (that is assumed to be already on the victim's PC). Payload B: writes to a file. This can be used to inform the malware running on the PC to perform some action.

- `BLERemoteKeyboard_download_file_attack_process_wifi`: Arduino sketch for the USB Ninja cable. Payload A: waits for an internet connection and then downloads and executes the malware. Payload B: writes to a file. This can be used to inform the malware running on the PC to perform some action. WARNING: You must modify the tiny url in the arduino sketch so that it points toward a malware.exe file. For more information about how to do this, please check-out the `/NinjaCrane/Attacks/powershell_script`

- `BLERemoteKeyboard_receive_file_from_bluetooth`: Arduino sketch for the USB Ninja cable. Payload A: opens the bluetooth parameters of the Windows OS, activates bluetooth and waits to receive a bluetooth file. Payload B: accepts the receiving bluetooth file. 

- `BLERemoteKeyboard_detect_buttonB_push`: Arduino sketch for the USB Ninja cable. Payload A: opens a text file that writes if pin associated to payload trigger A or B is low or high (by using `digitalRead(BUTTONAPIN)`). Payload B: Nonne. This script could be usefull to understand the timing of the rising/falling edge of the trigger payload bit.

## Description

The arduino sketches presents some leads to:
- Setup the name and password of the USB Ninja cable.
- Hide the HID keystrokes injection by exploiting a tiny bug in windows.
- Detect an internet connection on PC and download a malwar3.exe from a server.
- Activates blutooth by writing a powershell script or by naviagating in the bluetooth parameters.
- Receive a file from bluetooth by naviagating in the bluetooth parameters.
- Dump USB Ninja cable memory

As you can see, the arduino sketch writes

### Notes


#### Bug description

When running in a terminal a script that crashes the keyboard selection stays in this command terminal.

For example when running below command in the windows runner, its opens an hidden terminal window and tries to execute the nf.ps1 file since nf.ps1 file does not exist the command will fail but one can still type with the keyboard some commands in the terminal.

`cmd /k powershell -windowstyle hidden -file .\\nf.ps1`

#### Execute window (i.e. Windows Runner) saves all the entries entered by a user

Below are the commands to clear/disable the Windows Runner (open by Win + R) by modifying the registers.

Disable run command history :
`REG ADD HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\Advanced /v Start_TrackProgs /t REG_DWORD /d 1`

Delete run command history :
REG DELETE HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Explorer\RunMRU /f

The arduino sketch `BLERemoteKeyboard_attack_process_no_wifi` does this by default.


##### How to generate a tiny url that points to the malware.exe file ?

Check the `/NinjaCrane/Attacks/powershell_script/read_me`. 
