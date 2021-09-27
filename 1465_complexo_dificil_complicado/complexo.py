LIMIT = 2**30

def solve(r, i):
    initial_cplx = r + 1j*i
    cplx = 1*initial_cplx
    exp = 1
    while(cplx.imag != 0):
        cplx *= initial_cplx
        exp += 1
        if abs(cplx) >= LIMIT:
            print("TOO COMPLICATED")
            break
    print(exp)

M = int(input())
for k in range(M):
    r, i = map(int, input().split())
    solve(r, i)
