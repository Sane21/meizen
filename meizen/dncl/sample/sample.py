Kouka = [1,5,10,50,100]
kingaku = 46
maisu = 0
nokori = kingaku
for i  in range( 4 ,  0 , -1):
	maisu = maisu + nokori // Kouka[i]
	nokori = nokori % Kouka[i]
print(maisu)

def 枚数(kingaku):
	Kouka = [1,5,10,50,100]
	maisu = 0
	nokori = kingaku
	for i  in range( 4 ,  0 , -1):
		maisu = maisu + nokori // Kouka[i]
		nokori = nokori % Kouka[i]
	return maisu
