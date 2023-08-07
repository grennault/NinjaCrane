# This script extracts raw data from an exe file and copy it into another exe file.
# This script could be used to extract raw data of an exe file and send them over bluetooth.

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

exe_file_to_copy = "HiJack.exe"  # Name of the exe file to copy
exe_file_copy = "HiJack1.exe"    # Name of the new copy

with codecs.open(exe_file_to_copy, "rb") as f:
    raw_data = f.read()
    base64_encoded = base64.b64encode(raw_data)  # Encoded raw data
    # print("\\x" + "\\x".join(hex(char)[2:].zfill(2) for char in raw_data[:10]))

with codecs.open(exe_file_copy, "wb+") as f:
    base64_decoded = base64.b64decode(base64_encoded)
    f.write(raw_data)
