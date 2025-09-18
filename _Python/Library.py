# LeetCode에서 자주 쓰이는 Python 표준 라이브러리

"""
1. collections
----------------
- deque:
    - 양쪽 끝에서 O(1) 삽입/삭제 가능
    - BFS, 슬라이딩 윈도우 최적화에 사용
    - 예시::
        from collections import deque
        q = deque([start])
        while q:
            node = q.popleft()

- Counter:
    - 원소 빈도수 카운트
    - 다중 집합, 문자열 빈도 분석에 사용
    - 예시::
        from collections import Counter
        freq = Counter("leetcode")
        # {'l':1,'e':3,'t':1,'c':1,'o':1,'d':1}

- defaultdict:
    - 키가 없을 때 기본값 자동 생성
    - 그래프 인접 리스트, 그룹핑에 자주 활용
    - 예시::
        from collections import defaultdict
        graph = defaultdict(list)
        graph[1].append(2)
"""
import collections

q = collections.deque([1, 2, 3])
q.append(4)
first = q.popleft()
print("Deque:", list(q))

counter = collections.Counter("leetcode")
print("Counter:", dict(counter))

defaultdict = collections.defaultdict(list)
defaultdict[1].append(2)
defaultdict[2].append(3)
defaultdict[1].append(3)
defaultdict[3].append(4)
graph = dict(defaultdict)
print("DefaultDict:", graph)

"""
2. heapq
----------
- 최소 힙(min-heap) 구현
- 우선순위 큐, 다익스트라, k번째 원소 문제에 활용
- 주요 함수:
    - heapify(list): 리스트를 힙 구조로 변환
    - heappush(heap, item): 원소 삽입
    - heappop(heap): 최소값 꺼내기
    - nlargest(k, iterable): 상위 k개 큰 값
- 예시::
    import heapq
    nums = [3,2,1,5,6,4]
    heapq.heapify(nums)
    smallest = heapq.heappop(nums)
"""
import heapq

heap = [3, 2, 1, 5, 6, 4]
heapq.heapify(heap)
smallest = heapq.heappop(heap)
k_largest = heapq.nlargest(2, [3, 2, 1, 5, 6, 4])
print("Heap:", heap)
print("Smallest:", smallest)
print("K Largest:", k_largest)

"""
3. bisect
-----------
- 정렬된 배열에서 이진 탐색 지원
- lower/upper bound 구현에 사용
- 주요 함수:
    - bisect_left(arr, x): x 이상이 처음 나오는 위치
    - bisect_right(arr, x): x 초과가 처음 나오는 위치
    - insort(arr, x): 정렬된 상태 유지하며 삽입
- 예시::
    import bisect
    arr = [1,3,3,5,7]
    i = bisect.bisect_left(arr, 3)   # 1
    j = bisect.bisect_right(arr, 3)  # 3
"""
import bisect

arr = [1, 3, 3, 5, 7]
i = bisect.bisect_left(arr, 3)
j = bisect.bisect_right(arr, 3)
bisect.insort(arr, 4)
print("Bisect Left:", i)
print("Bisect Right:", j)
print("Insorted Array:", arr)

"""
4. functools
---------------
- cmp_to_key:
    - 정렬 기준을 함수로 정의 가능
    - 커스텀 문자열/숫자 정렬 문제에 사용
    - 예시::
        from functools import cmp_to_key
        arr.sort(key=cmp_to_key(lambda a,b: -1 if a+b>b+a else 1))

- lru_cache:
    - 함수 호출 결과 캐싱
    - DFS + 메모이제이션 (DP)에 유용
    - 예시::
        from functools import lru_cache
        @lru_cache(None)
        def fib(n):
            if n<2: return n
            return fib(n-1)+fib(n-2)
"""
import functools

cmp_func = lambda a, b: -1 if a + b > b + a else 1
arr_str = ["3", "30", "34", "5", "9"]
arr_str.sort(key=functools.cmp_to_key(cmp_func))
print("Sorted Strings:", arr_str)

"""
5. itertools
---------------
- 순열, 조합, 곱집합, 누적합 지원
- 백트래킹/조합 문제에서 자주 사용
- 주요 함수:
    - permutations(iterable, r)
    - combinations(iterable, r)
    - product(iterable, repeat)
    - accumulate(iterable)
- 예시::
    from itertools import permutations
    list(permutations([1,2,3], 2))
    # [(1,2),(1,3),(2,1),(2,3),(3,1),(3,2)]
"""
import itertools

def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
print("Fibonacci(5):", fib(5))

perms = list(itertools.permutations([1, 2, 3], 2))
print("Permutations:", perms)

"""
6. math
---------
- 수학/수론 문제에서 자주 사용
- 주요 함수:
    - gcd(a, b), lcm(a, b)
    - factorial(n)
    - sqrt(x), ceil(x), floor(x)
- 예시::
    import math
    g = math.gcd(48, 18)   # 6
"""
import math

g = math.gcd(48, 18)
print("GCD(48,18):", g)

factorial_5 = math.factorial(5)
sqrt_16 = math.sqrt(16)
ceil_4_2 = math.ceil(4.2)
floor_4_7 = math.floor(4.7)
print("Factorial(5):", factorial_5)
print("Sqrt(16):", sqrt_16)
print("Ceil(4.2):", ceil_4_2)
print("Floor(4.7):", floor_4_7)

"""
7. string
-----------
- 아스키 문자 집합 제공
- 주요 상수:
    - ascii_lowercase: 'abcdefghijklmnopqrstuvwxyz'
    - ascii_uppercase: 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    - digits: '0123456789'
- 예시::
    import string
    letters = string.ascii_lowercase
"""
import string

digits = string.digits
uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
print("Digits:", digits)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)