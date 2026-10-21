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
    # Ian: I didn't find a way of using slicing or list comprehension here.
    # I found system method ranodm.sample, but I think you want us not to use advanced built-in feachures for a while 
    result = []
    if min > max:
        min, max = max, min
    max_distinct_numbers = max - min + 1
    if size <= max_distinct_numbers:
        while len(result) < size:
            num = random.randint(min, max)
            if not exists(result, num):
                result.append(num)
    return result

print (distinct_random_numbers(1, 49, 7))
print (distinct_random_numbers(49, 1, 7))
print (distinct_random_numbers(-1, 7, 10))
print (distinct_random_numbers(-1, 7, 9))