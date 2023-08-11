# Modbus_packet_attack

## Structure

### Folders

- `ConvertToExe`: Folder that contains the python malware file to convert in exe.
- `Malware`: Folder that contains the malware in exe format.
- `TentativeToBreakModbusEnc`: Folder that contains a PoC to crack (i.e., finds back a pre-image) the hash function of the Program and Sefety Protection password used by the modbus UMAS protocol.

### Files

- `explore-modbus.py`: Python script that illustrates how to compute the password hashes by giving an example. 

- `hash_fct.py`: Python script that contains the hashing algo. This code was not written by me but by Nicholas Miles from Tenable (see [Examining Crypto and Bypassing Authentication in Schneider Electric PLCs (M340/M580)](https://medium.com/tenable-techblog/examining-crypto-and-bypassing-authentication-in-schneider-electric-plcs-m340-m580-f37cf9f3ff34))

- `modipwn-atk-process.py`: Python script that reads a wireshark log capture of the UMAS protocol and extracts the password hashes, crafts an authenticated packet, and extracts information. This script must be modified according to the extracted info. length. The malware in `/ConvertToExe` folder is highly inspired from this script but the malware performs the attack on the fly and not in offline mode with a wireshark log capture.
