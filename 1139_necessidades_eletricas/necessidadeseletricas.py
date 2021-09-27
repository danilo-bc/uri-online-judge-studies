def calc_dist(xi, yi, xt, yt):
    # -1 compensates for python indexes in calculating distance
    return max(abs(xi - xt - 1), abs(yi - yt - 1))

def solve(N, M, P, plants):
    distances = [[0] * M for i in range(N)]
    for i in range(N):
        for j in range(M):
            if (i+1, j+1) in plants:
                continue
            dist_per_plant = [0 for p in plants]
            for n_p in range(len(plants)):
                dist_per_plant[n_p] = calc_dist(plants[n_p][0], plants[n_p][1], i, j)
            distances[i][j] = min(dist_per_plant)
    ind = 1
    dist = 1
    max_ind = (N * M) - P
    power_dict = {i: 0 for i in range(1, max_ind+1)}
    while ind < max_ind:
        for i in range(N):
            for j in range(M):
                if distances[i][j] == dist:
                    power_dict[ind] = (i + 1, j + 1)
                    ind += 1

    return power_dict


N, M, P = map(int, input().split())
while((N, M, P) != (0, 0, 0)):
    plants = []
    for n_power_plants in range(P):
        plants.append(tuple(map(int, input().split())))
    Q = int(input()) #ignored
    Q_list = list(map(int, input().split()))
    ref_dict = solve(N, M, P, plants)
    
    for q in Q_list:
        i, j = ref_dict[q]
        print(f"{i} {j}")
    print("-")
    N, M, P = map(int, input().split())