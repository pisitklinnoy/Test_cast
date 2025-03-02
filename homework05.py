def gridChallenge(grid):

    sorted_grid = [sorted(row) for row in grid]

    for col in range(len(sorted_grid[0])):
        for row in range(1, len(sorted_grid)):
            if sorted_grid[row][col] < sorted_grid[row - 1][col]:
                return "NO"
    
    return "YES"

test_cases = [
    (["ebacd", "fghij", "olmkn", "trpqs", "xywuv"], "YES"),  # ตัวอย่างจากโจทย์
    (["abc", "lmp", "qrt"], "YES"),  # ตารางเล็ก
    (["mpxz", "abcd", "wlmf"], "NO"),  # ตารางที่คอลัมน์ไม่เรียง
    (["abc", "bca", "cab"], "NO"),  # ตารางที่มีแถวเรียง แต่คอลัมน์ไม่เรียง
    (["a", "b", "c"], "YES"),  # ตารางแนวตั้ง
]

for i, (grid, expected) in enumerate(test_cases, start=1):
    output = gridChallenge(grid)
    print(f"Test Case {i}:")
    print(f"Input Grid: {grid}")
    print(f"Output: {output} (Expected: {expected})")
    print(f"✅ {'Pass' if output == expected else 'Fail'}\n")
