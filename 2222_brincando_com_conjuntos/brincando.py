T = int(input())
results = []
for t in range(T):
    N = int(input())
    M_list = []
    for n in range(N):
        M = tuple(map(int, input().split()))
        M_list.append(set(M[1:]))
    Q = int(input())
    op_list = []
    for q in range(Q):
        op_list.append(tuple(map(int, input().split())))
    for op_seq in op_list:
        if(op_seq[0] == 1):
            results.append(len(M_list[op_seq[1]-1].intersection(M_list[op_seq[2]-1])))
        elif(op_seq[0] == 2):
            results.append(len(M_list[op_seq[1]-1].union(M_list[op_seq[2]-1])))
    
for r in results:
    print(r)
