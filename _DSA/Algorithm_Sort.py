num_array = [32, 1, 9, 6, 5, 10, 16, 7, 8]

# ------ Bubble Sort
'''
It's the worst algorithm to sort, because it has the same time complexity even if the array is already sorted.
Don't use this 😨
------------------------------------
Time Complexity:    O(N**2)
'''

def bubble_sort(num_array):
    array_len = len(num_array)

    is_swapped = False
    for i in range(0, array_len - 1):
        for j in range(0, array_len -1 - i):
            if num_array[j] > num_array[j + 1]:
                is_swapped = True
                num_array[j], num_array[j + 1] = num_array[j + 1], num_array[j]
        if not is_swapped:
            return num_array
    return num_array

print("bubble sort:", bubble_sort(num_array.copy()))

# ------ Insertion Sort
'''
Similar to sorting your cards in your hand~
Better than Bubble Sort. Because if the array is already sorted, the time complexity would be O(N).
------------------------------------
Time Complexity:    O(N**2)
'''

def insertion_sort(num_array):
    sorted = [num_array[0]]
    for i in range(1, len(num_array)):
        num = num_array[i]
        is_added = False
        for j in range(i):
            if num < sorted[j]:
                sorted.insert(j, num)
                is_added = True
                break
        if not is_added:
            sorted.append(num)
    return sorted

print("insertion sort:", insertion_sort(num_array.copy()))

# ------ Selection Sort
'''
Find maximum value in the list and put it to the last~\
------------------------------------
Time Complexity:    O(N**2)
'''

def selection_sort(num_array):
    for i in range(len(num_array)):
        max_index = 0
        for j in range(len(num_array) - i):
            if num_array[j] > num_array[max_index]:
                max_index = j

        num_array[max_index], num_array[len(num_array) - i - 1] = num_array[len(num_array) - i - 1], num_array[max_index]

    return num_array

print("selection sort:", selection_sort(num_array.copy()))

# ------ Quick Sort
'''
Just pick one element and put things smaller to the left and bigger to the right~
And repeat it with recursion~
------------------------------------

'''

def quick_sort(num_array):
    if len(num_array) == 0:
        return []

    pivot_index = 0

    for i in range(1, len(num_array)):
        pivot = num_array[pivot_index]
        num = num_array[i]
        if pivot > num:
            pivot_index += 1
            num_array.pop(i)
            num_array.insert(0, num)
    
    left = num_array[:pivot_index]
    middle = num_array[pivot_index]
    right = num_array[pivot_index + 1:]
    return quick_sort(left) + [middle] + quick_sort(right)

print("quick sort:", quick_sort(num_array.copy()))

# ------ Merge Sort
'''
Slice to half until it became sorted(if the length of array becomes 1, it means sorted).
And merge those sorted arrays using recursion.
------------------------------------
Time Complexity:    O(n log(n))
Space Complexity:   O(n)
'''

def merge_sort(num_array):
    if len(num_array) <= 1:
        return num_array

    mid = len(num_array) // 2
    left = merge_sort(num_array[:mid])
    right = merge_sort(num_array[mid:])

    l = r = 0

    merging = []
    while l < len(left) and r < len(right):
        if left[l] <= right[r]:
            merging.append(left[l])
            l += 1 # 📌 rather than use `left.pop(0)`
        else:
            merging.append(right[r])
            r += 1 # 📌 rather than use `right.pop(0)`

    # Also you can try below, instead of `return merging + left[l:] + right[r:]`
    merging.extend(left[l:])
    merging.extend(right[r:])
    return merging

print("merge sort:", merge_sort(num_array.copy()))

print("-------------------------")

# ------ Tips

# array - reference type, so use `copy()`
num_array.copy()

# array - count
len(num_array)

# array - get element
print("(minus index)", num_array[-3])    # (no error)
# num_array[90]                          # ⚠️ error

# array - insert
copy = num_array.copy()
copy.insert(3, -1)
print("(insert)", copy)

# array - append (to the end)
copy = num_array.copy()
copy.append(-1)
print("(append)", copy)

# array - add two arrays
copy = num_array.copy()
copy.extend(num_array.copy())
print("(extend)", copy)

# array - pop
copy = num_array.copy()
copy.pop()
print("(pop last)", copy)
copy.pop(2) # pop with index (but it would have O(N) time complexity, be careful to use this 😒)
print("(pop index)", copy)

# array - slice, it's safe 😍
print("(slice from first to index)", num_array[:1])     # index: first_index..<1
print("(slice from index to index)", num_array[2:5])    # index: 2..<5
print("(slice from index to last)", num_array[2:])      # index: 2...last_index
print("(slice with invalid index)", num_array[-1:5])    # (no error)
print("(slice with invalid index)", num_array[:90])     # (no error)

# switch values
a = 2
b = 5
print("(switch value 1)", a, b) # 2 5
a, b = b, a
print("(switch value 2)", a, b) # 5 2

# boolean - !
print("(not boolean)", not True) # False

# loop - range , it's safe 😍
range(2)    # 0..<2
range(1, 2) # 1..<2
range(1, 1) # (no execute)
range(1, 0) # (no execute)

# sorting in Python. this use Tim Sort(Hybrid Sorting Algorithm = it has several options on algorithms to use depends on situation)
copy = num_array.copy()
print("(Python sorted)", sorted(copy))
print("(Python sorted reverse)", sorted(copy, reverse=True))
print("(Python sorted with key)", sorted(["hello", "ih", "hi", "hi there i am hobin", "hello2"], key=len))

copy.sort()
print("(Python sort)", copy)