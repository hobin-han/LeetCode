> reference: [Youtube Video (KR)](https://youtu.be/kWiCuklohdY?si=u86ScVyIOg_sw-qF)

# 0. Print & Comment
```python
print("hello world")

# Comments here...

'''
Multiple Comments
Here~~~~
Good~~~~
'''

name = input("Please enter your name.")
old = int(input("How old are you?"))
```

# 1. String
```python
'Hello'     # Hello
"hi"        # hi
"Hi" * 9    # HiHiHiHiHiHiHiHiHi

sentence1 = """hi
hello"""

sentence = "Hihi hello I am hobin."
sentence[0]     # H
sentence[2:4]   # hi
sentence[:4]    # Hihi `4 elements from the start`
sentence[-5:]   # obin. `5 elements from the end`

sentence.upper()    # HIHI HELLO I AM HOBIN.
sentence.lower()    # hihi hello i am hobin.

sentence[0].isupper()  # True

len(sentence) # 22

sentence.replace("I am", "I'm") # Hihi hello I'm hobin.

sentence.index("I")     # 11
sentence.index("h", 3)  # 5

sentence.find("Hobin")  # -1 `It's safe. Using index() will occur Error!`

sentence.count("h")     # 3

print("I am %s." % "hobin") # I am hobin. '%s'
print("I am %d years old." % 20) # I am 20 years old. '%d'
print("Apple starts with a letter %c!" % "A") # Apple starts with a letter A! '%c'

print("I am %s years old." % 20) # I am 20 years old. '%s'
print("I like %s, and %s." % ("blue", "red")) # I like blue, and red.

print("I am {} years old.".format(20)) # I am 20 years old. '%s'
print("I like {}, and {}.".format("blue", "red")) # I like blue, and red.
print("I like {1}, and {0}.".format("blue", "red")) # I like red, and blue.

print("I like {color}, and I am {age} years old.".format(color = "blue", age = 20)) # I like blue, and I am 20 years old.

"\n" # new line
"hi I am \"hobin\"!" # hi I am "hobin"!
```

# 2. Boolean
```python
print(5 > 10) // False
print(True) // True
print(not True) // False
print(not (5 > 10)) // True
```

# 3. Variable
```python
name = "Hobin"
age = 20
is_adult = age >= 19

# Hi I am Hobin! And I'm 20 years old.
print("Hi I am " + name + "! And I'm " + str(age) + " years old.")
# Hi I am Hobin ! And I'm 20 years old. (you dont need `str()`)
print("Hi I am", name, "! And I'm", age, "years old.")

age = 10
print("Is " + name + " adult? " + str(is_adult)) # Is Hobin adult? False
```
```python
num = 100

def minus(a):
  # if you want to use global variable inside of a function use 'global'
  # if you don't usee `global` it will occur Error!
  global num
  num -= a
  print(num)

def minus_ret(num, a):
  num = num - a
  print(num)
  return num

minus(2)    # 98
minus_ret(num, 2) # 98
```
# 4. Operator
```python
print(1+1) # 2
print(3-2) # 1
print(5*2) # 10
print(6/3) # 2
print(2**3) # 2^3 = 8
print(5%3) # 2 `remainder`
print(10%3) # 1 `remainder`
print(5//3) # 1 `share`

print(10 > 3) # True
print(4 >= 7) # False
print(3 == 3) # True
print(3 + 4 == 7) # True
print(1 != 3) # True
print(not (1 != 3)) # False

print((3 > 0) and (3 < 5)) # True `and`
print((3 > 0) & (3 < 5)) # True `&`

print((3 > 0) or (3 > 5)) # True `or`
print((3 > 0) | (3 > 5)) # True `or`

print(5 > 4 > 3) # True
print(5 > 4 > 7) # False

print(2 + 3 * 4) # 14
print((2 + 3) * 4) # 20

number = 10
number += 2 # 12
number *= 2 # 24
number -= 2 # 22
number /= 2 # 11
number %= 5 # 1
```

# 5. Math
```python
abs(-5)      # 5

pow(4, 2)    # 4^2 = 16
sqrt(16)     # 4 `square root`

max(5, 12)   # 12
min(5, 12)   # 5

round(3.14)  # 3
round(3.5)   # 4
floor(4.99)  # 4 `round down`
ceil(4.01)   # 5 `round up`

random()                  # 0.0 <= r < 1.0
random() * 10             # 0.0 <= r < 10.0
int(random() * 10 + 1)    # 1 ~ 10
int(random() * 45 + 1)    # 1 ~ 45

randrange(1, 46)          # 1 ~ 45
randint(1, 45)            # 1 ~ 45
```

# 6. Array
```python
int_array = [10, 20, 30]

int_array.index(30)       # 2
int_array.append(40)      # [10, 20, 30, 40]
int_array.insert(1, 50)   # [10, 50, 20, 30, 40]

int_array.pop()       # [10, 50, 20, 30]
int_array.append(20)  # [10, 50, 20, 30, 20]
int_array.count(20)   # 2
int_array.sort()      # [10, 20, 20, 30, 50]
int_array.reverse()   # [50, 30, 20, 20, 10]

int_array.clear()     # []

mix_list = ["hi", 20, True]

[1, 2, 3].extend(mix_list)  # [1, 2, 3, "hi", 20, True]
```

# 7. Dictionary
```python
dictionary = {3: "hihi", 100: "hello"}
dictionary[3]      # hihi
dictionary.get(3)  # hihi

dictionary[5]                # !Error will occur!
dictionary.get(5)            # None `It's safe (recommended)`
dictionary.get(5, "unknown") # unknown `set default value`

5 in dictionary     # False

dictionary[3] = "hi"     # {3: "hi", 100: "hello"}
dictionary[7] = "Wawooo" # {3: "hi", 100: "hello", 7: "Wawooo"}

del dictionary[3] # {100: "hello", 7: "Wawooo"}

dictionary.keys()      # [100, 7]
dictionary.values()    # ["hello", "Wawooo"]
dictionary.items()     # [(100, "hello"), (7, "Wawooo")]

dictionary.clear()     # []
```

# 8. Tuple
```python
greet = ("hi", "hello")

greet[0]     # hi
greet[1]     # hello

greet.add("Hi~~")  # tuple cannot be added
```

# 9. Set
```python
my_set = {1, 2, 3, 3, 3} # {1, 2, 3}

set1 = {1, 2, 3}
set2 = {2, 10}

set2.add(44)               # {2, 10, 44}

set1 & set2                # {2}
set1.intersection(set2)    # {2}

set1 | set2                # {1, 2, 3, 10, 44)
set1.union(set2)           # {1, 2, 3, 10, 44)

set1 - set2                # {1, 3}
set1.difference(set2)      # {1, 3}

set1.remove(2)             # {1, 3}
```

# 10. Type Conversion
```python
list = ["hi", "hello"]
menu = {"hi", "hello"}
list(menu)     # ["hi", "hello"]
tuple(menu)    # ("hi", "hello")
set(list)      # {"hi", "hello"}
```

# 11. Condition
```python
if {Condition 1}:
  # do something here
elif {Condition 2}:
  # do something here
else:
  # do something here
```

# 12. Loop
```python
for i in [1, 2, 3, 4, 5]:
  # do something here

for i in range(1, 6):
  # do something here

while {Condition 1}:
  # do something here

continue, break

int_array = [1, 2, 3, 4, 5]
int_array = [i + 100 for i in int_array]   # [101, 102, 103, 104, 105]

str_array = ["hi", "hello"]
str_array = [len(i) for i in str_array]
```

# 13. Function
```python
def print_description():
  print("hi")

print_description()

def add(a, b):
  return a + b

add(1, 2) # 3

def emit(a, b):
  return a, b

a, b = emit(1, 2)   # a: 1, b: 2

def hi(a, b = 20):
  return a + b

hi(10)  # 30
hi(a=10, b=40) # 50
```
