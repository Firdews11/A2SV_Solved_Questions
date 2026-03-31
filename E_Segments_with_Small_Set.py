n ,k = map(int, input().split())
a = list(map(int,input().split()))
l = 0
ans = 0
freq = {}
for r in range(len(a)):
    freq[a[r]] = freq.get(a[r],0) +1
    while len(freq) > k:
        freq[a[l]] -=1
        if freq[a[l]] == 0:
           del freq[a[l]]
        l +=1
    ans += r - l +1
print (ans)
