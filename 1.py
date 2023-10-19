# f(x) = g(x) + h(x)
# h(x) = 位置错误的方块数量
# g(x) = 步数

goal = '135702684'

def exchange(string, i,j):
    try:
        temp = string[j]
        trailer = string[j+1:] if j + 1 < len(string) else ''
        string = string[0:j] + string[i] + trailer
        string = string[0:i] + temp + string[i+1:]
    except:
        return None
    return string
def get_fx(string, goal):
    gx = 1 # 代价一定是一步
    # 计算hx:位置错误的方块数量
    hx = 0
    for i in range(len(string)):
        if string[i] != goal[i]:
            hx += 1
    return hx+gx
def next_node(input):
    # 0 的位置
    pos0 = input.index('0')
    # 所有下一个可能的状态
    pos_dict = {0:[1,3], 
                1:[-1,1,3],
                2:[-1,3],
                3:[-3, 1,3],
                4:[-1,1,3,-3],
                5:[-3,3,-1],
                6:[-3,1],
                7:[-1,1,-3],
                8:[-3,-1]}
    all_possible_states = [exchange(input, pos0, pos0+x) for x in pos_dict[pos0]]
    # 找到fx最小的状态
    min_fx = 1e4
    selected_state = None
    for state in all_possible_states:
        if state != None:
            fx = get_fx(state, goal)
            if min_fx > fx:
                min_fx = fx
                selected_state = state
    return   selected_state, min_fx# 返回下一个状态和fx


with open('1_test.txt', 'r') as f:
    tests = f.readlines()
for test in tests:
    input = test.strip()
    cost = 0
    next_state = input
    # print(f'========= test:{input} ===========')
    while next_state != goal:
        cost += 1
        next_state, min_fx= next_node(next_state)
        # print('step:{}, state:{}, f(x): {}'.format(cost, next_state, min_fx))
        if cost > 200:
            print('not found')
            break
    # print('start:{}, end:{}, min_steps:{}\n'.format(input, next_state, cost))
    print(cost)