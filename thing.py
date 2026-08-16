import time
import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def animate(i, dataList, ser):
    ser.write(b'g')  # Transmite o caratere 'g' para recebr os dados do arduino
    arduinoData_string = ser.readline().decode('ascii')  # Decodifica os dados recebidos do arduino como uma string
    # print(i)     #remova o comentário para ver                            # 'i' é uma variável que é incrementada

    try:
        arduinoData_float = float(arduinoData_string)  # Converte para float
        dataList.append(arduinoData_float)  # Adiciona à lista que contém o número fixo de pontos a serem animados.

    except:  # Ignorar se o ponto de dados for inválido
        pass

    dataList = dataList[-50:]  # Define o tamanho da lista de modo que a janela do gráfico tenha um número x de pontos.

    ax.clear()  # Limpa o último frame de dados
    ax.plot(dataList)  # Plota um novo frame

    ax.set_ylim([0, 1200])  # Coloca o limite do eixo Y
    ax.set_title("Dados do  Arduino")  # Coloca o título
    ax.set_ylabel("Valor")  # Coloca o título do eixo Y


dataList = []  # cria uma lista vazia para usar depois

fig = plt.figure()  # Cria a janela inicial
ax = fig.add_subplot(111)  # Adiciona um subplot a janela inicial

ser = serial.Serial("COM3", 9600)  # Estabelece comunicação serial com a porta COM e taxa de  BAUD para combinar com as do arduino
time.sleep(2)  # Delay para o Arduino iniciar a comunicção Serial

# Função de animação do Matplotlib que gerencia a plotagem em tempo real.
ani = animation.FuncAnimation(fig, animate, frames=100, fargs=(dataList, ser), interval=100)

plt.show()  # Mantém a plotagem constante
ser.close()  # Fecha conexão serial ao fechar a plotagem
