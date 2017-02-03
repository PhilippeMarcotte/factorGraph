'''
x = P(X)
x_y = P(X,Y)
x_knowing_y = P(X | Y)
'''

cloudyTrue = 0.50

rain = [0.60, 0.20]

wetGrass = [0.90, 0.05]

cloudyTrue_rainTrue_wetGrassTrue = cloudyTrue * rain[0] * wetGrass[0]

rainTrue = cloudyTrue * rain[0] + (1 - cloudyTrue) * rain[1]

wetGrassTrue = rainTrue * wetGrass[0] + (1 - rainTrue) * wetGrass[1]

cloudyTrue_rainTrue_wetGrassFalse = cloudyTrue * rain[0] * (1 - wetGrass[0])

cloudyTrue_rainTrue = cloudyTrue_rainTrue_wetGrassTrue + cloudyTrue_rainTrue_wetGrassFalse

cloudyTrue_knowing_rainTrue = cloudyTrue_rainTrue / rainTrue

cloudyFalse_rainTrue_wetGrassTrue = (1 - cloudyTrue) * rain[1] * wetGrass[0]

wetGrassTrue_rainTrue = cloudyTrue_rainTrue_wetGrassTrue + cloudyFalse_rainTrue_wetGrassTrue

cloudyTrue_knowing_rainTrue_wetGrassTrue = cloudyTrue_rainTrue_wetGrassTrue / wetGrassTrue_rainTrue

cloudyTrue_rainFalse_wetGrassTrue = cloudyTrue * (1 - rain[0]) * wetGrass[1]

cloudyTrue_wetGrassTrue = cloudyTrue_rainTrue_wetGrassTrue + cloudyTrue_rainFalse_wetGrassTrue

cloudyTrue_knowing_wetGrassTrue = cloudyTrue_wetGrassTrue / wetGrassTrue

print("SERIAL BLOCKING")
print("Probabilite de nuages sachant que le gazon est mouille")
print(cloudyTrue_knowing_wetGrassTrue)

print("Si on ne sait rien sur s'il pleut, savoir si le gazon est mouille donne de l'information sur s'il y a des nuages.\n")

print("Probabilite de nuages sachant qu'il pleut = Probabilite de nuages sachant qu'il pleut et que le gazon est mouille")
print("                       {0} = {1}".format(cloudyTrue_knowing_rainTrue, cloudyTrue_knowing_rainTrue_wetGrassTrue))

print("Si l'on sait deja qu'il pleut, savoir que le gazon est mouille ne dit rien de plus sur s'il y a des nuages.\n")