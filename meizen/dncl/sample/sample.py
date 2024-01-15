Kouka = [1,5,10,50,100]
kingaku = 46
maisu = 0
nokori = kingaku
for i  in range( 1 ,  5 , 1):
    maisu = maisu + nokori
    nokori = maisu % Kouka[i]
print(maisu)
