import unittest

def gridChallenge(grid):
    # เรียงตัวอักษรในแต่ละแถว
    sorted_grid = [sorted(row) for row in grid]
    
    # ตรวจสอบแต่ละคอลัมน์ว่าต้องเรียงจากบนลงล่าง
    for col in range(len(sorted_grid[0])):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:  # ถ้าอักขระบน > ล่าง แสดงว่าไม่เรียง
                return "NO"
    
    return "YES"

class TestGridChallenge(unittest.TestCase):
    """ ทดสอบฟังก์ชัน gridChallenge """

    def setUp(self):
        """ เตรียม test cases """
        self.test_cases = [
            (["ebacd", "fghij", "olmkn", "trpqs", "xywuv"], "YES"),  # ตัวอย่างจากโจทย์
            (["abc", "lmp", "qrt"], "YES"),  # ตารางเล็ก
            (["mpxz", "abcd", "wlmf"], "NO"),  # ตารางที่คอลัมน์ไม่เรียง
            (["a", "b", "c"], "YES"),  # ตารางแนวตั้ง
            (["aaa", "aaa", "aaa"], "YES"),  # ตารางที่มีอักขระเดียวกัน
            (["zyx", "wvu", "tsr"], "NO"),  # ตารางที่แถวเรียงแล้ว แต่คอลัมน์ไม่เรียง
            (["z"], "YES"),  # ตาราง 1x1
            (["az", "by"], "NO"),  # ตาราง 2x2 ที่คอลัมน์ไม่เรียง
            (["ab", "cd"], "YES"),  # ตาราง 2x2 ที่คอลัมน์เรียงแล้ว
        ]

    def test_grid_challenge(self):
        """ ทดสอบว่า gridChallenge ให้ผลลัพธ์ถูกต้อง """
        print("\n=== Test Results ===")
        for i, (grid, expected) in enumerate(self.test_cases, start=1):
            with self.subTest(grid=grid):
                result = gridChallenge(grid)
                self.assertEqual(result, expected)

                # แสดงผลลัพธ์ของแต่ละ test case
                print(f"Test Case {i}:")
                print(f"Input Grid: {grid}")
                print(f"Output: {result} (Expected: {expected})")
                print(f"✅ {'Pass' if result == expected else '❌ Fail'}\n")

if __name__ == '__main__':
    unittest.main()
