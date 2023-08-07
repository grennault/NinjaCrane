# This deamon script allows to trigger over bluetooth the payload (A or B) to run by the USB Ninja cable
# Thanks to the Embedded Lab Vienna for IoT & Security (see https://wiki.elvis.science/index.php?title=Embedded_Lab_Vienna_for_IoT_%26_Security:About) for their help.

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


def deamon(BLE_address: str, password: bytes, payload: str, return_dict: bool):
    """Multiprocessing deamon that triggers over bluetooth the payload run by the USB Ninja cable)

        Args:
            BLE_address (str, required): Bluetooth address of the USB ninja cable. Defaults to BLE_address.
            password (bytes, required): Password of the USB Ninja cable (defined when running MSc_Project\\Attacks\\USBNinja\\Arduino_sketch\\NinjaBLESetup_MySetup_name_pwd\\NinjaBLESetup_MySetup_name_pwd.ino). Defaults to password.
            payload (str, required): Payload to trigger (stored in the USB Ninja arduino), either 'A' or 'B'. Defaults to "A".
            return_dict (bool, required): Return if connection to USB cable and payload trigger worked.
        """
    async def trigger_payload(BLE_address: str, password: str, payload: str):
        """Trigger over bluetooth the payload run by the USB Ninja cable)

        Args:
            BLE_address (str, optional): Bluetooth address of the USB ninja cable. Defaults to BLE_address.
            password (str, optional): Password of the USB Ninja cable (defined when running MSc_Project\\Attacks\\USBNinja\\Arduino_sketch\\NinjaBLESetup_MySetup_name_pwd\\NinjaBLESetup_MySetup_name_pwd.ino). Defaults to password.
            payload (str, optional): Payload to trigger (stored in the USB Ninja arduino), either 'A' or 'B'. Defaults to "A".
        """
        async with BleakClient(BLE_address) as client:

            service_nbr = 36
            try:
                await client.write_gatt_char(service_nbr, password)
            except:
                pass
            if payload == "A":
                await client.write_gatt_char(service_nbr, b'\x41\x3d\x4c\x0d\x0a')
            else:
                await client.write_gatt_char(service_nbr, b'\x42\x3d\x4c\x0d\x0a')

    try:
        asyncio.run(trigger_payload(BLE_address=BLE_address,
                    password=password, payload=payload))
        return_dict["success"] = True
    except:
        pass
