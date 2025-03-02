def caesarCipher(s, k):
    encrypted = []
    k = k % 26
    for char in s:
        if 'a' <= char <= 'z': 
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
        elif 'A' <= char <= 'Z': 
            new_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
        else:
            new_char = char
        encrypted.append(new_char)
    return "".join(encrypted)