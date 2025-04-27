import matplotlib.pyplot as plt

from pyvrp.plotting import plot_coordinates


def plot(m):
    _, ax = plt.subplots(figsize=(8, 8))
    plot_coordinates(m.data(), ax=ax)
    filename = "CVRP_test_plot.png"
    plt.savefig(f"{filename}", dpi=300, bbox_inches="tight")
    print(f"Plot saved as {filename}")

from pyvrp.plotting import plot_solution

def plotSolution(res,m):
    _, ax = plt.subplots(figsize=(8, 8))
    plot_solution(res.best, m.data(), ax=ax)
    filename = "CVRP_test_solution.png"
    plt.savefig(f"{filename}", dpi = 300,bbox_inches="tight")
    print(f"Plot saves as {filename}")

