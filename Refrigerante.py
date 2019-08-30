#Variaveis
Nota100 = 0
Nota50 = 10
Nota20 =10
Nota10 = 0
Nota5 = 10
Nota2 = 10
Moeda1 = 10
Moeda50 = 10
Moeda25 = 0
Moeda10 = 10
Moeda5 = 10
valorTroco = 0
refrigerante = 5.50
troco = 0
Saldo = 0

valorPago = float(input("Insira o Valor"))
if valorPago == 2 or valorPago == 5 or valorPago == 10 or valorPago == 50 or valorPago == 100 or valorPago == 1 or valorPago == 0.50 or valorPago == 0.25 or valorPago == 0.10 or valorPago == 0.05 :
    valorPago = valorPago - refrigerante
else:
    print("Nota Invalida")

#Este primeiro laço verifica se ainda falta fornecer valores para comprar o refrigerante
while valorPago < 0 : 
    print("Ainda faltam", abs(valorPago),"reais Complete o valor" )
    novoValor = float(input())
    #Verificar se a nota ou moeda é validar
    if novoValor == 2 or novoValor == 5 or novoValor == 10 or novoValor == 50 or novoValor == 100 or novoValor == 1 or novoValor == 0.50 or novoValor == 0.25 or novoValor == 0.10 or novoValor == 0.05 :
      valorPago = valorPago + novoValor
    #Se caso não for, informar
    else:
      print("Nota ou moeda invalida")
#O segundo laço calcula o troco para o cliente
if valorPago == 0 : # Pegue o refrigerante
 print("Obrigado e Boa tarde")

else:
 valorTroco = valorPago
 
while valorTroco > 0 : # VERIFICAR SE HA TROCO

 if valorTroco >= 50 and valorTroco < 100: #Verifica o intervalo do troco
     if (Nota50 * 50 >= valorTroco) or (Nota20 * 20 >= valorTroco): # Verifica se possui notas
         if Nota50 !=0: # Se tiver notas de 50
             valorTroco=valorTroco-50
         else:
              valorTroco = valorTroco -20
 elif valorTroco >=20 and valorTroco <50:  #Verifica o intervalo do troco
        if (Nota20 * 20 >= valorTroco) or (Nota10 * 10 >= valorTroco): # Verifica se possui notas
            if Nota20 !=0: # Se tiver notas de 20
                valorTroco = valorTroco-20
            else:
                valorTroco = valorTroco -10
 elif valorTroco >=10 and valorTroco < 20: #Verifica o intervalo do troco
     if (Nota10 * 10 >= valorTroco) or (Nota5 * 5 >= valorTroco): # Verifica se possui notas
            if Nota10 !=0: # Se tiver notas de 10
                valorTroco = valorTroco-10
            else:
                valorTroco = valorTroco -5
 elif valorTroco >=5 and valorTroco <10:#Verifica o intervalo do troco
        if (Nota5 * 5 >= valorTroco) or (Nota2 * 2 >= valorTroco): # Verifica se possui notas
            if Nota5 !=0: # Se tiver notas de 5
                valorTroco = valorTroco - 5
            else: # Senão notas de 2
                valorTroco = valorTroco - 2
 elif valorTroco >=1 and valorTroco <5:#Verifica o intervalo do troco
        if (Nota2 * 2 >= valorTroco) or (Moeda1 * 1 >= valorTroco): # Verifica se possui notas
            if Nota2 !=0 and valorTroco >=2: # Se tiver notas de 2
                valorTroco = valorTroco - 2
            else: # Senão moedas de 1
                valorTroco = valorTroco - 1
 elif  valorTroco <1:#Verifica o intervalo do troco
        if (Moeda50 * 0.50 >= valorTroco) or (Moeda25 * 0.25 >= valorTroco) or (Moeda10 * 0.10 >= valorTroco) or (Moeda5 * 0.05 >= valorTroco): # Verifica se possui notas
            if Moeda50 !=0 and valorTroco >=0.50: # Se tiver moedas de 50
                valorTroco = valorTroco - 0.50
            elif Moeda25 != 0 and (valorTroco >=0.25 and valorTroco <0.50): # Senão moedas de 25
                valorTroco = valorTroco - 0.25
            elif Moeda10 != 0 and ( valorTroco >=0.10 and valorTroco <0.25): # Senão moedas de 10
                valorTroco = valorTroco - 0.10
            else: # Senão moedas de 5
                valorTroco = valorTroco - 0.05
 else:
     print ("Não possui troco, pegue seu dinheiro de volta")
     valorPago = valorPago + refrigerante
     print ("valor Pago")
     valorPago = 0
     valorTroco = valorPago

