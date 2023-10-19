# fx = gx + hx
# gx = 输入中的D_i
# hx = 最小出路
# 堆节点结构：(节点，cost, fx)
import numpy as np
COST_IDX = 1
FX_IDX = 2
START_IDX = 0
END_IDX = 1

def parse(input):
    first_line = input.split("\n")[0].split(" ")
    N = int(first_line[0])
    M = int(first_line[1])
    K = int(first_line[2])
    paths = []
    for m in range(M):
        line_m = input.split("\n")[m+1].split(" ")
        start = int(line_m[0])
        end = int(line_m[1])
        cost = int(line_m[2])
        if start < end:
            paths.append([start, end, cost])
    return N, M, K, np.array(paths)  # 转为numpy方便筛选



def get_h(state):
    h = min(paths[paths[:, 0]==state][:, 2], default=0) # 最小出路
    return h



def find_k_paths(K):
    corr_state= 1
    goal = N
    costs = []
    fx = get_h(corr_state)  # 初始节点，gx=0
    heap = [(corr_state, 0, fx)]  # 模拟最小堆 (节点，cost, fx)
    while len(costs) < K and heap:  # goal 节点每出队一次， 说明找到一条路，最小堆保证了路是最短的
        pop_item = min(heap, key=lambda x: x[FX_IDX])  # 模拟最小堆pop
        heap.remove(pop_item) 
        if pop_item[0] == goal:  # 如果是goal出队，说明已经找到
            costs.append(int(pop_item[COST_IDX]))
        else:
            corr_state = pop_item[0]    # 取出节点号
            possible_next_states = paths[paths[:, START_IDX]==corr_state][:, END_IDX]  # 从当前节点出发，可能的下一个节点
            for possible_next_state in possible_next_states:  # 计算所有可能的下一个节点的gx, hx, fx, 并入堆  
                corr_cost = pop_item[COST_IDX]
                gx = paths[(paths[:,START_IDX]==corr_state)&(paths[:, END_IDX]==possible_next_state)][:,2] + corr_cost
                hx = get_h(possible_next_state)
                heap.append((possible_next_state, gx, hx+gx))
    if len(costs) < K:  # 不足K条路则补齐
        costs.extend([-1] * (K - len(costs)))
    return costs

inputs = open('2_test.txt', 'r').read().split('\n\n')
for input in inputs:
    N, M, K, paths = parse(input)
    cost = 0
    K_paths = find_k_paths(K)

    for Kth_path in K_paths:
        print(Kth_path, end=' ')
    print()
    
