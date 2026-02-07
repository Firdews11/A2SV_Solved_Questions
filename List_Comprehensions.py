if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    all_possibilities = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1)]
    nums = [x for x in all_possibilities if x[0]+x[1]+x[2] != n]
    print(nums)
