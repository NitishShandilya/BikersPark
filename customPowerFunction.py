"""
User-defined power function
"""
def power(a,b):
    num = 1
    for i in range(b):
        num *= a
    return num

# Test
a=2
b=3
print power(a,b)