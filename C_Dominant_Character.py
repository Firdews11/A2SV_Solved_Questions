t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    if n == 2 and s =='aa':
        print(2)
        
    elif n == 2 and s !='aa':
        print(-1)
    else:
        ans = float("inf")
        for i in range(n):
            for window in range(2,8):
                if i + window > n:
                    break
                a, b, c = 0, 0, 0 
                for j in range(i, i+ window):
                    if s[j] == "a":
                        a +=1
                    elif s[j] == "b":
                        b +=1
                    else:
                        c+=1
                if a>b and a>c:
                    ans = min(ans,window)
        if ans == float("inf"):
            print(-1)
        else:
            print(ans)
