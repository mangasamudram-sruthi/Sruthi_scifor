def roman_to_int(s):
    
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}   
    # Initialize the result
    result = 0
    for i in range(len(s)):
        current_value = roman_map[s[i]]
        if i + 1 < len(s) and roman_map[s[i + 1]] > current_value:
            result -= current_value
        else:
            result += current_value
    
    return result
s1 = "III"
print(roman_to_int(s1))

s2 = "LVIII"
print(roman_to_int(s2))  

s3 = "MCMXCIV"
print(roman_to_int(s3))  


# In[ ]:




