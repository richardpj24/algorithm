import math

locations = {
    "Depot": (0, 0),
    "C1": (2, 3),
    "C2": (5, 4),
    "C3": (1, 6),
    "C4": (6, 1),
    "C5": (3, 7)
}

demand = {
    "C1": 2,
    "C2": 3,
    "C3": 2,
    "C4": 4,
    "C5": 2
}

num_vehicles = 2
vehicle_capacity = 6

def distance(p1, p2):
    return round(math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2), 2)

# Distance matrix
distance_matrix = {}
for i in locations:
    distance_matrix[i] = {}
    for j in locations:
        distance_matrix[i][j] = distance(locations[i], locations[j])

unvisited = list(demand.keys())
routes = []
total_cost = 0

# VRP using greedy nearest neighbor
for v in range(num_vehicles):
    capacity_left = vehicle_capacity
    route = ["Depot"]
    current = "Depot"

    while True:
        nearest = None
        min_dist = float('inf')

        for customer in unvisited:
            if demand[customer] <= capacity_left:
                d = distance_matrix[current][customer]
                if d < min_dist:
                    min_dist = d
                    nearest = customer

        if nearest is None:
            break

        route.append(nearest)
        capacity_left -= demand[nearest]
        total_cost += min_dist
        current = nearest
        unvisited.remove(nearest)

    # return to depot
    route.append("Depot")
    total_cost += distance_matrix[current]["Depot"]
    routes.append(route)

# Output formatting
output = ""
output += "VEHICLE ROUTING PROBLEM SOLUTION\n"
output += "---------------------------------\n\n"

output += "Delivery Locations (Coordinates)\n"
for loc in locations:
    output += f"{loc} : {locations[loc]}\n"

output += "\nVehicle Information\n"
output += f"Number of Vehicles : {num_vehicles}\n"
output += f"Vehicle Capacity : {vehicle_capacity}\n"

output += "\nDistance Matrix\n"
for i in distance_matrix:
    for j in distance_matrix[i]:
        output += f"{distance_matrix[i][j]:6}"
    output += "\n"

output += "\nVehicle Routes\n"
for i, route in enumerate(routes):
    output += f"Vehicle {i+1} : {' -> '.join(route)}\n"

output += f"\nTotal Travel Distance : {round(total_cost, 2)}\n"

output += "\nTime Complexity\n"
output += "Greedy Nearest Neighbor Approach ~ O(n^2)\n"

print(output)

# Save to file
with open("vehicle_routing_output.txt", "w") as f:
    f.write(output)

print("Output saved to vehicle_routing_output.txt")
