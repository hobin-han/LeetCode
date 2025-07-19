# ------ Find Anagram

def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    return sorted(s1) == sorted(s2)

s1 = "Emperor Octavian"
s2 = "Captain over Rome"
print("is anagram:", is_anagram(s1, s2))

# ------ Find Palindrome

def is_palindrome(s):
    if len(s) <= 1:
        return True

    i = 0
    j = len(s) - 1
    while i < j:
        if s[i].lower() != s[j].lower():
            return False
        i += 1
        j -= 1
    return True

s = "Hannah"
print("is palindrome:", is_palindrome(s))

# ------ Find Last Number

def find_last_num(s):
    nums = [c for c in s if c.isdigit()]
    return nums[-1]

print("find last number:", find_last_num("h3k3k2j4k4l23lkkadfjkh"))

print("------------------------------")
# ------ Tips

# string - replace
print("(string replace)", "And I am Hobin".replace("Hobin", "hob"))
# string - lowercase, uppercase
print("(string lower)", "ABCDEFG".lower())
print("(string upper)", "abcdefg".upper())

# string, character - is digit
print("(is digit 1)", "123".isdigit())
print("(is digit 2)", 'c'.isdigit())

# List Comprehension
a_list = [c for c in ['a', 'b', 'A', 'c'] if c.lower() == 'a']
len_list = { len(c) for c in ["hi" , "hello", "      ", "hihi", "hobin", ""] if len(c.replace(' ', '')) > 0}
print("(list comprehension array)", a_list)
print("(list comprehension set)", len_list)