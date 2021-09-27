# Fortemente inspirado por:
# https://stackoverflow.com/a/10609036/4913389
# e usando essa ideia para pegar valores da tupla
# https://stackoverflow.com/a/638069/4913389

from itertools import combinations
def solve(order_list, max_pizzas):
    # Como P <= 30, a gente talvez pode ver todas as combinações
    # e avaliar se a quantidade de pizzas da combinação
    # é menor que o limite estipulado
    longest_time = -1
    for i in range(len(order_list), 0, -1):
        comb_group = ([comb 
                            for comb in combinations(order_list, i) 
                                if sum(i for i, j in comb) > longest_time
                                and sum(j for i, j in comb) <= max_pizzas
                    ])
        all_times_for_this_group = []
        for ans_tuple in comb_group:
            all_times_for_this_group.append(sum(comb[0] for comb in ans_tuple))
        if len(all_times_for_this_group) > 0:
            longest_time = max(all_times_for_this_group)
    # Retorna-se o maior tempo encontrado
    print(f"{longest_time} min.")

N = int(input())
while N != 0:
    P = int(input())
    order_list = []
    for i in range(N):
        minutes, pizzas = [int(x) for x in input().split()]
        order_list.append((minutes, pizzas))
    solve(order_list, P)
    
    N = int(input())