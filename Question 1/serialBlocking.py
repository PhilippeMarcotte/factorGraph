'''
x = P(X)
x_y = P(X,Y)
x_knowing_y = P(X | Y)
'''

cloudyTrue = 0.50

rain = [0.60, 0.45]

wetGrass = [0.90, 0.05]

cloudyTrue_rainTrue_wetGrassTrue = cloudyTrue * rain[0] * wetGrass[0]

rainTrue = cloudyTrue * rain[0] + (1.0 - cloudyTrue) * rain[1]

wetGrassTrue = rainTrue * wetGrass[0] + (1.0 - rainTrue) * rain[1]

cloudyTrue_rainTrue_wetGrassFalse = cloudyTrue * rain[0] * (1 - wetGrassTrue)

cloudyTrue_rainTrue = cloudyTrue_rainTrue_wetGrassTrue + cloudyTrue_rainTrue_wetGrassFalse

cloudyTrue_knowing_rainTrue = cloudyTrue_rainTrue / rainTrue

cloudyFalse_rainTrue_wetGrassTrue = (1- cloudyTrue) * rain[1] * wetGrass[0]

wetGrassTrue_rainTrue = cloudyTrue_rainTrue_wetGrassTrue + cloudyFalse_rainTrue_wetGrassTrue

wetGrassTrue_knowing_rainTrue = wetGrassTrue_rainTrue / rainTrue

print "Probabilite de nuages sachant qu'il pleut > Probability de nuages"
print "                           {0} > {1}".format(cloudyTrue_knowing_rainTrue, cloudyTrue)

print "On connaissait deja la probabilite que le gazon soit mouille sachant qu'il pleut"
print "{0} = {1}".format(wetGrassTrue_knowing_rainTrue, wetGrass[0])