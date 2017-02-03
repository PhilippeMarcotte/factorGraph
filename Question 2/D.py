import reseau

print("P(C) = {}".format(reseau.cambriolageTrue))

print("P(T) = {}".format(reseau.tremblementTrue))

alarmeTrue = reseau.cambriolageTrue * reseau.tremblementTrue * reseau.alarmeTrue[1][1] + reseau.cambriolageFalse * reseau.tremblementTrue * reseau.alarmeTrue[0][1] + reseau.cambriolageTrue * reseau.tremblementFalse * reseau.alarmeTrue[1][0] + reseau.cambriolageFalse * reseau.tremblementFalse * reseau.alarmeTrue[0][0]

print("P(A) = {}".format(alarmeTrue))

marieAppelleTrue = alarmeTrue * reseau.marieAppelleTrue[1] + (1 - alarmeTrue) * reseau.marieAppelleTrue[0]

print("P(M) = {}".format(marieAppelleTrue))

jeanAppelleTrue = alarmeTrue * reseau.jeanAppelleTrue[1] + (1 - alarmeTrue) * reseau.jeanAppelleTrue[0]

print("P(J) = {}".format(jeanAppelleTrue))