from sumproduct import Variable, Factor, FactorGraph
import numpy as np



C = Variable('C', 2)
T = Variable('T', 2)
A = Variable('A', 2)
M = Variable('M', 2)
J = Variable('J', 2)

fC = Factor('fC', np.array([0.999, 0.001]))
fT = Factor('fT', np.array([0.998, 0.002]))
fACT = Factor('fACT', np.array([[[0.999, 0.001],[0.71, 0.29]],[[0.06, 0.94],[0.05, 0.95]]]))
fMA = Factor("fMA", np.array([[0.95, 0.05],[0.1, 0.9]]))
fJA = Factor("fJA", np.array([[0.99, 0.01],[0.3, 0.7]]))

g = FactorGraph(C, silent = False)
g.append('C', fACT)
g.append('fACT', T)
g.append('fACT', A)
g.append('A', fMA)
g.append('fMA', M)
g.append('A', fJA)
g.append('fJA', J)
g.append('C', fC)
g.append('T', fT)

g.compute_marginals()

print(g.nodes['J'].marginal())