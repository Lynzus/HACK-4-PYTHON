"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    result2 = []
    i=0
    bandera = 1
    while i != len(result)+1:
        if bandera == 0:
            result.insert(i,'@')
            bandera = 1
            i+=1
        elif bandera == 1:
            bandera = 0
            i+=1
        print(result)
    return result  
fn_hack_9()