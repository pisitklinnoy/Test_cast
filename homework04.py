import unittest

def is_alternating(s):
    """ ตรวจสอบว่าสตริงมีอักขระสลับกันหรือไม่ """
    return all(s[i] != s[i + 1] for i in range(len(s) - 1))

def alternate(s):
    """ หาความยาวมากที่สุดของสตริงที่เหลือเมื่อเลือกอักขระแค่ 2 ตัวและทำให้เป็น alternating """
    unique_chars = list(set(s))  
    max_length = 0

    for i in range(len(unique_chars)):
        for j in range(i + 1, len(unique_chars)):
            char1, char2 = unique_chars[i], unique_chars[j]
            
            # กรองเฉพาะอักขระ char1 และ char2
            filtered = "".join([c for c in s if c == char1 or c == char2])

            # เช็ค alternating โดยเก็บอักขระที่สลับกันเท่านั้น
            if is_alternating(filtered):
                max_length = max(max_length, len(filtered))
    
    return max_length


class TestAlternateFunction(unittest.TestCase):
    """ ทดสอบฟังก์ชัน alternate ด้วย unittest """

    def setUp(self):
        """ กำหนด test cases """
        self.test_cases = [
            ("beabeefeab", 5),  
            ("abcabc", 4),       
            ("aaaa", 0),         
            ("abababab", 8),     
            ("a", 0),            
            ("", 0),             
            ("xyxyx", 5),        
            ("zzxyx", 3),        
        ]

    def test_alternate(self):
        """ ทดสอบว่าผลลัพธ์ของ alternate ถูกต้อง """
        for s, expected in self.test_cases:
            with self.subTest(s=s):
                result = alternate(s)
                self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
