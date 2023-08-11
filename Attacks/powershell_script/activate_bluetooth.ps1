# Written by G. Renault
# This powershell command activates bluetooth

[CmdletBinding()] Param () If ((Get-Service bthserv).Status -eq 'Stopped') {Start-Service bthserv} Add-Type -AssemblyName System.Runtime.WindowsRuntime;$asTaskGeneric=([System.WindowsRuntimeSystemExtensions].GetMethods()|?{$_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0];Function Await($WinRtTask,$ResultType) {$asTask = $asTaskGeneric.MakeGenericMethod($ResultType);$netTask=$asTask.Invoke($null,@($WinRtTask));$netTask.Wait(-1) | Out-Null;$netTask.Result};[Windows.Devices.Radios.Radio,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;[Windows.Devices.Radios.RadioAccessStatus,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;Await ([Windows.Devices.Radios.Radio]::RequestAccessAsync()) ([Windows.Devices.Radios.RadioAccessStatus]) | Out-Null;$radios=Await ([Windows.Devices.Radios.Radio]::GetRadiosAsync()) ([System.Collections.Generic.IReadOnlyList[Windows.Devices.Radios.Radio]]);$bluetooth = $radios | ? {$_.Kind -eq 'Bluetooth'};[Windows.Devices.Radios.RadioState,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;Await ($bluetooth.SetStateAsync('On')) ([Windows.Devices.Radios.RadioAccessStatus]) | Out-Null

# ALTERNATIVE TO ACTIVATE WINDOWS FROM TERMINAL COMMANDS ONLY: 
# From terminal windows :
# 1. Create powershell file in desktop file
# cd %USERPROFILE%\Desktop
# mkdir powershell_script
# cd powershell_script
# .>bluetooth.ps1 2>NUL
# 2. And fill-in with the correct powershell command
# echo|set/p="[CmdletBinding()] Param () If ((Get-Service bthserv).Status -eq 'Stopped') {Start-Service bthserv} Add-Type -AssemblyName System.Runtime.WindowsRuntime;$asTaskGeneric=([System.WindowsRuntimeSystemExtensions].GetMethods()|?{$_.Name -eq 'AsTask' -and $_.GetParameters().Count -eq 1 -and $_.GetParameters()[0].ParameterType.Name -eq 'IAsyncOperation`1' })[0];Function Await($WinRtTask,$ResultType) {$asTask = $asTaskGeneric.MakeGenericMethod($ResultType);$netTask=$asTask.Invoke($null,@($WinRtTask));$netTask.Wait(-1) | Out-Null;$netTask.Result};[Windows.Devices.Radios.Radio,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;[Windows.Devices.Radios.RadioAccessStatus,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;Await ([Windows.Devices.Radios.Radio]::RequestAccessAsync()) ([Windows.Devices.Radios.RadioAccessStatus]) | Out-Null;$radios=Await ([Windows.Devices.Radios.Radio]::GetRadiosAsync()) ([System.Collections.Generic.IReadOnlyList[Windows.Devices.Radios.Radio]]);$bluetooth = $radios | ? {$_.Kind -eq 'Bluetooth'};[Windows.Devices.Radios.RadioState,Windows.System.Devices,ContentType=WindowsRuntime] | Out-Null;Await ($bluetooth.SetStateAsync('On')) ([Windows.Devices.Radios.RadioAccessStatus]) | Out-Null" >> bluetooth.ps1
# 3. Execute the powershell script
# powershell ./bluetooth.ps1 


# ===============
# + PRO TIPS: to run bluetooth.ps1 on every boot (i.e automatically activates bluetooth on startup on windows)
# BELOW WILL CREATE A SHORTCUT Hello.lnk that execute %USERPROFILE%\Desktop\powershell_script\bluetooth.ps1
# echo Set oWS = WScript.CreateObject("WScript.Shell") > CreateShortcut.vbs
# echo sLinkFile = "%USERPROFILE%\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup\Hello.lnk" >> CreateShortcut.vbs
# echo Set oLink = oWS.CreateShortcut(sLinkFile) >> CreateShortcut.vbs
# echo oLink.TargetPath = "powershell "& %USERPROFILE%\Desktop\powershell_script\bluetooth.ps1'"" >> CreateShortcut.vbs
# echo oLink.Save >> CreateShortcut.vbs
# cscript CreateShortcut.vbs
# del CreateShortcut.vbs
# ===============