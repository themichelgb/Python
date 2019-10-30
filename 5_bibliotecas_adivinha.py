animal=input("Entre com um animal: cao, vaca, passaro, galo, cobra, tarta")
tipo=input("Ave, mamifero, reptil?")
late=input("Late? s/n")
voa=input("Voa? s/n")
casco=input("Tem Casco? s/n")

if tipo == "mamifero" and late == "s":
    print("cao")
elif tipo=="mamifero" and late =="n":
    print("vaca")
elif tipo=="ave" and voa =="s":
    print("passaro")
elif tipo=="ave" and voa =="n":
    print("galinha")
elif tipo=="reptil" and casco =="s":
    print("tarta")
elif tipo=="reptil" and casco =="n":
    print("cobra")
else:
    print("Opa, tem algo errado nas respostas")
