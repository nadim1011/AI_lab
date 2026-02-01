import heapq

GOAL_STATE = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]  

DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]

#manhattan_distance
def MHdis(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                ii = (value - 1) // 3
                jj = (value - 1) % 3
                dist += abs(i - ii) + abs(j - jj)
    return dist


def is_goal(state):
    return state == GOAL_STATE


def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)

    for dx, dy in DIRECTIONS:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(new_state)

    return neighbors


def find(start):
    heap = []
    heapq.heappush(heap, (MHdis(start), start, []))
    visited = set()

    while heap:
        h, state, path = heapq.heappop(heap)

        state_tuple = tuple(tuple(row) for row in state)
        if state_tuple in visited:
            continue
        visited.add(state_tuple)

        if is_goal(state):
            return path + [state]

        for neighbor in get_neighbors(state):
            neighbor_tuple = tuple(tuple(row) for row in neighbor)
            if neighbor_tuple not in visited:
                heapq.heappush(
                    heap,
                    (MHdis(neighbor), neighbor, path + [state])
                )

    return None



start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = find(start_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves.\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
