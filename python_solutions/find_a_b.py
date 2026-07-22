# https://www.codewars.com/kata/5714803d2817ffce17000a35/train/python

def find_a_b(numbers, c):
    if not numbers:
        return None
    
    index_j = 0
    for index_i, item_i in enumerate(numbers):
        index_j = index_i + 1
        
        while index_j < len(numbers):
            
            if c == numbers[index_i] * numbers[index_j]:
                return [numbers[index_i], numbers[index_j]]
            index_j += 1
    
    return None

print(find_a_b([-3,-2,-2,-1,0,1,2,3,4],4))