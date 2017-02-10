import numpy as np
from abc import abstractclassmethod, ABC

class Node(ABC):
    def __init__(self, id):
        self.id = id
        self.connectedNodes = []
        self.incoming = []
        self.incomingMessagesStatus = []
        self.outgoingMessagesStatus = []
        

    def receiveMessage(self, node, message):
        index = self.connectedNodes.index(node)
        self.incoming[index] = message
        self.incomingMessagesStatus[index] = True
    
    def normalize(self, index):
        self.outgoing[index] = self.outgoing[index] / np.sum(self.outgoing[index])
    
    def saveOutgoing(self):
        self.oldOutgoing = self.outgoing[:]
    
    def checkIfMessagesTransmittedToAll(self):
        return all(self.outgoingMessagesStatus)

    @abstractclassmethod
    def calculate(self, reception):
        pass

    def calculateAndSendMessage(self):
        for i in range(0, len(self.incoming)):
            tmp = self.incomingMessagesStatus[:]
            del tmp[i]

            if all(tmp):
                message = self.calculate(i)
                self.connectedNodes[i].receiveMessage(self, message)
                self.outgoingMessagesStatus[i] = True

class VariableNode(Node):
    def __init__(self, id):
        super(VariableNode, self).__init__(id)
        self.isObserved = False

    def observed(self, value):
        self.isObserved = True
        self.observedValue = np.zeros(2)
        self.observedValue[value] = 1

    def calculate(self, reception):
        if not self.isObserved :
            if len(self.connectedNodes) > 1:
                result = 1
                for i in range(0, len(self.incoming)):
                    if i == reception:
                        continue
                    result = np.multiply(result, self.incoming[i])
                return result
            else:
                return np.ones(2) / 2
        else:
            return self.observedValue[:]

class FactorNode(Node):
    def __init__(self, id, array, *args):
        super(FactorNode, self).__init__(id)
        self.array = np.array(array)
        self.connectedNodes = list(args)

        for varNode in self.connectedNodes:
            if len(self.connectedNodes) != 1:
                self.incoming.append(np.ones(2))
                self.incomingMessagesStatus.append(False)              
            else:
                self.incoming.append(self.array)
                self.incomingMessagesStatus.append(True)
            
            self.outgoingMessagesStatus.append(False)
            
            varNode.connectedNodes.append(self)
            varNode.incoming.append(np.ones(2))
            varNode.incomingMessagesStatus.append(False)
            varNode.outgoingMessagesStatus.append(False)

    def calculate(self, reception):
        if len(self.connectedNodes) > 1:
            productMessagesMatrices = 1
            for i in range(0, len(self.incoming)):
                messagesMatrix = np.ones(self.array.shape)
                if i == reception:
                    continue      

                for index in np.ndindex(self.array.shape):
                    messagesMatrix[index] *= self.incoming[i][index[i]]
                
                productMessagesMatrices = np.multiply(productMessagesMatrices, messagesMatrix)        

            productMessagesMatrices = np.multiply(self.array, productMessagesMatrices)
            sumMessagesMatrices = np.zeros(2)
            for index in np.ndindex(self.array.shape):
                sumMessagesMatrices[index[reception]] += productMessagesMatrices[index]
            sumMessagesMatrices = sumMessagesMatrices / sum(sumMessagesMatrices)
            return sumMessagesMatrices
        else:
             return self.array[:]