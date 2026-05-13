# Minha solução
def collinearity(x1, y1, x2, y2):
    # Tratar os casos de vetores na origem
    if x1==0 and y1==0:
        return True
    if x2==0 and y2==0:
        return True
    
    # Casos em que um dos valores é zero
    if x1==0:
        if x2==0:
            return True
        else:
            return False

    if x2==0:
        if x1==0:
            return True
        else:
            return False
    
    if y1==0:
        if y2==0:
            return True
        else:
            return False
    
    if y2==0:
        if y1==0:
            return True
        else:
            return False

    ratio_of_x = x1/x2
    ratio_of_y = y1/y2

    if ratio_of_x==ratio_of_y:
        return True
    return False

# Melhor solução da comunidade 
#def collinearity(x1, y2, x2, y2):
#    return x1 * y2 == x2 * y1

# Testes
#(1,1,1,1) ➞ true
#(1,2,2,4) ➞ true
#(1,1,6,1) ➞ false
#(1,2,-1,-2) ➞ true
#(1,2,1,-2) ➞ false
#(4,0,11,0) ➞ true
#(0,1,6,0) ➞ false
#(4,4,0,4) ➞ false
#(0,0,0,0) ➞ true
#(0,0,1,0) ➞ true
#(5,7,0,0) ➞ true