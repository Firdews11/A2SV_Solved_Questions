#1504B
t = int(input())
for _ in range(t):
    n = int(input())
    a = input()
    b = input()
    good = [0]*n
    zero = one = 0
    
    for i in range(n):
        if a[i] == '0':
            zero += 1
        else:
            one += 1
        
        if zero == one:
            good[i] = 1
    
    flip = 0
    
    for i in range(n-1, -1, -1):
        cur = a[i]
        if flip:
            cur = '1' if cur == '0' else '0'
        
        if cur != b[i]:
            if good[i] == 0:
                print("NO")
                break
            flip ^= 1
    else:
        print("YES")
