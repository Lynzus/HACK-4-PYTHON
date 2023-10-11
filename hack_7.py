"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    i = 6
    while i != 0:
        result.append(i-1)
        i-=1
    return result  