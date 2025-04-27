import CVRP_test_model
import CVRP_test_data
import CVRP_test_graph
import CVRP_test_solve

model = CVRP_test_model.createModel(CVRP_test_data.COORDS,CVRP_test_data.DEMANDS)
print(model)
CVRP_test_graph.plot(model)
res = CVRP_test_solve.solve(model)
print(res)
CVRP_test_graph.plotSolution(res,model)

print("FINISHED")
