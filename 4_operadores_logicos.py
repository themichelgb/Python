chuva=input("Está chovendo (s/n)?")
vento=input("Está ventando (s/n)?")
sol=input("Está com sol (s/n)?")
frio=input("Está frio (s/n)?")

if chuva == "s" and vento == "s":
    print("Saia de Carro")
elif chuva == "s" and vento == "n":
    print("Saia de bike e guarda chuva")
if sol == "s" or frio == "n":
    print("Não precisa de edredom")
elif frio == "s":
    print("Saia com um edredom")
