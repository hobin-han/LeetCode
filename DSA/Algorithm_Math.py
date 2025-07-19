# ------ Binary Number

b = bin(16)
print("binary number:", b) # 0b10000 ('0b' means it's binary number)

# ------ Bitwise Operator ( &, | )
b1 = 0b10   # 2
b2 = 0b11   # 3
print("bitwise operator 1:", b1 & b2, b1 | b2)    # 2 3
print("bitwise operator 2:", 2 & 3, 2 | 3)        # 2 3

def is_even(n):
    return not n & 1 # same with `not (n & 1)`

print("is even 1:", is_even(3))
print("is even 2:", is_even(4))

def is_power(n):
    return n & (n - 1) == 0

print("is power 1:", is_power(0b1000))
print("is power 2:", is_power(0b1001))

# ------ FizzBuzz

def fizzbuzz(n):
    return ("Fizz" if n % 3 == 0 else "") + ("Buzz" if n % 5 == 0 else "")

print("fizzbuzz 1:", fizzbuzz(6))
print("fizzbuzz 2:", fizzbuzz(15))
print("fizzbuzz 3:", fizzbuzz(10))

# ------ Greatest Common Factor

def gcf(n1, n2):
    if n1 == 0 or n2 == 0:
        return None
    if n1 == 1 or n2 == 1:
        return 1
    
    gcf = None
    smaller = n1 if n1 <= 2 else n2

    for i in range(1, smaller + 1):
        if n1 % i == 0 and n2 % i == 0:
            gcf = i
    
    return gcf

print("greatest common factor:", gcf(20, 24))

# ------ Prime Number

def is_prime(n):
    if n <= 1:
        return False
        
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

print("is prime 1:", is_prime(7))
print("is prime 2:", is_prime(6))

def find_prime(n):
    # return [i for i in range(n + 1) if is_prime(i)]
    return [i for i in range(n + 1) if is_prime(i)]

print("find prime:", find_prime(100))