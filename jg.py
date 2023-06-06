from random import randint
from time import sleep

print('-='*20)
print('Bem vindo ao jogo de matemática'.upper())
print('-='*20)

acertosjogador1 = 0
acertosjogador2 = 0
acertosjogador3 = 0


numerodaquestao1 = 0
numerodaquestao2 = 0
numerodaquestao3 = 0

totaldeperguntas = 0

while True:
    simbolo = str(input('Deseja treinar qual símbolo matematico?'))
    while True:
        if simbolo != 'x' and simbolo != '/' and simbolo != '-' and simbolo != '+':
            print('erro, tente novamente! Use somente os símbolos x / + - ')
            simbolo = str(input('Deseja treinar qual símbolo matematico? '))
        else:
            break

    dificuldade = int(input('Você quer treinar no fácil [1], médio [2] ou no difícil [3]:'))
    while True:
        if dificuldade != 1 and dificuldade != 2 and dificuldade !=3:
            print('erro, tente novamente. Somente opções 1, 2 e 3')
            dificuldade = int(input('Você quer treinar no fácil [1], médio [2] ou no difícil [3]:'))
        else:
            break
    if dificuldade == 1:
        if simbolo == 'x':
            for c in range(10):
                numero = randint(1,12), randint(1,101)
                resposta = numero[0] * numero[1]
                sleep(0.5)
                respostadojogador = int(input(f'{numerodaquestao1 + 1}ª questão: {numero[0]} x {numero[1]} ='))
                totaldeperguntas +=1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador1 += 1
                    numerodaquestao1 +=1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao1 += 1
                    sleep(0.5)

        elif simbolo =='/':
            for c in range(10):
                numero = randint(1,120), randint(1,50)
                resposta = numero[0] / numero[1]

                respostadojogador = int(input(f'{numerodaquestao1 + 1}ª questão: {numero[0]} / {numero[1]} ='))
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador1 += 1
                    numerodaquestao1 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao1 += 1
                    sleep(0.5)



        elif simbolo =='-':
            for c in range(10):
                numero = randint(1,120), randint(1,50)
                respostadojogador = int(input(f'{numerodaquestao1 + 1}ª questão: {numero[0]} - {numero[1]} ='))
                totaldeperguntas += 1
                resposta = numero[0] - numero[1]

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador1 += 1
                    numerodaquestao1 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao1 += 1
                    sleep(0.5)


        elif simbolo == '+':
            for c in range(10):
                numero = randint(1,100), randint(1,200)
                resposta = numero[0] + numero[1]

                respostadojogador = int(input(f'{numerodaquestao1 + 1}ª questão: {numero[0]} + {numero[1]} ='))
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador1 += 1
                    numerodaquestao1 += 1
                    sleep(0.51)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    sleep(0.5)
                    numerodaquestao1 += 1


    elif dificuldade == 2:
        if simbolo == 'x':
            for c in range(10):
                numero = randint(1,20), randint(1,150)
                resposta = numero[0] * numero[1]
                sleep(0.5)

                respostadojogador = int(input(f'{numerodaquestao2 + 1}ª questão: {numero[0]} x {numero[1]} ='))
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador2 += 1
                    numerodaquestao2 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao2 += 1
                    sleep(0.5)



        elif simbolo =='/':
            for c in range(10):

                numero = randint(1,400), randint(1,100)
                resposta = numero[0] / numero[1]

                respostadojogador = int(input(f'{numerodaquestao2 + 1}ª questão: {numero[0]} / {numero[1]} ='))
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador2 += 1
                    numerodaquestao2 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao2 += 1
                    sleep(0.5)


        elif simbolo =='-':
            for c in range(10):
                numero = randint(1,300), randint(1,300)
                resposta = numero[0] - numero[1]

                respostadojogador = int(input(f'{numerodaquestao2 + 1}ª questão: {numero[0]} - {numero[1]} ='))
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador2 += 1
                    numerodaquestao2 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao2 += 1
                    sleep(0.5)

        elif simbolo == '+':
            for c in range(10):
                numero = randint(1,300), randint(1,600)
                respostadojogador = int(input(f'{numerodaquestao2 + 1}ª questão: {numero[0]} + {numero[1]} ='))
                totaldeperguntas += 1
                resposta = numero[0] + numero[1]

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador2 += 1
                    numerodaquestao2 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao2 += 1
                    sleep(0.5)

    if dificuldade == 3:
        if simbolo == 'x':
            for c in range(10):
                numero = randint(1,180), randint(1,200)
                resposta = numero[0] * numero[1]

                respostadojogador = int(input(f'{numerodaquestao3 + 1}ª questão: {numero[0]} x {numero[1]} ='))
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador3 += 1
                    numerodaquestao3 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    sleep(0.5)
                    numerodaquestao3 += 1


        elif simbolo =='/':
            for c in range(10):

                numero = randint(1,1200), randint(1,200)
                resposta = numero[0] / numero[1]
                respostadojogador = int(input(f'{numerodaquestao3 + 1}ª questão: {numero[0]} / {numero[1]} ='))
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador3 += 1
                    numerodaquestao3 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao3 += 1
                    sleep(0.5)




        elif simbolo =='-':
            for c in range(10):

                numero = randint(1,900), randint(1,1500)
                resposta = numero[0] - numero[1]

                respostadojogador = int(input(f'{numerodaquestao3 + 1}ª questão: {numero[0]} - {numero[1]} ='))
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador3 += 1
                    numerodaquestao3 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao3 += 1
                    sleep(1)



        elif simbolo == '+':
            for c in range(10):
                numero = randint(1,900), randint(1,1800)
                respostadojogador = int(input(f'{numerodaquestao3 + 1}ª questão: {numero[0]} + {numero[1]} ='))
                resposta = numero[0] + numero[1]
                totaldeperguntas += 1

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    acertosjogador3 += 1
                    numerodaquestao3 += 1
                    sleep(0.5)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao3 += 1
                    sleep(0.5)



    print('[1] Deseja treinar treinar outro operador matemático.')
    print('[2] Encerrar programa.')
    pause = int(input('Digite:'))
    if pause == 2:
        break



print(f'Número de questões acertadas:')
print(f'Facéis:{numerodaquestao1} Acertos: {acertosjogador1}')
print(f'Médias:{numerodaquestao2} Acertos: {acertosjogador2}')
print(f'Difíceis: {numerodaquestao3} Acertos: {acertosjogador3}')

if totaldeperguntas > 1:
    print(f'Totais de perguntas: {totaldeperguntas} perguntas')
else:
    print(f'Totais de perguntas: {totaldeperguntas} pergunta')

totaldeacertos = acertosjogador1 + acertosjogador2 + acertosjogador3
if totaldeacertos == 1:
    print('Você acertou apenas um cálculo matemático.')
else:
    print(f'totais de perguntas acertadas: {totaldeacertos} perguntas')


