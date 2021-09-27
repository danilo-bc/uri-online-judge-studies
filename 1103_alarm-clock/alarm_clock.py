def solve(h1, m1, h2, m2):
    if h2 < h1:
        h2 += 24
    elif h2 == h1:
        if m2 < m1:
            h2 += 24
    print(f"{(h2 - h1)*60 + (m2 - m1)}")


h1, m1, h2, m2 = [int(x) for x in input().split()]
while (h1, m1, h2, m2) != (0, 0, 0, 0):
    solve(h1, m1, h2, m2)
    h1, m1, h2, m2 = [int(x) for x in input().split()]