while valorPago > 0 : # DAR TROCO E RETIRAR A NOTA DA MAQUINA

 if valorPago >= 50 and valorPago < 100: #Verifica o intervalo do troco
     if (Nota50 * 50 >= valorPago) or (Nota20 * 20 >= valorPago): # Verifica se possui notas
         if Nota50 !=0: # Se tiver notas de 50
             valorPago=valorPago-50 # retira 50 reais do valor total
             troco = troco + 50 # coloca 50 reais no troco da maquina
             Nota50 = Nota50 -1 # tira uma nota de 50 da maquina
         else:
             valorPago = valorPago-20 # retira 20 reais do valor total
             troco = troco + 20 # coloca 20 reais no troco da maquina
             Nota20 = Nota20 -1 # tira uma nota de 20 da maquina
 elif valorPago >=20 and valorPago <50:  #Verifica o intervalo do troco
        if (Nota20 * 20 >= valorPago) or (Nota10 * 10 >= valorPago): # Verifica se possui notas
            if Nota20 !=0: # Se tiver notas de 20
             valorPago=valorPago-20 # retira 20 reais do valor total
             troco = troco + 20 # coloca 20 reais no troco da maquina
             Nota20 = Nota20 -1 # tira uma nota de 20 da maquina
            else:
             valorPago=valorPago-10 # retira 10 reais do valor total
             troco = troco + 10 # coloca 10 reais no troco da maquina
             Nota10 = Nota10 -1 # tira uma nota de 10 da maquina
 elif valorPago >=10 and valorPago < 20: #Verifica o intervalo do troco
     if (Nota10 * 10 >= valorPago) or (Nota5 * 5 >= valorPago): # Verifica se possui notas
            if Nota10 !=0: # Se tiver notas de 10
             valorPago=valorPago-10 # retira 10 reais do valor total
             troco = troco + 10 # coloca 50 reais no troco da maquina
             Nota10 = Nota10 -1 # tira uma nota de 10 da maquina
            else:
             valorPago=valorPago-5 # retira 5 reais do valor total
             troco = troco + 5 # coloca 5 reais no troco da maquina
             Nota5 = Nota5 -1 # tira uma nota de 5 da maquina
 elif valorPago >=5 and valorPago <10:#Verifica o intervalo do troco
        if (Nota5 * 5 >= valorPago) or (Nota2 * 2 >= valorPago): # Verifica se possui notas
            if Nota5 !=0: # Se tiver notas de 5
             valorPago=valorPago-5 # retira 5 reais do valor total
             troco = troco + 5 # coloca 5 reais no troco da maquina
             Nota5 = Nota5 -1 # tira uma nota de 5 da maquina
            else: # Senão notas de 2
             valorPago=valorPago-2 # retira 2 reais do valor total
             troco = troco + 2 # coloca 2 reais no troco da maquina
             Nota2 = Nota2 -1 # tira uma nota de 2 da maquina
 elif valorPago >=1 and valorPago <5:#Verifica o intervalo do troco
        if (Nota2 * 2 >= valorPago) or (Moeda1 * 1 >= valorPago): # Verifica se possui notas
            if Nota2 !=0 and valorPago >=2: # Se tiver notas de 2
             valorPago=valorPago-2 # retira 2 reais do valor total
             troco = troco + 2 # coloca 2 reais no troco da maquina
             Nota2 = Nota2 -1 # tira uma nota de 2 da maquina
            else: # Senão moedas de 1
             valorPago=valorPago-1 # retira 1 reais do valor total
             troco = troco + 1 # coloca 1 reais no troco da maquina
             Moeda1 = Moeda1 -1 # tira uma moeda de 1 da maquina
 else : # intervalo < 1 
        if (Moeda50 * 0.50 >= valorPago) or (Moeda25 * 0.25 >= valorPago) or (Moeda10 * 0.10 >= valorPago) or (Moeda5 * 0.05 >= valorPago): # Verifica se possui notas
            if Moeda50 !=0 and valorPago >=0.50: # Se tiver moedas de 50
             valorPago=valorPago-0.50 # retira 0.50 centavos do valor total
             troco = troco + 0.50 # coloca 50 reais no troco da maquina
             Moeda50 = Moeda50 -1 # tira uma moeda de 50 da maquina
            elif Moeda25 != 0 and (valorPago >=0.25 and valorPago <0.50): # Senão moedas de 25
             valorPago=valorPago-0.25 # retira 25 centavos do valor total
             troco = troco + 0.25 # coloca 25 centavos no troco da maquina
             Moeda25 = Moeda25 -1 # tira uma moeda de 25 da maquina
            elif Moeda10 != 0 and ( valorPago >=0.10 and valorPago <0.25): # Senão moedas de 10
             valorPago=valorPago-0.10 # retira 10 centavos do valor total
             troco = troco + 0.10 # coloca 10 centavos no troco da maquina
             Moeda10 = Moeda10 -1 # tira uma moeda de 10 centavos da maquina
            else: # Senão moedas de 5
             valorPago=valorPago-0.05 # retira 0.05 do valor total
             troco = troco + 0.05 # coloca 5 centavos no troco da maquina
             Moeda5 = Moeda5 -1 # tira uma moeda de 5 centavos da maquina


def calcula ():
    print("Calculado")

calcula()

Saldo= Saldo + refrigerante
print ("Saldo atual é:", Saldo)
print("O troco atual é :", troco)
print(Nota20, Nota10, Nota5,Moeda25,Moeda5)
print(valorPago)

    