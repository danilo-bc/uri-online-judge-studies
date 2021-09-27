while(True):
    try:
        L = int(input())
        lesmas = list(map(int, input().split()))
        max_speed_lesma = max(lesmas)
        res = 0
        if max_speed_lesma < 10:
            res = 1
        elif 10 <= max_speed_lesma < 20:
            res = 2
        else:
            res = 3
        print(res)
    except:
        break
