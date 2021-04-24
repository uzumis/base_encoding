#Implementação do HDB3
import matplotlib.pyplot as plt
string = input("Insira uma sequencia de bits: ")
string = str(string)
codificado = []
codificadoImpresso = []
def HBD3():
    contador = 0
    p_anterior = 0
    violacao = 0
    p_violacao = 0
#A codificação HBD3 consiste em transmissões positivas e negativas. Sendo um desenvolvimento da Alternate Mark Inversion
    for bit in string:
        if bit == str(1):
            bit = int(1)
            if p_anterior == 1:
                codificado.append(int(-1))
                codificadoImpresso.append(int(-1))
                p_anterior = int(-1)
                p_violacao = int(-1)
                violacao = violacao +1
            elif p_anterior == -1:
                codificado.append(int(1))
                codificadoImpresso.append(int(1))
                p_anterior = int(1)
            elif p_anterior == 0:
                codificado.append(bit)
                codificadoImpresso.append(bit)
                p_anterior = int(bit)
        elif bit == str(0):
            bit = int(0)
            contador = contador +1
            if contador == 4:
                codificado.pop()
                codificado.pop()
                codificado.pop()
                codificadoImpresso.pop()
                codificadoImpresso.pop()
                codificadoImpresso.pop()
                if violacao % 2 == 0:
                    #B00V
                    p_violacao = p_anterior * -1
                    codificado.extend([int(p_violacao), int(0),int(0), int(p_violacao)])
                    codificadoImpresso.extend(['B', 0, 0, 'V'])
                    violacao = violacao + 1
                    p_anterior = p_violacao
                else:
                    #000V
                    codificado.extend([int(0), int(0), int(0), int(p_violacao)])
                    codificadoImpresso.extend([0, 0, 0, 'V'])
                    violacao = violacao + 1
                contador = 0
            else:
                codificado.append(int(bit))
                codificadoImpresso.append(int(bit))
HBD3 ()
#Exibe o Gráfico
plt.axhline(y=0, color='r', linestyle='-')
plt.plot(codificado, marker="None", color="black",drawstyle="steps-pre")
plt.title("HDB3")
plt.ylabel("SInal")
plt.yticks([-1,0, 1])
plt.xlabel(codificadoImpresso)
plt.show()