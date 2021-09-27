def solve(mat):
    ref = set(range(1,10))

    for i in range(9):
        if ref != set(mat[i]): #linhas 
            print("NAO")
            return
        if ref != set([mat[j][i] for j in range(9)]): #colunas
            print("NAO")
            return

    for i in range(0,8,3):
        for j in range(0,8,3):
            if ref != set([mat[k][n] for k in range(i, i+3) for n in range(j, j+3)]): # submatrizes 3x3
                print("NAO")
                return
        
    print("SIM")
    return

n = int(input())
for i in range(n):
    linha = ""
    mat = []
    for n_linhas in range(9):
        linha = list(map(int, input().split()))
        mat.append(linha)
    print("Instancia", i+1)
    solve(mat)
    print("")