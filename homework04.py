def is_alternating(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

def alternate(s):
    unique_chars = set(s)
    max_length = 0
    

    for char1 in unique_chars:
        for char2 in unique_chars:
            if char1 != char2:
                filtered = [c for c in s if c == char1 or c == char2]

                if is_alternating(filtered):
                    max_length = max(max_length, len(filtered))