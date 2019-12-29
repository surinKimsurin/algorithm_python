# input
# 4 5 1
# 1 2
# 1 3
# 1 4
# 2 4
# 3 4

# input2
# 5 5 3
# 5 4
# 5 2
# 1 2
# 3 4
# 3 1

input1 = list(map(int, input().split(" ")))

matrix = [[0]*(input1[0]+1) for _ in range(input1[0]+1)]

for num in range(input1[1]):
    input2 = list(map(int, input().split(" ")))
    matrix[input2[0]][input2[1]] = 1
    matrix[input2[1]][input2[0]] = 1

print(matrix)

# [0, 0, 0, 0, 0],
# [0, 0, 1, 1, 1],
# [0, 1, 0, 0, 1],
# [0, 1, 0, 0, 1],
# [0, 1, 1, 1, 0]

def bfs(start):
    queue = [start]
    foot_prints = [start]

    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_prints:
                foot_prints += [search_node]
                queue += [search_node]

    return foot_prints


def bfs2(start):
    queue = [start]
    foot_print = [start]

    while queue:
        current_node = queue.pop(0)
        for search_node in range(len(matrix[current_node])):
            if matrix[current_node][search_node] and search_node not in foot_print:
                queue.extend([search_node])
                foot_print.extend([search_node])

    return foot_print


def dfs(current_node, row, foot_prints):
    foot_prints += [current_node]
    for search_node in range(len(row[current_node])):
        if row[current_node][search_node] and search_node not in foot_prints:
            foot_prints = dfs(search_node, row, foot_prints)

    return foot_prints

print(*dfs(input1[2], matrix, []))
