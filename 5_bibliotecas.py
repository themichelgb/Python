import random

chute=int(input("Entre com um número entre 1 e 10"))
num=random.randint(1,10)

if chute > num:
    print("Vc chutou alto, era:", num)
elif chute < num:
    print("Vc chutou baixo, era: ", num)
else:
    print("Na mosca")
