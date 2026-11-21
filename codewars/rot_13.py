ROT_MAP = {
    chr(ord('a') + i): chr(ord('a') + (i + 13) % 26) for i in range(26)
} | {
    chr(ord('A') + i): chr(ord('A') + (i + 13) % 26) for i in range(26)
}

def rot13(message):
    return ''.join(ROT_MAP.get(c, c) for c in message)


# BASE = ord('a')

# def rot13(message):
#     is_capital = a.lower()
#     cipher = ''.join([chr(((ord(c) - ord('a') + 13) % 26) + ord('a')) for c in message])
#     return cipher
