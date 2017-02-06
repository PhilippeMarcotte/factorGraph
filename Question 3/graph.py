from node import FactorNode, VariableNode
import numpy as np

class Graph():
    def __init__(self):
        self.variableNodes = []
        self.factorNodes = []
    
    def addVariableNode(self, id):
        varNode = VariableNode(id)
        self.variableNodes.append(varNode)
    
    def addFactorNode(self, id, array, *args):
        factorNode = FactorNode(id, array, *args)
        self.factorNodes.append(factorNode)

    def addVariableNode(self, varNode):
        self.variableNodes.append(varNode)
    
    def addFactorNode(self, factorNode):
        self.factorNodes.append(factorNode)
    
    def sumProduct(self):
        for i in range(0,500):
            for factorNode in self.factorNodes:
                # start with factor-to-variable
                # can send immediately since not sending to any other factors
                factorNode.calculateAndSendMessage()

            for varNode in self.variableNodes:
                # variable-to-factor
                varNode.calculateAndSendMessage()

            # check for convergence
            isConverging = True
            for varNode in self.variableNodes:
                isConverging = varNode.checkIfMessagesTransmittedToAll()
                if not isConverging:
                    break

            for factorNode in self.factorNodes:
                isConverging = factorNode.checkIfMessagesTransmittedToAll()
                if not isConverging:
                    break

            if isConverging: # we have convergence!
                break

    def variableNodeIsObserved(self, id, value):
        for varNode in self.variableNodes:
            if varNode.id == id:
                varNode.observed(value)
                break
    
    def marginalProbabilities(self):
        self.sumProduct()

        marginalProbabilities = {}
        for varNode in self.variableNodes:
            marginalProbability = 1
            for message in varNode.incoming:
                marginalProbability *= message
            
            # normalize
            n = np.sum(marginalProbability)
            marginalProbability = marginalProbability / n

            marginalProbabilities[varNode.id] = marginalProbability
        
        return marginalProbabilities