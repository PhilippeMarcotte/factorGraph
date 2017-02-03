import numpy as np

import reseau

def getCambriolageAndMarieAppelleAndJeanAppelle(cambriolage, marieAppelle, jeanAppelle):
    cambriolage_alarmeTrue_marieAppelle_jeanAppelle = reseau.getJointProbability( cambriolage= cambriolage, tremblement= True, alarme= True, marieAppelle= marieAppelle, jeanAppelle= jeanAppelle) + reseau.getJointProbability( cambriolage= cambriolage, tremblement= False, alarme= True, marieAppelle= marieAppelle, jeanAppelle= jeanAppelle )

    cambriolage_alarmeFalse_marieAppelle_jeanAppelle = reseau.getJointProbability( cambriolage= cambriolage, tremblement= True, alarme= False, marieAppelle= marieAppelle, jeanAppelle= jeanAppelle ) + reseau.getJointProbability( cambriolage= cambriolage, tremblement= False, alarme= False, marieAppelle= marieAppelle, jeanAppelle= jeanAppelle )

    return cambriolage_alarmeTrue_marieAppelle_jeanAppelle + cambriolage_alarmeFalse_marieAppelle_jeanAppelle

def getMarieAppelleAndJeanAppelle(marieAppelle, jeanAppelle):
    cambriolageTrue_marieAppelle_jeanAppelle = getCambriolageAndMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = marieAppelle, jeanAppelle = jeanAppelle)

    cambriolageFalse_marieAppelle_jeanAppelle = getCambriolageAndMarieAppelleAndJeanAppelle(cambriolage = False, marieAppelle = marieAppelle, jeanAppelle = jeanAppelle)

    return cambriolageTrue_marieAppelle_jeanAppelle + cambriolageFalse_marieAppelle_jeanAppelle

def getCambriolageKnowingMarieAppelleAndJeanAppelle(cambriolage, marieAppelle, jeanAppelle):
    marieAppelle_jeanAppelle = getMarieAppelleAndJeanAppelle(marieAppelle = marieAppelle, jeanAppelle = jeanAppelle)

    cambriolageTrue_knowing_marieAppelle_jeanAppelle = getCambriolageAndMarieAppelleAndJeanAppelle(cambriolage = cambriolage, marieAppelle = marieAppelle, jeanAppelle = jeanAppelle) / marieAppelle_jeanAppelle

    return cambriolageTrue_knowing_marieAppelle_jeanAppelle
    
print("P(Cambriolage = V| MarieAppelle = V,  JeanAppelle =  F) = {}".format(getCambriolageKnowingMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = True, jeanAppelle = False)))

print("P(Cambriolage = V| MarieAppelle = F,  JeanAppelle =  V) = {}".format(getCambriolageKnowingMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = False, jeanAppelle = True)))

print("P(Cambriolage = V| MarieAppelle = V,  JeanAppelle =  V) = {}".format(getCambriolageKnowingMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = True, jeanAppelle = True)))

print("P(Cambriolage = V| MarieAppelle = F,  JeanAppelle =  F) = {}".format(getCambriolageKnowingMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = False, jeanAppelle = False)))

marieAppelleTrue = getMarieAppelleAndJeanAppelle(marieAppelle = True, jeanAppelle = True) + getMarieAppelleAndJeanAppelle(marieAppelle = True, jeanAppelle = False)

cambriolageTrue_marieAppelleTrue = getCambriolageAndMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = True, jeanAppelle = True) + getCambriolageAndMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = True, jeanAppelle = False)

cambriolageTrue_knowing_marieAppelleTrue = cambriolageTrue_marieAppelleTrue / marieAppelleTrue

print("P(Cambriolage = V| MarieAppelle = V) = {}".format(cambriolageTrue_knowing_marieAppelleTrue))

jeanAppelleTrue = getMarieAppelleAndJeanAppelle(marieAppelle = True, jeanAppelle = True) + getMarieAppelleAndJeanAppelle(marieAppelle = False, jeanAppelle = True)

cambriolageTrue_jeanAppelleTrue = getCambriolageAndMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = True, jeanAppelle = True) + getCambriolageAndMarieAppelleAndJeanAppelle(cambriolage = True, marieAppelle = False, jeanAppelle = True)

cambriolageTrue_knowing_jeanAppelleTrue = cambriolageTrue_jeanAppelleTrue / jeanAppelleTrue

print("P(Cambriolage = V| JeanAppelle = V) = {}".format(cambriolageTrue_knowing_jeanAppelleTrue))