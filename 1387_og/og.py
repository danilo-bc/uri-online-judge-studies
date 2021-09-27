def solve(L, R):
    print(L+R)

L, R = [int(x) for x in input().split()]
while L != 0 and R != 0:
    solve(L, R)
    L, R = [int(x) for x in input().split()]