while(True):
    try:
        D, P, R, B = map(int, input().split())
        d_cost = list(map(int, input().split()))
        p_cost = list(map(int, input().split()))
        rivals = []
        for i in range(R):
            rivals.append(tuple(map(int, input().split())))
        print(D, P, R, B)
        print(d_cost)
        print(p_cost)
        print(rivals)

    except:
        break