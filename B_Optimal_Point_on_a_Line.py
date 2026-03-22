a=int(input())
x=[int(i) for i in input().split()]
x.sort()
if a%2:
    print(x[a//2])
else:
    print(x[a//2 -1])
