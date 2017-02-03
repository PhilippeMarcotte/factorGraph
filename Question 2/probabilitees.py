import numpy as np

cambriolageTrue = 0.001

cambriolageFalse = 1 - cambriolageTrue

cambriolage = np.array([cambriolageFalse, cambriolageTrue])

tremblementTrue = 0.002

tremblementFalse = 1 - tremblementTrue

tremblement = np.array([tremblementFalse, tremblementTrue])

alarmeTrue = np.array([[0.001, 0.29],
                   [0.94, 0.95]])

alarmeFalse = 1- alarmeTrue

marieAppelleTrue = np.array([0.05, 0.9])

marieAppelleFalse = 1- marieAppelleTrue

jeanAppelleTrue = np.array([0.01, 0.7])

jeanAppelleFalse = 1- jeanAppelleTrue

jointProbabilities = []

for c in range(0,2):
    for t in range(0,2):
        for a in range(0,2):
            for m in range(0,2):
                for j in range(0,2):
                    jointProbability = cambriolage[c] * tremblement[t]
                    if a:
                        jointProbability *= alarmeTrue[c][t]
                    else:
                        jointProbability *= alarmeFalse[c][t]
                    
                    if m:
                        jointProbability *= marieAppelleTrue[a]
                    else:
                        jointProbability *= marieAppelleFalse[a]
                    
                    if j:
                        jointProbability *= jeanAppelleTrue[a]
                    else:
                        jointProbability *= jeanAppelleFalse[a]
                    
                    jointProbabilities.append(jointProbability)

jointProbabilities = np.asarray(jointProbabilities)

def getJointProbability(cambriolage, tremblement, alarme, marieAppelle, jeanAppelle):
    binaryArray = [cambriolage, tremblement, alarme, marieAppelle, jeanAppelle]
    binaryValue = 0
    for value in binaryArray:
        binaryValue *= 10
        binaryValue += value
    
    return jointProbabilities[int(str(binaryValue), 2)]