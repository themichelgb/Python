num1=int(input("Entre com o Número 1:"))
opera=input("indique o operador, ( + - * / )")
num2=int(input("Entre com o Número 2:"))
if opera == "+":
    soma=num1+num2
    print(num1, " + ", num2, " é igual a: ", soma)
elif opera == "-":
    sub=num1-num2
    print(num1, " - ", num2, " é igual a: ", sub)
elif opera == "*":
    mult=num1*num2
    print(num1, " x ", num2, " é igual a: ", mult)
elif opera == "/":
    div=num1/num2
    print(num1, " / ", num2, " é igual a: ", div)
