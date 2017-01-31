'''
x = P(X)
x_y = P(X,Y)
x_knowing_y = P(X | Y)
'''

sprinkler = 0.3

rain = 0.45

wetGrass = [[0.98, 0.80],
           [0.90, 0.05]]

rainTrue_wetGrassTrue_sprinklerTrue = sprinkler * rain * wetGrass[0][0]

rainTrue_wetGrassTrue_sprinklerFalse = sprinkler * rain * wetGrass[0][1]

rainFalse_wetGrassTrue_sprinklerTrue = sprinkler * rain * wetGrass[1][0]

rainFalse_wetGrassTrue_sprinklerFalse = sprinkler * rain * wetGrass[1][1]

rainTrue_wetGrassTrue = rainTrue_wetGrassTrue_sprinklerTrue + rainTrue_wetGrassTrue_sprinklerFalse

wetGrassTrue = rainTrue_wetGrassTrue_sprinklerTrue + rainTrue_wetGrassTrue_sprinklerFalse + rainFalse_wetGrassTrue_sprinklerTrue + rainFalse_wetGrassTrue_sprinklerFalse

rainTrue_knowing_wetGrassTrue = rainTrue_wetGrassTrue / wetGrassTrue

wetGrassTrue_sprinklerTrue = rainTrue_wetGrassTrue_sprinklerTrue + rainFalse_wetGrassTrue_sprinklerTrue

rainTrue_knowing_wetGrassTrue_sprinklerTrue = rainFalse_wetGrassTrue_sprinklerTrue / wetGrassTrue_sprinklerTrue

print "Probabilite de pluie sachant que le gazon est mouille > Probabilite de pluie sachant que le gazon est mouille et que le sprinkler a ete active"
print "                                       {0} > {1}".format(rainTrue_knowing_wetGrassTrue, rainTrue_knowing_wetGrassTrue_sprinklerTrue)