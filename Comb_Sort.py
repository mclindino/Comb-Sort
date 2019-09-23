#CombSort - Matheus Lindino

def CombSort(Array):													#Define a função CombSort.
	Gap = len(Array)													#Gap recebe tamanho do Vetor.
	Troca = True
	while Gap > 1 or Troca:
		Gap = max(1, int((Gap * 10) / 13))								#Calcula o Gap. A função max() permite ter um valor minimo
		Troca = False													#de retorno, no qual é 1.
		for i in range(len(Array) - Gap):
			if Array[i] > Array[i + Gap]:								#Compara se o valor da posição atual é maior que a posição + Gap,
				Array[i], Array[i + Gap] = Array[i + Gap], Array[i]		#caso for, troca de posição. Ordenando o vetor em pares, separados
				Troca = True											#por um "salto" (Gap).

from random import *													#Importa biblioteca Random.
import time 															#Importa biblioteca Time.
N = 1000
while N <= 50000:
	Media = 0
	print('\033[37mTamanho do vetor = ''\033[34m',N)
	Array = [0] * N 													#Cria um Vetor de 0's com N posições.
	for i in range(0,10):
		for j in range(0,N):
			Array[j] = randint(0,N)										#Coloca numeros randomicos no vetor. A função Randint pode repetir numeros.
		Inicio = time.process_time()									#Inicia a contagem do tempo.
		CombSort(Array)
		Fim = time.process_time()										#Termina a contagem do tempo.
		Duracao = Fim - Inicio											#Calcula a duração
		Media = Duracao + Media 										#Calcula a Media dos casos.
		print('\t\033[37mTeste',(i + 1), '-> \033[32m', Duracao)
	print('\t\033[37mMedia = \033[31m',(Media / 10))
	if N == 1000:
		N = 5000
	else:
		N = N + 5000
