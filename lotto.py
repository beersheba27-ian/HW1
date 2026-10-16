import random
def exists(numbers: list[int], num: int) -> bool:
    """
    returns True if "num" exists in list "numbers" otherwise False
    """
    return num in numbers

def distinct_random_numbers(min: int, max: int, size: int) -> list[int]:
    """
    
    returns list with "size" distinct random numbers 
    each number >= "min" and <= "max"
    if creating "size" distinct random numbers is impossible, return empty array
    requirement: to use the above function "exists" and one while-loop
    """
    result = []
    i = 0
    max_distinct_numbers = max - min + 1
    if size > max_distinct_numbers:
        return result
    while i < size:
        num = random.randrange(min, max+1)
        if not exists(result, num):
            result.append(num)
            i += 1
    return result

print (distinct_random_numbers(-1, 7, 10))
print (distinct_random_numbers(-1, 7, 9))