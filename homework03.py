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
    ("abc", 3, "def"),
    ("xyz", 2, "zab"),  
    ("ABC", 3, "DEF"),
    ("Hello, World!", 5, "Mjqqt, Btwqi!"),  
    ("LOve", 2, "NQxg"),  
    ("som", 3, "vrp"),
    ("songtis", 5, "xtslynx"),  
    ("6710110289", 10, "6710110289"),  
    ("a b c", 3, "d e f"),  
    ("!@#$%^&*()", 4, "!@#$%^&*()"),  
]

for i, (s, k, expected) in enumerate(test_cases, start=1):
    output = caesarCipher(s, k)
    print(f"Test Case {i}:")
    print(f"Input: s = \"{s}\", k = {k}")
    print(f"Output: \"{output}\" (Expected: \"{expected}\")")
    print(f"✅ {'Pass' if output == expected else 'Fail'}\n")