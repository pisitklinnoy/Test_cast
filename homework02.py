def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

test_cases = [
    ("AAAA", 3),      
    ("BBBBB", 4),    
    ("ABABABAB", 0),  
    ("BABABA", 0),    
    ("AAABBB", 4),   
    ("A", 0),        
    ("", 0),          
    ("ABBABBA", 2),  
    ("ABBAABB", 3),   
]

for i, (s, expected) in enumerate(test_cases, start=1):
    output = alternatingCharacters(s)
    print(f"Test Case {i}:")
    print(f"Input: \"{s}\"")
    print(f"Output: {output} (Expected: {expected})")
    print(f"✅ {'Pass' if output == expected else 'Fail'}\n")