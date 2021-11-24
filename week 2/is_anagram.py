def isAnagram(s, t):
    s = sorted(s)
    t = sorted(t)
    if s == t:
        return True
    else:
        return False


s = "anagram"
t = "nagramaa"
print(isAnagram(s, t))
