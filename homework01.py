import unittest

def funnyString(s):
    """ตรวจสอบว่าสตริงเป็น 'Funny' หรือ 'Not Funny' ตามเงื่อนไขที่กำหนด"""
    if len(s) <= 1:
        return "Funny"
    
    original_diffs = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    reversed_diffs = original_diffs[::-1]

    return "Funny" if original_diffs == reversed_diffs else "Not Funny"

class TestFunnyString(unittest.TestCase):
    """ทดสอบฟังก์ชัน funnyString ด้วย unittest"""
    
    def setUp(self):
        """เตรียม test cases"""
        self.test_cases = [
            ("abcba", "Funny"),
            ("abz", "Not Funny"),
            ("", "Funny"),  # สตริงว่าง
            ("a", "Funny"),  # ตัวอักษรเดียว
            ("๑๒๓", "Funny"),  # ตัวเลขไทย
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

    def test_funnyString(self):
        """ทดสอบว่าผลลัพธ์ของ funnyString ถูกต้อง"""
        funny_count = 0
        not_funny_count = 0

        print("\n=== Test Results ===")
        for i, (s, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(s=s):
                result = funnyString(s)
                self.assertEqual(result, expected)
                
                # นับจำนวน Funny และ Not Funny
                if result == "Funny":
                    funny_count += 1
                else:
                    not_funny_count += 1
                
                # แสดงผลลัพธ์ของแต่ละ test case
                print(f"Test Case {i}:")
                print(f"Input: \"{s}\"")
                print(f"Output: {result} (Expected: {expected})")
                print(f"✅ {'Pass' if result == expected else '❌ Fail'}\n")

        # คำนวณเปอร์เซ็นต์
        total_cases = len(self.test_cases)
        funny_percentage = (funny_count / total_cases) * 100
        not_funny_percentage = (not_funny_count / total_cases) * 100

        # แสดงสรุปผลลัพธ์
        print("\n=== Results Summary ===")
        print(f'Funny: {funny_percentage:.2f}%')
        print(f'Not Funny: {not_funny_percentage:.2f}%')

if __name__ == '__main__':
    unittest.main()
