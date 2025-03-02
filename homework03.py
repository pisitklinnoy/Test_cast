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

test_cases = [
    ("", 5, ""),                 
    ("som", 3, "vrp"),           
    ("songtis", 5, "xtslynx"),   
    ("6710110289", 10, "6710110289"),  
    ("LOve", 2, "NQxg"),         
    ("Hello, World!", 7, "Olssv, Dvysk!"),  
    ("Zebra-123!", 4, "Difve-123!") 
]

for i, (s, k, expected) in enumerate(test_cases, start=1):
    output = caesarCipher(s, k)
    print(f"Test Case {i}:")
    print(f"Input: s = \"{s}\", k = {k}")
    print(f"Output: \"{output}\"")
    print()