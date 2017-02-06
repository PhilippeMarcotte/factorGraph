from graph import Graph
from node import FactorNode, VariableNode

def createExerciseGraph():
    C = VariableNode("C")
    T = VariableNode("T")
    A = VariableNode("A")
    M = VariableNode("M")
    J = VariableNode("J")

    fC = FactorNode("fC", [0.999, 0.001], C)
    fCTA = FactorNode("fACT", [[[0.999, 0.71],[0.06, 0.05]], 
                            [[0.001, 0.29],[0.94, 0.95]]], A, C, T)
    fT = FactorNode("fT", [0.998, 0.002], T)

    fMA = FactorNode("fMA", [[0.95, 0.1], 
                            [0.05, 0.9]], M, A)

    fJA = FactorNode("fJA", [[0.99, 0.3], 
                            [0.01, 0.7]], J, A)

    graph = Graph()

    graph.addVariableNode(C)

    graph.addFactorNode(fCTA)

    graph.addVariableNode(T)

    graph.addVariableNode(A)

    graph.addFactorNode(fMA)

    graph.addVariableNode(M)

    graph.addFactorNode(fJA)

    graph.addVariableNode(J)

    graph.addFactorNode(fC)

    graph.addFactorNode(fT)

    return graph

graph = createExerciseGraph()
graph.variableNodeIsObserved("M", 1)
graph.variableNodeIsObserved("J", 0)
marginalProbabilities = graph.marginalProbabilities()
print("P(Cambriolage = V| MarieAppelle = V,  JeanAppelle =  F) = {}".format(marginalProbabilities["C"][1]))

graph = createExerciseGraph()
graph.variableNodeIsObserved("M", 0)
graph.variableNodeIsObserved("J", 1)
marginalProbabilities = graph.marginalProbabilities()
print("P(Cambriolage = V| MarieAppelle = F,  JeanAppelle =  V) = {}".format(marginalProbabilities["C"][1]))

graph = createExerciseGraph()
graph.variableNodeIsObserved("M", 1)
graph.variableNodeIsObserved("J", 1)
marginalProbabilities = graph.marginalProbabilities()
print("P(Cambriolage = V| MarieAppelle = V,  JeanAppelle =  V) = {}".format(marginalProbabilities["C"][1]))

graph = createExerciseGraph()
graph.variableNodeIsObserved("M", 0)
graph.variableNodeIsObserved("J", 0)
marginalProbabilities = graph.marginalProbabilities()
print("P(Cambriolage = V| MarieAppelle = F,  JeanAppelle =  F) = {}".format(marginalProbabilities["C"][1]))

graph = createExerciseGraph()
graph.variableNodeIsObserved("M", 1)
marginalProbabilities = graph.marginalProbabilities()
print("P(Cambriolage = V| MarieAppelle = V) = {}".format(marginalProbabilities["C"][1]))

graph = createExerciseGraph()
graph.variableNodeIsObserved("J", 1)
marginalProbabilities = graph.marginalProbabilities()
print("P(Cambriolage = V| JeanAppelle = V) = {}".format(marginalProbabilities["C"][1]))

graph = createExerciseGraph()
marginalProbabilities = graph.marginalProbabilities()
for key, value in marginalProbabilities.items():
    print("P({0}) = {1}".format(key, value[1]))