import itertools
# INPUT DATA
robots = ["R1", "R2", "R3"]
tasks = ["T1", "T2", "T3"]
# Cost matrix (rows = robots, columns = tasks)
cost_matrix = [
 [9, 2, 7],
 [6, 4, 3],
 [5, 8, 1]
]
# DISPLAY INPUT
print("Robots:", robots)
print("Tasks:", tasks)
print("\nCost Matrix:")
for row in cost_matrix:
 print(row)
# BRUTE FORCE (for understanding)
min_cost = float('inf')
best_assignment = None
all_permutations = list(itertools.permutations(range(len(tasks))))
print("\nPossible Allocations and Costs:")
for perm in all_permutations:
 total_cost = 0
 allocation = []

 for i in range(len(robots)):
 total_cost += cost_matrix[i][perm[i]]
 allocation.append((robots[i], tasks[perm[i]]))

 print(allocation, "-> Cost:", total_cost)

 if total_cost < min_cost:
 min_cost = total_cost
 best_assignment = allocation
# FINAL OUTPUT
print("\nOptimal Task Allocation:")
for r, t in best_assignment:
 print(f"{r} -> {t}")
print("Minimum Total Cost:", min_cost)
# TIME COMPLEXITY
print("\nTime Complexity:")
print("Brute Force: O(n!)")
print("Hungarian Algorithm: O(n^3)")
with open("robot_task_allocation_output.txt", "w") as f:
 f.write("Robot Task Allocation Output\n\n")

 f.write("Robots:\n")
 f.write(str(robots) + "\n\n")

 f.write("Tasks:\n")
 f.write(str(tasks) + "\n\n")

 f.write("Cost Matrix:\n")
 for row in cost_matrix:
 f.write(str(row) + "\n")

 f.write("\nOptimal Allocation:\n")
 for r, t in best_assignment:
 f.write(f"{r} -> {t}\n")

 f.write(f"\nMinimum Total Cost: {min_cost}\n")

 f.write("\nTime Complexity:\n")
 f.write("Brute Force: O(n!)\n")
 f.write("Hungarian Algorithm: O(n^3)\n")
print("\nOutput saved to robot_task_allocation_output.txt")