def is_alternating(s):
    """ ตรวจสอบว่าสตริงมีอักขระสลับกันหรือไม่ """
    return all(s[i] != s[i + 1] for i in range(len(s) - 1))

def alternate(s):
    """ หาความยาวมากที่สุดของสตริงที่เหลือเมื่อเลือกอักขระแค่ 2 ตัวและทำให้เป็น alternating """
    unique_chars = list(set(s))  # ใช้ list เพื่อให้เข้าถึง index ได้เร็วขึ้น
    max_length = 0
    
    # ลองจับคู่ทุกตัวอักษรที่แตกต่างกัน
    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            
            # กรองเฉพาะอักขระ char1 และ char2
            filtered = [c for c in s if c == char1 or c == char2]
            
            # ตรวจสอบว่าเป็น alternating หรือไม่
            if is_alternating(filtered):
                max_length = max(max_length, len(filtered))
    
    return max_length  # คืนค่าความยาวสูงสุด


test_cases = [
    ("beabeefeab", 5),    # "babab" หรือ "abaea"
    ("abcabc", 4),        # "abab" หรือ "acac"
    ("aaaa", 0),          # ไม่มี alternating sequence ที่เป็นไปได้
    ("abababab", 8),      # ตัวมันเองเป็น alternating อยู่แล้ว
    ("a", 0),             # อักขระตัวเดียว ทำ alternating ไม่ได้
    ("", 0),              # สตริงว่าง
    ("xyxyx", 5),         # "xyxyx" (เป็น alternating อยู่แล้ว)
    ("abcde", 2),         # "ab", "ac", "ad", "ae", "bc", etc.
    ("aabbcc", 2),        # "ab", "ac", "bc" ได้แค่ 2 ตัว
    ("zzxyx", 3),         # "xyx"
]

for i, (s, expected) in enumerate(test_cases, start=1):
    output = alternate(s)
    print(f"Test Case {i}:")
    print(f"Input: s = \"{s}\"")
    print(f"Output: {output} (Expected: {expected})")
    print(f"✅ {'Pass' if output == expected else 'Fail'}\n")