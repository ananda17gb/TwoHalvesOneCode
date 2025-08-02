def is_triangle(a, b, c):
    s1, s2, s3 = 0, 0, 0
    s1 = a + b    
    s2 = a + c    
    s3 = c + b    
    if s1 > c and s2 > b and s3 > a:
        return True
    return False

