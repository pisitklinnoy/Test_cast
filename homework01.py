def funnyString(s):
    if len(s) <= 1:
        return "Funny"
    
    original_diffs = [abs(ord(s[i]) - ord(s[i - 1])) for i in range(1, len(s))]
    reversed_diffs = original_diffs[::-1]

    return "Funny" if original_diffs == reversed_diffs else "Not Funny"


# Test cases
test_cases = [
    "abcba", "abz", "", "a", "๑๒๓", "a1B2", "madam", "abcdefgfedcba",
    "a b c", "!@#$%^&*()", "som", "susi", "12705", "aie"
]

# Run tests and collect results
results = {s: funnyString(s) for s in test_cases}

# Count statistics
funny_count = sum(1 for result in results.values() if result == "Funny")
not_funny_count = sum(1 for result in results.values() if result == "Not Funny")

total_cases = len(test_cases)
funny_percentage = (funny_count / total_cases) * 100
not_funny_percentage = (not_funny_count / total_cases) * 100

# Display results
for s, result in results.items():
    print(f'Input: "{s}" -> Output: {result}')

# Display summary
print("\nResults Summary:")
print(f"Funny: {funny_percentage:.2f}%")
print(f"Not Funny: {not_funny_percentage:.2f}%")
