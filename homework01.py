def funnyString(s):
    if len(s) <= 1:
        return "Funny"
    
    original_diffs = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    reversed_diffs = original_diffs[::-1]

    return "Funny" if original_diffs == reversed_diffs else "Not Funny"


test_cases = [
    ("abcba", "Funny"),
    ("abz", "Not Funny"),
    ("", "Funny"),  
    ("a", "Funny"),  
    ("๑๒๓", "Funny"),  
    ("a1B2", "Not Funny"),
    ("madam", "Funny"),
    ("abcdefgfedcba", "Funny"),
    ("a b c", "Not Funny"),  
    ("!@#$%^&*()", "Not Funny"),
    ("som", "Not Funny"),
    ("susi", "Not Funny"),
    ("12705", "Not Funny"),
    ("aie", "Not Funny"),
]
for i, (s, expected) in enumerate(test_cases, start=1):
    output = funnyString(s)
    print(f"Test Case {i}:")
    print(f"Input: \"{s}\"")
    print(f"Output: {output} (Expected: {expected})")
    print(f"✅ {'Pass' if output == expected else 'Fail'}\n")