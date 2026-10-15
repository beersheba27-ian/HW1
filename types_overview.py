x = 0
while x < 5:
    print(x)
    x += 1
def exists(numbers, num):
    # numbers list of integers
    # num - being tested number for existence
    i = 0
    size = len(numbers)
    while i < size and numbers[i] != num:
        i += 1
    return i < size  
numbers = [10,20, 30] 
print(exists(numbers, 15)) # False
print(exists(numbers, 30)) # True




  
