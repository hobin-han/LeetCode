
def count(str):
    s_count = {}
    for s in str:
        if s in s_count:
            s_count[s] += 1
        else:
            s_count[s] = 1
    print("count:", s_count)

count("abccbscbcacb")

def two_sum_brute(list, num):
    a_dict = {}
    for i, n in enumerate(list):
        remain = num - n
        if remain in a_dict:
            return i, a_dict[remain]
        else:
            a_dict[n] = i

i1, i2 = two_sum_brute([-1, 2, 3, 4, 7], 5)
print("two sum brute:", i1, i2)

print("------------------")

# ------ Tips

# enumerate
nums = [2, 10, 5]
for i, n in enumerate(nums):
    print(i, n)