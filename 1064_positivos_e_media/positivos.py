positivos = []
for i in range(6):
    val = float(input())
    if val > 0:
        positivos.append(val)
print(f"{len(positivos)} valores positivos")
print(f"{sum(positivos)/len(positivos):.1f}")