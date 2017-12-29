def f(n): 
    result = [n, 1, n+1, 0]
    return result[n%4]
    
def xor(a, b): 
    return f(a-1)^f(b)

def answer(start, length): 
    beginning = start
    checksum = 0
    for i in range(length, 0, -1): 
        checksum ^= xor(beginning, beginning + i - 1)
        beginning = beginning + length
    
    return checksum
            
answer(17, 4)