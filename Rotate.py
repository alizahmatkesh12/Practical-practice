"""
        For example,
    rotate("hello", 2) return "llohe"
    rotate("hello", 5) return "hello"
    rotate("hello", 6) return "elloh"
    rotate("hello", 7) return "llohe"
    rotate("hello", 102) return "lohel"
    
"""

def rotate(s, k):
    double_s = s * (k // len(s) + 2)          # s + s
    if k <= len(s):
        return double_s[k: k + len(s)]
    else:
        return double_s[k - len(s):k]
    
print(rotate("hello", 2))
