# ConvertToExe

## Structure

### `malware.pyw`

This is the main script (i.e. `malwar3.exe`) that will run on the engineering station.

You can compile it to a .exe file with `auto-py-to-exe` (onefile, window based, icon):

--disable-windowed-traceback ENABLE
--clean ENABLE
--upx-dir `NinjaCrane\drivers\upx-4.0.2-win64`
--debug noarchive

- `pyinstaller --noconfirm --onefile --windowed --icon "C:/***/NinjaCrane/Attacks/Modbus_packet_attack/ConvertToExe/malware_icon.ico"  "C:/***/NinjaCrane/Attacks/Modbus_packet_attack/ConvertToExe/malware.pyw"`

When running `malware.pyw`, it will modify a registery key to by-pass windows UAC (it should revert it back after attack is completed). 

See https://dzone.com/articles/bypassing-windows-10-uac-withnbsppython

 
### `malware_icon.ico`

Just an icon for the malware ;)