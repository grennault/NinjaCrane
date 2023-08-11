# This script allows to send over bluetooth keystrokes to the USB Ninja cable.

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


def convert_qwert_azert(message: str):
    """Converts qwerty to azerty keystrokes. The USB Ninja cable pro. injects keystrokes following a qwerty layout.
    To use the USB Ninja cable pro. as if it was using an azerty layout the sent keystrokes must be converted before.

    Args:
        message (str): Message to convert

    Returns:
        str: Converted message
    """
    return message.translate(
        str.maketrans(
            "qwertyuiop64asdfghjkl,8zxcvbn;mM1&é\"'(-è_çà+QWERTYUIOPASDFGHJKL?5ZXCVBN§:!/.1%3457ù9082",
            "azertyuiop^$qsdfghjklm*wxcvbn,;:!1234567890+AZERTYUIOPQSDFGHJKLM%WXCVBN?./><!\"#$%&'()*@",
        )
    )


if __name__ == "__main__":

    async def scan_BLE_devices_around():
        """Scan the bluetooth devices around and print their names, BLE address, details, and metadata.
        Use this function to find the BLE address of your USB Ninja cable pro..
        """
        devices = await BleakScanner.discover(timeout=10)
        print(devices)
        for d in devices:
            print(f"Address : {d.address}")
            print(f"Details : {d.details}")
            print(f"Metadata : {d.metadata}")
            print(f"Name : {d.name}")
            print(f"RSSI : {d.rssi}")

    # Scan the bluetooth devices around and print their names, BLE address, details, and metadata.
    asyncio.run(scan_BLE_devices_around())

    async def main(address):
        """Sends keystrokes to the USB Ninja cable pro. to open an Execute window, open a hidden command prompt, create a hello.txt file with a hello message inside it located in the /Destkop folder.

        Args:
            address (str): BLE address of the USB Ninja cable pro.
        """
        async with BleakClient(address) as client:
            # Sends the password to the cable (i.e., 8888)
            await client.write_gatt_char(handle, "8888".encode(), True)
            time.sleep(0.2)
            # Sends NEXTID:8
            await client.write_gatt_char(handle, "NEXTID:8".encode() + b"\x0a", True)
            time.sleep(0.2)
            # Sends REMOTE
            await client.write_gatt_char(handle, "REMOTE".encode() + b"\x0d\x0a", True)
            time.sleep(0.2)
            # Sends MSCONOFF 0
            await client.write_gatt_char(
                handle, "MSCONOFF 0".encode() + b"\x0d\x0a", True
            )
            time.sleep(0.2)
            # Sends USBON
            await client.write_gatt_char(handle, "USBON".encode() + b"\x0d\x0a", True)
            time.sleep(0.2)
            # Sends WINDOWS r (to open a Execute window)
            await client.write_gatt_char(
                handle, "WINDOWS r".encode() + b"\x0d\x0a", True
            )
            time.sleep(1)  # Waits the Execute window to open
            # Sends cmd /k powershell -windowstyle hidden -file .//nf.ps1 to open a hidden (i.e. in background) command prompt
            await client.write_gatt_char(
                handle,
                b"STRING "
                + convert_qwert_azert(
                    "cmd /k powershell -windowstyle hidden -file .//nf.ps1"
                ).encode()
                + b"\x0d\x0a",
                True,
            )
            time.sleep(0.5)
            await client.write_gatt_char(handle, "ENTER".encode() + b"\x0d\x0a", True)
            time.sleep(0.2)
            # Move to the /Desktop path
            await client.write_gatt_char(
                handle,
                b"STRING "
                + convert_qwert_azert("cd %USERPROFILE%//Desktop").encode()
                + b"\x0d\x0a",
                True,
            )
            time.sleep(0.5)
            await client.write_gatt_char(handle, "ENTER".encode() + b"\x0d\x0a", True)
            time.sleep(0.2)
            # Create a hello.txt file containing a hello message (i.e. echo hello>hello.txt)
            await client.write_gatt_char(
                handle,
                b"STRING " + convert_qwert_azert("echo hello").encode() + b"\x0d\x0a",
                True,
            )
            time.sleep(0.2)
            await client.write_gatt_char(handle, b"SHIFT \xfd" + b"\x0d\x0a", True)
            time.sleep(0.2)
            await client.write_gatt_char(
                handle,
                b"STRING " + convert_qwert_azert("hello.txt").encode() + b"\x0d\x0a",
                True,
            )
            time.sleep(0.2)
            await client.write_gatt_char(handle, "ENTER".encode() + b"\x0d\x0a", True)

    address = "F0:9E:C6:56:04:90"  # NOTE: Change this line with the BLE address of your USB Ninja cable pro.
    asyncio.run(
        main(address)
    )  # Calls the fct to create a hello.txt file in /Desktop location
