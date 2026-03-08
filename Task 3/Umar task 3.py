JUG1_CAPACITY = 4
JUG2_CAPACITY = 3

GOAL = 2

visited_states = set()
step_count = 0


def print_state(x, y):
    global step_count
    step_count += 1
    print("\nStep", step_count)
    print("Current State -> Jug1:", x, "Jug2:", y)


def is_goal(x, y):
    if x == GOAL or y == GOAL:
        return True
    return False


def dfs(x, y):

    if (x, y) in visited_states:
        return False

    visited_states.add((x, y))

    print_state(x, y)

    if is_goal(x, y):
        print("\nGoal Achieved Successfully!")
        return True

    print("Applying Rule: Fill Jug 1")
    if dfs(JUG1_CAPACITY, y):
        return True

    print("Applying Rule: Fill Jug 2")
    if dfs(x, JUG2_CAPACITY):
        return True

    print("Applying Rule: Empty Jug 1")
    if dfs(0, y):
        return True

    print("Applying Rule: Empty Jug 2")
    if dfs(x, 0):
        return True

  
    print("Applying Rule: Pour Jug 1 into Jug 2")
    transfer = min(x, JUG2_CAPACITY - y)
    new_x = x - transfer
    new_y = y + transfer
    if dfs(new_x, new_y):
        return True

    print("Applying Rule: Pour Jug 2 into Jug 1")
    transfer = min(y, JUG1_CAPACITY - x)
    new_x = x + transfer
    new_y = y - transfer
    if dfs(new_x, new_y):
        return True

    return False
print("Water Jug Problem using DFS")
print("--------------------------------")

start_x = 0
start_y = 0

dfs(start_x, start_y)