import base64
import pwgen


def encode(string: str):
    unencoded = string
    bytes = unencoded.encode('ascii')
    b64_bytes = base64.b64encode(bytes)
    encoded = b64_bytes.decode('ascii')
    return encoded


def decode(string: str):
    encoded = string
    b64_bytes = encoded.encode('ascii')
    decoded_bytes = base64.b64decode(b64_bytes)
    decoded = decoded_bytes.decode('ascii')
    return decoded


if __name__ == "__main__":
    pw = pwgen.genPwd(32)
    encodedString = encode(pw)
    print("Encoded: " + encodedString + " | Decoded: " + decode(str(encodedString)) + " | Org.: " + pw)
    print("So... works fine :D")
