def solve(N):
    n1 = 0
    n2 = 1
    for i in range(N):
        curr = n1 + n2
        if i == N-1:
            print(f"{n1}")
        else:
            print(f"{n1}", end=' ')
        n1 = n2
        n2 = curr
        

N = int(input())
solve(N)