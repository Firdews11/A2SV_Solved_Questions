t = int(input())
 
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    m = int(input())
    b = list(map(int, input().split()))
    sum_r = 0
    max_r = 0
    for x in r:
        sum_r += x
        if sum_r > max_r:
            max_r = sum_r
    sum_b = 0
    max_b = 0
    for x in b:
        sum_b += x
        if sum_b > max_b:
            max_b = sum_b
    
    print(max_r + max_b)
