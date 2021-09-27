hi, mi, hf, mf = map(int, input().split())

dif_h = hf - hi
dif_m = mf - mi

if dif_m < 0:
    dif_h -= 1
    if dif_h < 0:
        dif_h += 24
    dif_m += 60

if dif_h == 0 and dif_m == 0:
    dif_h = 24

print(f"O JOGO DUROU {dif_h} HORA(S) E {dif_m} MINUTO(S)")