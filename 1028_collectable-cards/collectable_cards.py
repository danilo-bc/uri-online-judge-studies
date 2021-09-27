import math

def solve(n1, n2):
    print(f"{math.gcd(n1, n2)}")
    
N = int(input())
for i in range(N):
    n1, n2 = [int(x) for x in input().split()]
    solve(n1, n2)