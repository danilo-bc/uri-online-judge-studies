def solve(gray_levels):
    index = -1
    for i in range(len(gray_levels)):
        if gray_levels[i] <= 127:
            if index == -1:
                index = i
            else:
                print("*")
                return
    if index == -1:
        print("*")
    elif index == 0:
        print("A")
    elif index == 1:
        print("B")
    elif index == 2:
        print("C")
    elif index == 3:
        print("D")
    else:
        print("E")
    return

N = -1
while N != 0:
    N = int(input())
    for i in range(N):
        gray_levels = list(map(int, input().split()))
        solve(gray_levels)