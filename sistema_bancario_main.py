#MENSAGENS

#VARIAVEIS

##Login e Senha
login = 'abcd123'
senha = 'abcd123'
login_usuario = 'ppbn'
senha_usuario = 'ppbn890'

##Limites
LIMITE_SAQUE = 500
LIMITE_ACUMULADO = 1500
saldo = 1000.00

##Data e Hora
from datetime import datetime
tempo = datetime.now()
time_now = tempo.strftime("%d-%m-%Y às %H:%M:%S")

##Operacoes

###Deposito
deposito_n = 0
deposito: [float] = [0 for x in range(0)]
### Saque
saque_n = 0
saque: [float] = [0 for x in range(0)]
saque_acumulado = 0


#SISTEMA BANCARIO

##Autenticacao
while (login != 'ppbn') and (senha != 'ppbn890'):
    login = (input('Insira o seu login: '))
    senha = (input('Insira a sua senha: '))

##Primeiras Informacoes
print('''
-----------------------------------
Seja muito bem-vindo ao XDBank!
Como você gostaria de ser chamado?
-----------------------------------''')
NOME = input()

print(f'''
-----------------------------------
É um prazer ter você aqui conosco,
{NOME}! Agora vamos te passar
algumas opções disponíveis aqui, 
ok?
-----------------------------------''')

print('''
-----------------------------------
Em qual dessas operações podemos
lhe ajudar hoje?

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------''')
operacao = int(input())

##Operacoes
while operacao is int(operacao):

    if operacao == 1:
        print('''
-----------------------------------
Por favor, informe qual o valor que
você deseja depositar.
-----------------------------------''')
        deposito.append(float(input()))

        while deposito[deposito_n] < 0:
            print('Não são permitidos depósitos negativos, tente novamente ou insira 0 (ZERO) para sair. ')
            deposito.insert(len(deposito)-1, float(input()))
            deposito.pop(len(deposito)-1)

        saldo += deposito[deposito_n]

        print(f'''
-----------------------------------
O depósito de R$ {deposito[deposito_n]:.2f}
foi realizado com sucesso!
Seu novo saldo é de R$ {saldo:.2f}
Podemos lhe ajudar em mais alguma
hoje, {NOME}?
Escolha uma das opções abaixo:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------''')
        deposito_n += 1
        operacao = int(input())
    elif operacao == 2:
        if saque_acumulado < LIMITE_ACUMULADO:
            print('''
-----------------------------------
Por favor, informe qual o valor que
você deseja sacar.
-----------------------------------''')
            saque.append(float(input()))
                
            while (saque[saque_n] > saldo) or (saque[saque_n] > LIMITE_SAQUE) or (saque[saque_n] < 0):
                
                while saque[saque_n] < 0:
                    print('Não são permitidos saques negativos, tente novamente ou insira 0 (ZERO) para sair. ')
                    saque.insert(len(saque)-1, float(input()))
                    saque.pop(len(saque)-1)

                while saque[saque_n] > saldo:
                    print('Saldo insuficiente para a transação. Por favor, tente novamente ou insira 0 (ZERO) para sair.')
                    saque.insert(len(saque)-1, float(input()))
                    saque.pop(len(saque)-1)

                while saque[saque_n] > LIMITE_SAQUE:
                    print('Esse valor está acima do seu limite por saque. Por favor, tente novamente.')
                    saque.insert(len(saque)-1, float(input()))
                    saque.pop(len(saque)-1) 

            saque_acumulado += saque[saque_n]
            saldo -= saque[saque_n]
            saque_n += 1   
                
            print(f'O saque no valor de R$ {saque[saque_n-1]:.2f} realizado com sucesso! Seu saldo é de R$ {(saldo):.2f}.')
        else:
            print(f'Você atingiu seu limite de saque de R$ {(LIMITE_ACUMULADO):.2f}')


        print(f'''
-----------------------------------
Podemos lhe ajudar em mais alguma
hoje, {NOME}?
Escolha uma das opções abaixo:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------''')
        operacao = int(input())
    elif operacao == 3:
        tempo = datetime.now()
        time_now = tempo.strftime("%d-%m-%Y às %H:%M:%S")
        print(f'''
-----------------------------------
Extrato gerado para a conta de
{NOME} em {time_now}. 
-----------------------------------''')
        print('Depósitos realizados no período:')
        for i in range(0, deposito_n):
            print(f'+ R$ {deposito[i]:.2f}')
            
        print()
        print('Saques realizados no período:')
        for j in range(0, saque_n):
            print(f'- R$ {saque[j]:.2f}')

        print()
        print(f'SALDO: R$ {saldo:.2f}')

            
        print(f'''
-----------------------------------
EXTRATO GERADO COM SUCESSO!
Podemos lhe ajudar em mais alguma
hoje, {NOME}?
Escolha uma das opções abaixo:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------''')
        operacao = int(input())
    elif operacao == 0:
        print(f'''
-----------------------------------
Muito obrigado por utilizar nossos
serviços, {NOME}!
Até a próxima!
-----------------------------------''')
        break
    else:
        print('Operação invalida, tente novamente!')
        operacao = int(input())                

#FIM DO CODIGO#
