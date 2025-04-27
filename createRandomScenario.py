import random
import math
from pyvrp import ProblemData

def generate_random_cvrp_instance(
    num_clients=20,
    grid_size=100,
    demand_range=(1, 10),
    vehicle_capacity=100,
    seed=None
):
    if seed is not None:
        random.seed(seed)

    # Depot coordinates
    depot = (grid_size // 2, grid_size // 2)
    coords = [depot]
    demands = [0]  # Depot has no demand
    service_times = [0]  # Assuming zero service time for simplicity

    # Generate random client data
    for _ in range(num_clients):
        x = random.randint(0, grid_size)
        y = random.randint(0, grid_size)
        coords.append((x, y))
        demands.append(random.randint(*demand_range))
        service_times.append(0)

    # Compute Euclidean distance matrix
    distance_matrix = [
        [
            int(math.hypot(x1 - x2, y1 - y2))
            for (x2, y2) in coords
        ]
        for (x1, y1) in coords
    ]

    # Create ProblemData instance
    data = ProblemData(
        coordinates=coords,
        distance_matrix=distance_matrix,
        demands=demands,
        service_times=service_times,
        vehicle_cap=vehicle_capacity,
    )

    return data

# Example usage
if __name__ == "__main__":
    data = generate_random_cvrp_instance()
    # print(data)
    # Now you can use 'data' with PyVRP's solver

