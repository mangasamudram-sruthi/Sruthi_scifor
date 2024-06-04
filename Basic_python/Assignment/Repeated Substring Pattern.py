def repeated_substring_pattern(s):
    n = len(s)    
    # Check each possible length of the substring
    for i in range(1, n // 2 + 1):
        # If i is a divisor of n
        if n % i == 0:
            # Check if the substring s[:i] can be repeated to form s
            repeated = s[:i] * (n // i)
            if repeated == s:
                return True   
    return False
s1 = "abab"
print(repeated_substring_pattern(s1))  
s2 = "aba"
print(repeated_substring_pattern(s2))  
s3 = "abcabcabcabc"
print(repeated_substring_pattern(s3))  








# In[ ]:




