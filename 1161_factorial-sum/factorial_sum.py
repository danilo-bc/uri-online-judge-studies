from math import factorial
def solve(M, N):
    print(f"{factorial(M) + factorial(N)}")

while(True):
    try:
        M, N = [int(x) for x in input().split()]
        solve(M, N)
    except EOFError:
        break