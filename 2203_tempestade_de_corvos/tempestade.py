from math import sqrt

while(True):
    try:
        xf, yf, xi, yi, vi, r1, r2 = map(int, input().split())

        dist_i = sqrt((xf - xi)**2 + (yf - yi)**2)
        dist_f = dist_i + vi * 1.5

        if dist_f <= r1 + r2:
            print("Y")
        else:
            print("N")
    except:
        break