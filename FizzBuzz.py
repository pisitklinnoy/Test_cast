import unittest

def fizzbuzz(x):
    if x % 3 == 0 and x % 5 == 0:
        return "FizzBuzz"
    elif x % 3 == 0:
        return "Fizz"
    elif x % 5 == 0:
        return "Buzz"
    else:
        return str(x)

class TestFizzBuzz(unittest.TestCase):
    def test_fizz(self):
        """Test Case 1: เลขที่หาร 3 ลงตัว"""
        for num in [3, 6, 9, 12, 18]:
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), "Fizz")

    def test_buzz(self):
        """Test Case 2: เลขที่หาร 5 ลงตัว"""
        for num in [5, 10, 20, 25]:
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), "Buzz")

    def test_fizzbuzz(self):
        """Test Case 3: เลขที่หาร 3 และ 5 ลงตัว"""
        for num in [15, 30, 45, 60]:
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), "FizzBuzz")

    def test_number(self):
        """Test Case 4: เลขที่ไม่หาร 3 หรือ 5 ลงตัว"""
        for num in [1, 2, 4, 7, 8]:
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), str(num))

    def test_edge_cases(self):
        """Test Case 5: ขอบเขตพิเศษ เช่น 0 และเลขติดลบ"""
        test_data = {
            0: "FizzBuzz",  # 0 ควรเป็น FizzBuzz เพราะหารได้ทั้ง 3 และ 5
            -3: "Fizz",
            -5: "Buzz",
            -15: "FizzBuzz"
        }
        for num, expected in test_data.items():
            with self.subTest(num=num):
                self.assertEqual(fizzbuzz(num), expected)

if __name__ == "__main__":
    unittest.main()