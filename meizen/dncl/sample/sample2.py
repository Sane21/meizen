from sample import Maisu

kakaku = 46
min_maisu = 100
for tsuri  in range( 0 ,  99 ,  1 ):
	shiharai = kakaku + tsuri
	maisu = Maisu(shiharai) + Maisu(tsuri)
	if maisu < min_maisu :
		maisu = maisu
print(maisu)
