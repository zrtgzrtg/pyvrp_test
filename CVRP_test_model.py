


from pyvrp import Model

def createModel(COORDS,DEMANDS):
    m = Model()
    m.add_vehicle_type(4, capacity=15)
    depot = m.add_depot(x=COORDS[0][0], y=COORDS[0][1])
    clients = [
        m.add_client(x=COORDS[idx][0], y=COORDS[idx][1], delivery=DEMANDS[idx])
        for idx in range(1, len(COORDS))
    ]
    
    locations = [depot] + clients
    for frm in locations:
        for to in locations:
            distance = abs(frm.x - to.x) + abs(frm.y - to.y)  # Manhattan
            m.add_edge(frm, to, distance=distance)
    return m

