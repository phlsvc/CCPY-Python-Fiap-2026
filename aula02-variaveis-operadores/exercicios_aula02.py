#exercicio 1
raio=5
area= 3.14159 * raio**2
print(area)

#exercicio 2
farenheit=int(input("Digite a temperatura em Farenheit: "))
celsius= (farenheit - 32) * 5/9
print(str(celsius) + " graus Celsius")

#exercicio 4
livro=25
caneta=5
total= 3 * livro + 2 * caneta
print(str(total) + " reais")

#exercicio 5
distancia=150
velocidade= 60
tempo= distancia / velocidade
print(str(tempo) + " horas")

#exercicio 6
a=input("Digite o valor da sua primeira nota: ")
b=input("Digite o valor da sua segunda nota: ")
media= (float(a) + float(b)) / 2
print(str(media) + " é a média das suas notas")

#exercicio 7
a=input("Digite o valor da sua primeira nota: ")
b=input("Digite o valor da sua segunda nota: ")
media= (float(a)*4 + float(b)*6) / 10
print(str(media) + " é a média das suas notas")

#exercicio 8
#nao sei se eu entendi direito o enunciado, mas acho que é isso
nome1=input("Digite o nome do primeiro produto: ")
quantidade1=int(input("Digite a quantidade do primeiro produto: "))
valor1= float(input("Digite o valor unitario do primeiro produto: "))
nome2=input("Digite o nome do segundo produto: ")
quantidade2=int(input("Digite a quantidade do segundo produto: "))
valor2= float(input("Digite o valor unitario do segundo produto: "))
total= quantidade1 * valor1 + quantidade2 * valor2  
print(str(total) + " é o valor total da compra")
#exercicio 9
produto= input("Digite o valor do produto: ")
pago= input("Digite o valor pago: ")
troco= float(pago) - float(produto)
print(str(troco) + " é o valor do troco")