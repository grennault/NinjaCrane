# G. Renault 18/07/23
# This scripts computes the different hash used during a Modbus/UMAS communication.
from hashlib import sha256
import base64
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


# Variables deduced by simply observing the communication (i.e., public var.)
salt1 = "50iiBJuyhpk="
hash1 = "zpEsnhyOxtgg/Z/IXIgDEyd/voAiPDv2hp7OP7ZDo6g="
salt2 = "gKemcCBaPRg="
hash2 = "gqT6C49A4TuSef1vxzQAi5TttxhnwRg4Tqu9Xy+0tEQ="
enc_pwd = "37713D7S6"
salt3 = "6Umv13jYhak="
hash3 = "XBhpWAvOQj/l67B7SV00wh03M+7KO/sMstr2Teed/54="

# Variables set by the user (i.e., private var.)
app_pwd = "application"
prgrm_pwd = "password"
data_pwd = "datadownload"
firmware_pwd = "fwdownload"


assert sha256_digest(base64.b64decode(salt1) +
                     data_pwd.encode(encoding="utf-16-le"), True) == hash1, "hash1 != SHA256(salt1 + prgrm_pwd)"

assert sha256_digest(base64.b64decode(salt2) +
                     firmware_pwd.encode(encoding="utf-16-le"), True) == hash2, "hash2 != SHA256(salt2 + firmware_pwd)"

assert sha256_digest(base64.b64decode(salt3) +
                     app_pwd.encode(encoding="utf-16-le"), True) == hash3, "hash3 != SHA256(salt3 + app_pwd)"

print("hash1 == SHA256(salt1 + prgrm_pwd)")
print("hash2 == SHA256(salt2 + firmware_pwd)")
print("hash3 == SHA256(salt3 + app_pwd)")
