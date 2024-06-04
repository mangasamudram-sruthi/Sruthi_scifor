def merge(word1: str, word2: str) -> str:
    merged_string = []
    i, j = 0, 0
    while i < len(word1) and j < len(word2):
        merged_string.append(word1[i])
        merged_string.append(word2[j])
        i += 1
        j += 1
    if i < len(word1):
        merged_string.extend(word1[i:])
    if j < len(word2):
        merged_string.extend(word2[j:])
    return ''.join(merged_string)
word1 = "def"
word2 = "hi"
print(merge(word1, word2))  







