"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    
    popi = 1

    while popi < 6:
       
       result.insert(popi,"@")
       popi += 2
    
    return result  