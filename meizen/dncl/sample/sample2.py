from sample import 枚数

kakaku = 46
min_maisu = 100
for tsuri  in range( 0 ,  99 ,  1 ):
	shiharai = kakaku + tsuri
	maisu = 枚数(shiharai) + 枚数(tsuri)
	if maisu < min_maisu :
		maisu = maisu
print(maisu)
