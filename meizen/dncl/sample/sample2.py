from .sample import Maisu

kakaku = 46
min_maisu = 100
for tsuri  in range( 1 ,  99 ,  1 ):
    shiharai = kakaku + tsuri
    maisu = kakaku + kakaku
    if maisu < min_maisu :
        maisu = maisu
print(min_maisu)
