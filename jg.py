from random import randint
from time import sleep

print('-='*20)
print('Bem vindo ao jogo de matemática'.upper())
print('-='*20)

cont = 0

numerodaquestao1 = 1
numerodaquestao2 = 1
numerodaquestao3 = 1

while True:
    simbolo = str(input('Deseja treinar qual símbolo matematico?'))
    dificuldade = int(input('Você quer treinar no fácil [1], médio [2] ou no difícil [3]:'))
    if dificuldade == 1:
        if simbolo == 'x':
            while True:
                numero = randint(1,12), randint(1,101)
                resposta = numero[0] * numero[1]
                sleep(0.5)
                respostadojogador = int(input(f'{numerodaquestao1}ª questão: {numero[0]} x {numero[1]} ='))

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao1 +=1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao1 += 1
                    sleep(1)

                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break

        elif simbolo =='/':
            while True:
                numero = randint(1,120), randint(1,50)
                resposta = numero[0] / numero[1]

                respostadojogador = int(input(f'{numerodaquestao1}ª questão: {numero[0]} / {numero[1]} ='))

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao1 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao1 += 1
                    sleep(1)

                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break


        elif simbolo =='-':
            while True:
                numero = randint(1,120), randint(1,50)
                respostadojogador = int(input(f'{numerodaquestao1}ª questão: {numero[0]} - {numero[1]} ='))
                resposta = numero[0] - numero[1]

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao1 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao1 += 1
                    sleep(1)

                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break
        elif simbolo == '+':
            while True:
                numero = randint(1,100), randint(1,200)
                resposta = numero[0] + numero[1]

                respostadojogador = int(input(f'{numerodaquestao1}ª questão: {numero[0]} + {numero[1]} ='))

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao1 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    sleep(1)
                    numerodaquestao1 += 1
                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break


    elif dificuldade == 2:
        if simbolo == 'x':
            while True:
                numero = randint(1,20), randint(1,150)
                resposta = numero[0] * numero[1]
                sleep(0.5)

                respostadojogador = int(input(f'{numerodaquestao2}ª questão: {numero[0]} x {numero[1]} ='))

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao2 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao2 += 1
                    sleep(1)

                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break

        elif simbolo =='/':
            while True:
                numero = randint(1,400), randint(1,100)
                resposta = numero[0] / numero[1]

                respostadojogador = int(input(f'{numerodaquestao2}ª questão: {numero[0]} x {numero[1]} ='))


                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao2 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao2 += 1
                    sleep(1)

                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break


        elif simbolo =='-':
            while True:
                numero = randint(1,300), randint(1,300)
                resposta = numero[0] - numero[1]

                respostadojogador = int(input(f'{numerodaquestao2}ª questão: {numero[0]} x {numero[1]} ='))

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao2 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao2 += 1
                    sleep(1)
                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break
        elif simbolo == '+':
            while True:
                numero = randint(1,300), randint(1,600)
                respostadojogador = int(input(f'{numerodaquestao2}ª questão: {numero[0]} x {numero[1]} ='))
                resposta = numero[0] + numero[1]

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao2 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao2 += 1
                    sleep(1)
                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break
    if dificuldade == 3:
        if simbolo == 'x':
            while True:
                numero = randint(1,180), randint(1,200)
                resposta = numero[0] * numero[1]

                respostadojogador = int(input(f'{numerodaquestao3}ª questão: {numero[0]} x {numero[1]} ='))

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao3 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    sleep(1)
                    numerodaquestao3 += 1

                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break
        elif simbolo =='/':
            while True:
                numero = randint(1,1200), randint(1,200)
                resposta = numero[0] / numero[1]
                respostadojogador = int(input(f'{numerodaquestao3}ª questão: {numero[0]} / {numero[1]} ='))

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao3 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao3 += 1
                    sleep(1)

                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break


        elif simbolo =='-':
            while True:
                numero = randint(1,900), randint(1,1500)
                resposta = numero[0] - numero[1]

                respostadojogador = int(input(f'{numerodaquestao3}ª questão: {numero[0]} - {numero[1]} ='))


                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao3 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao3 += 1
                    sleep(1)
                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break
        elif simbolo == '+':
            while True:
                numero = randint(1,900), randint(1,1800)
                respostadojogador = int(input(f'{numerodaquestao3}ª questão: {numero[0]} + {numero[1]} ='))
                resposta = numero[0] + numero[1]

                if respostadojogador == resposta:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Parabéns, você acertou!!')
                    cont +=1
                    numerodaquestao3 += 1
                    sleep(1)
                else:
                    sleep(0.3)
                    print(f'A resposta certa é {resposta}! Você errou!!')
                    numerodaquestao3 += 1
                    sleep(1)
                continuar = str(input('Quer continuar?')).lower()
                if continuar == 'n':
                    break


    print('[1] Deseja treinar treinar outro operador matemático.')
    print('[2] Encerrar programa.')
    pause = int(input('Digite:'))
    if pause == 2:
        break

if cont == 1:
    print(f'Você acertou {cont} cáculo matmático!')
elif cont > 1:
    print(f'Você acertou {cont} cáculos matmáticos!')
else:
    print('Você não acertou nenhum cálculo matemático')


