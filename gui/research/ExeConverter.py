# This script extracts raw data from an exe file and copy it into another exe file.
# This script could be used to extract raw data of an exe file and send them over bluetooth.
# This script has not been used as sending raw data over bluetooth was taking too much time.

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

import base64
import codecs
import multiprocessing
import bluetooth_send

exe_file_to_copy = "malwar3.exe"  # Name of the exe file to copy
exe_file_copy = "malwar3.exe"    # Name of the new copy
# USB Ninja cable professional BLE Address
BLE_address_pro_DEFAULT = "F0:9E:C6:56:04:90"
BLE_address = BLE_address_pro_DEFAULT
# Password is '8888' for USB Ninja professional cable
password_pro_DEFAULT = "8888"
password = password_pro_DEFAULT
cable = "USB Ninja cable"


def extract_raw_from_exe(exe_file_to_copy):
    # Extracts base64 raw data from an exe file
    with codecs.open(exe_file_to_copy, "rb") as f:
        raw_data = f.read()
        base64_encoded = base64.b64encode(raw_data)  # Encoded raw data
        # print("\\x" + "\\x".join(hex(char)[2:].zfill(2) for char in raw_data[:10]))
    return base64_encoded


def write_exe_from_raw(exe_file_copy, base64_encoded):
    # Writes base64 raw data to an exe file
    with codecs.open(exe_file_copy, "wb+") as f:
        base64_decoded = base64.b64decode(base64_encoded)
        f.write(base64_decoded)


def main():
    base64_encoded = extract_raw_from_exe(exe_file_to_copy)
    process1 = multiprocessing.Process(target=bluetooth_send.deamon, args=(
        BLE_address, password, base64_encoded, return_dict, cable))
    process1.start()
    process1.join()
