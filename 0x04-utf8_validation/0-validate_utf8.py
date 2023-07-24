#!/usr/bin/python3
"""0.UTF-8 Validation"""


def validUTF8(data):
    """Write a method that determines if a given data set represents a valid
    UTF-8 encoding.
    Prototype: def validUTF8(data)
    Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to handle
    the 8 least significant bits of each integer
    """
    # check if data is valid argument:
    try:
        assert type(data) == list
        for num in data:
            assert type(num) == int
    except Exception:
        return False
    byte_stream = [format(num, '08b')[-8:] for num in data]
    stream_size = len(byte_stream)
    current_byte = 0
    # Itrerate over all bytes, inspecting for 0, 110, 1110 and 11110
    # plus checking that the following bytes begin with 10 for multi-byte chars
    while current_byte < stream_size:
        if byte_stream[current_byte][0] == '0':
            current_byte += 1
            continue
        elif byte_stream[current_byte][:3] == '110' and \
                current_byte + 1 < stream_size and \
                byte_stream[current_byte + 1][:2] == '10':
            current_byte += 2
            continue
        elif byte_stream[current_byte][:4] == '1110' and \
                current_byte + 2 < stream_size and \
                byte_stream[current_byte + 1][:2] == '10' and \
                byte_stream[current_byte + 2][:2] == '10':
            current_byte += 3
            continue
        elif byte_stream[current_byte][:5] == '11110' and \
                current_byte + 3 < stream_size and \
                byte_stream[current_byte + 1][:2] == '10' and \
                byte_stream[current_byte + 2][:2] == '10' and \
                byte_stream[current_byte + 3][:2] == '10':
            current_byte += 4
            continue
        # Can't continue
        return False

    return True


if __name__ == "__main__":
    pass
