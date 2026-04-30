#1515D
from collections import Counter 
t = int(input())
for _ in range(t):
    n, l, r = map(int,input().split())
    c = list(map(int,input().split()))
    left = Counter(c[:l])
    right = Counter(c[l:])
    cost = 0
    for color in left:
        if color in right:
            m = min(left[color], right[color])
            left[color] -= m
            right[color] -= m

    l_rem = sum(left.values())
    r_rem = sum(right.values())

    if l_rem < r_rem:
        l_rem, r_rem = r_rem, l_rem
        surplus_counts = right
    else:
        surplus_counts = left

    diff = (l_rem - r_rem) // 2
    same_color_pairs = 0
    for color in surplus_counts:
        same_color_pairs += surplus_counts[color] // 2

    print(l_rem - min(diff, same_color_pairs))
