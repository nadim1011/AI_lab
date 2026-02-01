import heapq

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

MOVES = [(-1,0), (1,0), (0,-1), (0,1)]

def manhattan(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = GOAL.index(state[i])
            distance += abs(i//3 - goal_pos//3) + abs(i%3 - goal_pos%3)
    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    x, y = zero // 3, zero % 3

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_zero = nx * 3 + ny
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors

def best_first_search(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), start, []))
    visited = set()

    while pq:
        h, state, path = heapq.heappop(pq)

        if state == GOAL:
            return path + [state]

        if state in visited:
            continue
        visited.add(state)

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                heapq.heappush(
                    pq,
                    (manhattan(neighbor), neighbor, path + [state])
                )
    return None

def print_solution(solution):
    for step in solution:
        print(step[0:3])
        print(step[3:6])
        print(step[6:9])
        print("------")

start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

solution = best_first_search(start_state)
print_solution(solution)
