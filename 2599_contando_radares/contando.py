def solve(N, radar_sizes):
    print(N, radar_sizes)

C = int(input())
for _ in range(C):
    N, M = map(int, input().split())
    radar_sizes = tuple(map(int, input().split()))
    solve(N, radar_sizes)