def is_anagram(s, t):
    # Check if the lengths are equal
    if len(s) != len(t):
        return False

    s_counts = Counter(s)

    for char in t:
        if char in s_counts:
            s_counts[char] -= 1
        else:
            return False
    
    # Check if all counts are zero
    for count in s_counts.values():
        if count != 0:
            return False
    
    return True

s1 = "anagram"
t1 = "nagaram"
print(is_anagram(s1, t1)) 

s2 = "rat"
t2 = "car"
print(is_anagram(s2, t2)) 





