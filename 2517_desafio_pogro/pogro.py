from math import sqrt

def solve(a, b, c, xc, yc, xf):
    x_vals = range(0, 100*xf)
    distances = []
    for x in x_vals:
        xi = x/100
        f_x = -xi**2/a -xi/b + c

        dist = sqrt((xi - xc)**2 + (f_x - yc)**2)
        distances.append(dist)
    print(f"{min(distances):.2f}")


while(True):
    a, b, c = (0, 0, 0)
    xc, yc = (0, 0)
    xf = 0
    try:
        a, b, c = map(int, input().split())
        xc, yc = map(int, input().split())
        xf = int(input())
    except:
        break
    solve(a, b, c, xc, yc, xf)