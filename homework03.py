import unittest

def caesarCipher(s, k):
    """เข้ารหัสซีซาร์โดยเลื่อนอักษรตามค่าของ k"""
    encrypted = []
    k = k % 26  # ป้องกันค่า k เกิน 26 รอบ
    for char in s:
        if 'a' <= char <= 'z': 
            new_char = chr(((ord(char) - ord('a') + k) % 26) + ord('a'))
        elif 'A' <= char <= 'Z': 
            new_char = chr(((ord(char) - ord('A') + k) % 26) + ord('A'))
        else:
            new_char = char  # คงค่าเดิมถ้าไม่ใช่ตัวอักษร
        encrypted.append(new_char)
    return "".join(encrypted)

class TestCaesarCipher(unittest.TestCase):
    """ทดสอบฟังก์ชัน caesarCipher ด้วย unittest"""

    def setUp(self):
        """เตรียม test cases"""
        self.test_cases = [
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

    def test_caesarCipher(self):
        """ทดสอบว่าผลลัพธ์ของ caesarCipher ถูกต้อง"""
        print("\n=== Test Results ===")
        for i, (s, k, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(s=s, k=k):
                result = caesarCipher(s, k)
                self.assertEqual(result, expected)

                # แสดงผลลัพธ์ของแต่ละ test case
                print(f"Test Case {i}:")
                print(f"Input: s = \"{s}\", k = {k}")
                print(f"Output: \"{result}\" (Expected: \"{expected}\")")
                print(f"✅ {'Pass' if result == expected else '❌ Fail'}\n")

if __name__ == '__main__':
    unittest.main()
