n, s = map(int, input().split())
a = list(map(int, input().split()))
 
l = 0
curr_sum = 0
count = 0
 
for r in range(n):
    curr_sum += a[r]
    
    while curr_sum >= s:
        count += n - r
        curr_sum -= a[l]
        l += 1
 
print(count)
