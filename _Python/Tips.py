# ------ ASCII Code

# to ordinal
a = ord('0') # 48
a = ord('A') # 65
a = ord('a') # 97

# to character
a = chr(65) # A


# ------ str, chr

# char array to string
char_array = ['c', 'a', 't']
a = ''.join(char_array)

# append char to string
a = "" + 'a'

# string to char array
a = list("string")


# ------ Not & None

# not boolean
a = not True                # False

# not in
a = 1 not in [1, 2, 3]
a = not 2 in [1, 2, 3]

# is None
data = None
a = not data         # True
a = data is None     # True
a = data == None     # True


# ------ Math

# share
11 // 2 # 5


# ------ Set

# set
a = set([1, 3, 4, 1, 2])


# ------ Array

num_array = [1, 2, 3, 4, 5]

# length
a = len(num_array)

# get element
a = num_array[0]
a = num_array[-3]           # no error (; third element from the end)
# a = num_array[100000]     # ⚠️ error (; number is bigger than the length of array)

# has element
a = 2 in num_array          # True

# copy (array is reference type)
a = num_array.copy()

# insert
num_array.insert(3, -1)

# append
num_array.append(-1)

# add two arrays
num_array.extend([1, 2, 3])

# pop
num_array.pop()
num_array.pop(2)            # with index (but, time complexity: O(N))

# slice (it's safe 😍)
a = num_array[:1]           # index: first_index..<1
a = num_array[2:5]          # index: 2..<5
a = num_array[2:]           # index: 2...last_index
a = num_array[-1:5]         # (no error)
a = num_array[:90]          # (no error)

# ------ Loop

# enumerate
for i, n in enumerate([2, 10, 5]):
    break

# range (it's safe 😍)
for n in range(5):          # 0 <= n < 5
    break
for n in range(1, 3):       # 1 <= n < 3
    break
for n in range(1, 1):       # -
    break
for n in range(1, 0):       # -
    break


# ------ exchange values

a = 2
b = 5
a, b = b, a                 # here!


# ------ Reverse

# reversed str
a = ''.join(reversed("abcd"))   # 📌use ''.join() with reversed()

# reverse array
num_array.reverse()


# ------ Sort
# sorting in Python. this use Tim Sort(Hybrid Sorting Algorithm = it has several options on algorithms to use depends on situation)

# sorted
a = sorted([1, 2, 3])
a = sorted(sorted([1, 2, 3], reverse=True))
a = sorted(sorted(["hello", "ih", "hi", "hi there i am hobin", "hello2"], key=len))

# sort
num_array.sort()