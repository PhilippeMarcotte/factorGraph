import probabilitees

print("P(C) = {}".format(probabilitees.cambriolageTrue))

print("P(T) = {}".format(probabilitees.tremblementTrue))

alarmeTrue = probabilitees.cambriolageTrue * probabilitees.tremblementTrue * probabilitees.alarmeTrue[1][1] + probabilitees.cambriolageFalse * probabilitees.tremblementTrue * probabilitees.alarmeTrue[0][1] + probabilitees.cambriolageTrue * probabilitees.tremblementFalse * probabilitees.alarmeTrue[1][0] + probabilitees.cambriolageFalse * probabilitees.tremblementFalse * probabilitees.alarmeTrue[0][0]

print("P(A) = {}".format(alarmeTrue))

marieAppelleTrue = alarmeTrue * probabilitees.marieAppelleTrue[1] + (1 - alarmeTrue) * probabilitees.marieAppelleTrue[0]

print("P(M) = {}".format(marieAppelleTrue))

jeanAppelleTrue = alarmeTrue * probabilitees.jeanAppelleTrue[1] + (1 - alarmeTrue) * probabilitees.jeanAppelleTrue[0]

print("P(J) = {}".format(jeanAppelleTrue))