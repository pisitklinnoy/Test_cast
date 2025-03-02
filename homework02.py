# ฟังก์ชันหลัก
def alternatingCharacters(s):
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

# ชุดทดสอบแบบแสดงผล
test_cases = [
    ("AABAAB", 2),
    ("AAAA", 3),
    ("ABABABAB", 0),
    ("BABABA", 0),
    ("AAABBB", 4),
    ("A", 0),
    ("", 0),
    ("ABBA", 1),
    ("ABBBA", 2),
    ("AAABBAA", 4),
]

# แสดงผลลัพธ์ในรูปแบบที่ต้องการ
for i, (s, expected) in enumerate(test_cases, start=1):
    output = alternatingCharacters(s)
    print(f"Test Case {i}:")
    print(f"Input: s = \"{s}\"")
    print(f"Output: {output}\n")
