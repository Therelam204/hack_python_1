"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    
    popi = 0
    while popi < 6:
        result.append(popi)
        popi += 1
    
    result.reverse()
    return result  


