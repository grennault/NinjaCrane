# This script allows to trigger over bluetooth the payload (A or B) to run by the USB Ninja cable.
# Requires to run this script in Windows OS with bluetooth capability.

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

if __name__ == "__main__":

    async def scan_BLE_devices_around():
        """Scan the bluetooth devices around and print their names, BLE address, details, and metadata.
        Use this function to find the BLE address of your USB Ninja cable.
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
        """Triggers the payload A, waits 3 seconds and then triggers the payload B of the USB Ninja cable.

        Args:
            address (str): BLE address of the USB Ninja cable
        """
        async with BleakClient(address) as client:

            # Prints the services of the USB Ninja cable
            # svcs = await client.get_services()
            # for service in svcs:
            #     print(service)

            # Prints the gatt characteristics of the handles of the USB Ninja cable
            # for i in range(1024):
            #    try:
            #        char = await client.read_gatt_char(i)
            #        print(f"Handle {hex(i)}: {char}")
            #    except:
            #        pass

            j = 36  # Handle number

            await client.write_gatt_char(
                j, b"\x35\x39\x37\x32"
            )  # NOTE: Change this with the password set of your USB Ninja cable (set by uploading an Arduino sketch to the cable, i.e. NinjaCrane/Attacks/USBNinja_payload/Arduino_sketch/NinjaBLESetup_MySetup_name_pwd).
            await client.write_gatt_char(
                j, b"\x42\x3d\x4c\x0d\x0a"
            )  # Triggers payload A
            print(f"Trigger BUTTON A done")

            time.sleep(3)  # Waits 3 sec

            await client.write_gatt_char(
                j, b"\x35\x39\x37\x32"
            )  # NOTE: Change this with the password set of your USB Ninja cable (set by uploading an Arduino sketch to the cable, i.e. NinjaCrane/Attacks/USBNinja_payload/Arduino_sketch/NinjaBLESetup_MySetup_name_pwd).
            await client.write_gatt_char(
                j, b"\x41\x3d\x4c\x0d\x0a"
            )  # Triggers payload B
            print(f"Trigger BUTTON B done")

    address = "CE:31:66:D0:67:EC"  # NOTE: Change this line with the BLE address of your USB Ninja cable
    asyncio.run(main(address))  # Calls the fct to trigger payload A then B.
