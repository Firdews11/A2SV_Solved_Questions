from collections import Counter
 
n,m = map(int,input().split())
a1 = list(map(int,input().split()))
a2 = list(map(int,input().split()))
ans =0
counts =Counter(a1)
counts2 = Counter(a2)
for values in counts:
    if values in counts2:
        ans+= counts[values]*counts2[values]
print(ans)
