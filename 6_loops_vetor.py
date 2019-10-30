print("Cadastre 5 pessoas. Cada pessoa terá um ID de 0 a 5")
um=input("1º Pessoa? ")
do=input("2º Pessoa? ")
tr=input("3º Pessoa? ")
qu=input("4º Pessoa? ")
ci=input("5º Pessoa? ")

lista=[um, do, tr, qu, ci]

qual=int(input("Qual ID Consultar? "))
novo="s"

while novo=="s":
    print("O Nome nesse ID é: ", lista[qual])
    novo=input("Quer consultar outro? s/n")
    if novo=="s":
        qual=int(input("Qual ID Consultar"))
    
print("Terminamos, visite meu site em www.kody.mobi")

