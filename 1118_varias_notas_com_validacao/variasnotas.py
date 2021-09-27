opcao = 1
while(opcao == 1):
    opcao = -1
    x = []
    while len(x) < 2:
        val = float(input())
        if 0 <= val <= 10:
            x.append(val)
        else:
            print("nota invalida")
    print(f"media = {sum(x)/2:.2f}")
    while(opcao != 1 and opcao != 2):
        print("novo calculo (1-sim 2-nao)")
        opcao = int(input())
