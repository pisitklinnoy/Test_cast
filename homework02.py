import unittest

def alternatingCharacters(s):
    """คืนค่าจำนวนครั้งที่ต้องลบตัวอักษรเพื่อให้สลับกัน (ไม่มีตัวอักษรติดกันที่เหมือนกัน)"""
    deletions = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            deletions += 1
    return deletions

class TestAlternatingCharacters(unittest.TestCase):
    """ทดสอบฟังก์ชัน alternatingCharacters ด้วย unittest"""

    def setUp(self):
        """เตรียม test cases"""
        self.test_cases = [
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

    def test_alternatingCharacters(self):
        """ทดสอบว่าผลลัพธ์ของ alternatingCharacters ถูกต้อง"""
        print("\n=== Test Results ===")
        for i, (s, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(s=s):
                result = alternatingCharacters(s)
                self.assertEqual(result, expected)

                # แสดงผลลัพธ์ของแต่ละ test case
                print(f"Test Case {i}:")
                print(f"Input: \"{s}\"")
                print(f"Output: {result} (Expected: {expected})")
                print(f"✅ {'Pass' if result == expected else '❌ Fail'}\n")

if __name__ == '__main__':
    unittest.main()
