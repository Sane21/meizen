Kouka = [1,5,10,50,100]
kingaku = 46
maisu = 0
nokori = kingaku
for i in range(0,5):
    i+=1
    maisu = maisu + 1
    nokori = nokori // Kouka[i]
print(maisu)