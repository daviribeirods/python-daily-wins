# https://www.codewars.com/kata/563cf89eb4747c5fb100001b

def remove_smallest(numbers: list) -> list:
    if not numbers:
        return []
    
    smallest_rating = 100_000_000
    for i in numbers:
        if i <= smallest_rating:
            smallest_rating = i

    new_array = numbers.copy()
    new_array.remove(smallest_rating)

    return new_array

print(remove_smallest([5, 5, 1, 1, 2, 1, 3]))