def solve(x1, y1, x2, y2, meteo_coords):
    m_count = 0
    for m in meteo_coords:
        mx = m[0]
        my = m[1]
        if (x1 <= mx <= x2) and (y2 <= my <= y1):
            m_count += 1
    return m_count
        
x1, y1, x2, y2 = map(int, input().split())
results = []
while x1 != 0 and y1 != 0 and x2 != 0 and y2 != 0:
    n_meteoritos = int(input())
    meteo_coords = [(0, 0)] * n_meteoritos
    for m in range(n_meteoritos):
        meteo_coords[m] = tuple(map(int, input().split()))
    results.append(solve(x1, y1, x2, y2, meteo_coords))
    x1, y1, x2, y2 = map(int, input().split())

for i in range(len(results)):
    print(f"Teste {i+1}")
    print(results[i])