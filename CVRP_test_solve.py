
from pyvrp.stop import MaxRuntime
def solve(m):
    res = m.solve(stop=MaxRuntime(1), display=True)  # one second
    return res
