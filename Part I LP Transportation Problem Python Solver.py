from pulp import LpProblem, LpVariable, LpMinimize

# Warehouses and destinations
num_warehouses = 3
num_destinations = 7

# Define decision variables
X = LpVariable.dicts("X", [(i, j) for i in range(num_warehouses) for j in range(num_destinations)], lowBound=0)

# Objective function
objective = 0
costs = [
    [15, 160, 154, 245, 130, 125, 215],
    [160, 12, 315, 410, 290, 427, 375],
    [100, 260, 56, 190, 58, 204, 160]
]
for i in range(num_warehouses):
    for j in range(num_destinations):
        objective += costs[i][j] * X[(i, j)]

problem = LpProblem("Minimize_Transportation_Cost", LpMinimize)
problem.setObjective(objective)

# Supply constraints
capacity = [3980, 1785, 4856]
for i in range(num_warehouses):
    constraint_name = f"Warehouse_{i+1}_Capacity"
    constraint = sum(X[(i, j)] for j in range(num_destinations)) <= capacity[i]
    problem.addConstraint(constraint, name=constraint_name)

# Demand constraints 
demands = [1168, 1560, 1439, 986, 1658, 2035, 1159]
for j in range(num_destinations):
    constraint_name = f"Destination_{j+1}_Demand"
    constraint = sum(X[(i, j)] for i in range(num_warehouses)) >= demands[j]
    problem.addConstraint(constraint, name=constraint_name)

# Nonnegativity constraints
for i in range(num_warehouses):
    for j in range(num_destinations):
        problem.addConstraint(X[(i, j)] >= 0, name=f"NonNeg_{(i, j)}")

# Solve the problem
problem.solve()

# Print the solution (total cost)
print(f"Total Transportation Cost: {problem.objective.value():.2f}")

for i in range(num_warehouses):
  for j in range(num_destinations):
    value = X[(i, j)].value()
    print(f"Optimal X({i+1}, {j+1}): {value:.2f}")
