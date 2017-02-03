'''
x = P(X)
x_y = P(X,Y)
x_knowing_y = P(X | Y)
'''

cloudyTrue = 0.50

rain = [0.60, 0.20]

sprinkler = [0.30, 0.70]

cloudyTrue_rainTrue_sprinklerTrue = cloudyTrue * rain[0] * sprinkler[0]

rainTrue = cloudyTrue * rain[0] + (1 - cloudyTrue) * rain[1]

cloudyTrue_rainTrue_sprinklerFalse = cloudyTrue * rain[0] * (1 - sprinkler[0])

cloudyTrue_rainTrue = cloudyTrue_rainTrue_sprinklerTrue + cloudyTrue_rainTrue_sprinklerFalse

rainTrue_knowing_cloudyTrue = cloudyTrue_rainTrue / cloudyTrue

cloudyTrue_rainFalse_sprinklerTrue = cloudyTrue * (1 - rain[0]) * sprinkler[0]

sprinklerTrue_cloudyTrue = cloudyTrue_rainTrue_sprinklerTrue + cloudyTrue_rainFalse_sprinklerTrue

rainTrue_knowing_cloudyTrue_sprinklerTrue = cloudyTrue_rainTrue_sprinklerTrue / sprinklerTrue_cloudyTrue

cloudyFalse_rainTrue_sprinklerTrue = (1 - cloudyTrue) * rain[1] * sprinkler[1]

rainTrue_sprinklerTrue = cloudyTrue_rainTrue_sprinklerTrue + cloudyFalse_rainTrue_sprinklerTrue

sprinklerTrue = cloudyTrue * sprinkler[0] + (1 - cloudyTrue) * sprinkler[1]

rainTrue_knowing_sprinklerTrue = rainTrue_sprinklerTrue / sprinklerTrue

print("DIVERGENT BLOCKING")
print("Probabilite qu'il pleut sachant que l'arrosoir est active")
print(rainTrue_knowing_sprinklerTrue)

print("Si on ne sait rien sur les nuages, savoir si l'arrosoir est active donne de l'information sur s'il pleut.\n")

print("Probabilite qu'il pleut sachant qu'il y a des nuages = Probabilite qu'il pleut sachant qu'il y a des nuages et que l'arrosoir est active")
print("                             	                 {0} = {1}".format(rainTrue_knowing_cloudyTrue, rainTrue_knowing_cloudyTrue_sprinklerTrue))

print("Si l'on sait deja qu'il y a des nuages, savoir que l'arrosoir est active ne dit rien de plus sur s'il pleut.\n")