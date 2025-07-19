num_array = [1, 3, 7, 5, 8, 2, 4, 9, 6]

# ------ Linear Search
'''
Time Complexity:    O(N)
'''

def linear_search(num_array, num):
    for n in num_array:
        if n == num:
            return True
    return False
    
print(linear_search(num_array, 2))  # True
print(linear_search(num_array, 10)) # False

# (more simple way)

print(2 in num_array)   # True
print(10 in num_array)  # False

# ------ Binary Search
'''
use if the array is sorted.
Time Complexity:    O(logN)
'''

sorted_num_array = [1, 2, 3, 4, 6, 7, 8, 9, 10]

def binary_search(num_array, num):
    first_index = 0
    last_index = len(num_array) - 1

    while first_index <= last_index:        
        mid_index = (first_index + last_index) // 2
        mid_num = num_array[mid_index]
        
        if num == mid_num:
            return mid_index
        elif num < mid_num:
            last_index = mid_index - 1
        else:
            first_index = mid_index + 1
    
    return -1
        

print(binary_search(sorted_num_array, 10)) # 8

# ------ Tips

# ASCII Code
print(ord('0')) # 48
print(ord('A')) # 65
print(ord('a')) # 97

# array - get(index)
num_array[0]

# array - count
len(num_array)

# array - contains
print(2 in num_array)   # True

# Math - share
11 // 2 # 5