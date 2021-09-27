def solve(n, f, cost_hire_new, cost_fire, cost_weekly, cost_surplus):
    curr_workers = 0
    total_cost = 0
    for i in range(n):
        
        total_cost += curr_workers * cost_weekly
        diff_workers = f[i] - curr_workers
        if diff_workers > 0:
            total_cost += diff_workers * (cost_hire_new + cost_weekly)
            curr_workers += diff_workers
        elif diff_workers < 0:
            total_cost_to_fire = abs(diff_workers) * cost_fire
            total_cost_to_keep = abs(diff_workers) * cost_surplus
            if total_cost_to_fire < total_cost_to_keep:
                curr_workers += diff_workers
                total_cost += total_cost_to_fire
            else:
                total_cost += total_cost_to_keep
        print(curr_workers)

    print(total_cost)

inst_count = 0
n = int(input())
while n != 0:
    inst_count += 1
    f = list(map(int, input().split()))
    x, y, z, w = map(int, input().split())
    print(f"Instancia {inst_count}")
    solve(n, f, x, y, z, w)
    n = int(input())