#VARIAVEIS
##Tempo
from datetime import datetime
tempo = datetime.now()
time_now = tempo.strftime("%d-%m-%Y às %H:%M:%S")

##Login e Senha
contas = {}
usuarios = {}
validacao = False
validacao_conta = False
numero_conta = 0
nome = 'PADRAO'
login = 'abcd123'
senha = 'abcd123'
login_usuario = 'ppbn'
senha_usuario = 'ppbn890'
operacao_pass = False

##Limites
LIMITE_SAQUE = 500
LIMITE_ACUMULADO = 1500
saldo = 1000.00

##Deposito
deposito_n = 0
deposito: [float] = [0 for x in range(0)]

## Saque
saque_n = 0
saque: [float] = [0 for x in range(0)]
saque_acumulado = 0

#MENSAGENS

mensagens = {
'primeiras_mensagens': {'mensagem_00':
'''-----------------------------------
Oi! Espero que essa mensagem esteja
encontrando você bem!
No que podemos lhe ajudar hoje?
[1] Login
[2] Cadastrar usuário
[3] Cadastrar conta
[0] Sair
-----------------------------------''',
'mensagem_00a':
'''-----------------------------------
Cadastro realizado com sucesso!
O que mais podemos fazer por você 
hoje?
[1] Login
[2] Cadastrar usuário
[3] Cadastrar conta
[0] Sair
-----------------------------------''',
'mensagem_00b':
'''-----------------------------------
O que mais podemos fazer por você 
hoje?
[1] Login
[0] Sair
-----------------------------------''',
'mensagem_01': 
'''-----------------------------------
Seja muito bem-vindo ao XDBank!
Como você gostaria de ser chamado?
-----------------------------------''', 
'mensagem_02': 
f'''-----------------------------------
É um prazer ter você aqui conosco,
{nome}! Agora vamos te passar
algumas opções disponíveis aqui, 
ok?
-----------------------------------''',
'mensagem_03': 
'''-----------------------------------
Em qual dessas operações podemos
lhe ajudar hoje?

[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------'''},
'mensagem_saque': 
'''-----------------------------------
Por favor, informe qual o valor que
você deseja sacar.
-----------------------------------''', 
'mensagem_operacao':
f'''-----------------------------------
Podemos lhe ajudar em mais alguma
hoje, {nome}?
Escolha uma das opções abaixo:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------''', 
'mensagem_deposito_01':
'''-----------------------------------
Por favor, informe qual o valor que
você deseja depositar.
-----------------------------------''',
'mensagem_deposito_02': 
'''O depósito de R$ {deposito[deposito_n-1]:.2f}
foi realizado com sucesso!
Seu novo saldo é de R$ {saldo:.2f}.''', 
'mensagem_extrato':
f'''-----------------------------------
Extrato gerado para a conta de
{nome} em {time_now}. 
-----------------------------------''',
'mensagem_saida':
f'''-----------------------------------
Muito obrigado por utilizar nossos
serviços, {nome}!
Até a próxima!
-----------------------------------'''
}

## Funcoes

def funcao_saque(*, total_saque, total_limite, saque_permitido):  
    global saque
    global saque_n
    global saque_acumulado
    global saldo
    global operacao

    if total_saque < total_limite:
        print(mensagens['mensagem_saque'])
        saque.append(float(input()))
                
        while (saque[saque_n] > saldo) or (saque[saque_n] > saque_permitido) or (saque[saque_n] < 0):
                
            while saque[saque_n] < 0:
                print('Não são permitidos saques negativos, tente novamente ou insira 0 (ZERO) para sair. ')
                saque.insert(len(saque)-1, float(input()))
                saque.pop(len(saque)-1)

            while saque[saque_n] > saldo:
                print('Saldo insuficiente para a transação. Por favor, tente novamente ou insira 0 (ZERO) para sair.')
                saque.insert(len(saque)-1, float(input()))
                saque.pop(len(saque)-1)

            while saque[saque_n] > saque_permitido:
                print('Esse valor está acima do seu limite por saque. Por favor, tente novamente.')
                saque.insert(len(saque)-1, float(input()))
                saque.pop(len(saque)-1) 

        saque_acumulado += saque[saque_n]
        saldo -= saque[saque_n]
        saque_n += 1   
                
        print(f'O saque no valor de R$ {saque[saque_n-1]:.2f} realizado com sucesso! Seu saldo é de R$ {(saldo):.2f}.')
    else:
        print(f'Você atingiu seu limite de saque de R$ {(total_limite):.2f}')


    print(f'''-----------------------------------
Podemos lhe ajudar em mais alguma
hoje, {nome}?
Escolha uma das opções abaixo:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------''')
    operacao = int(input())

def funcao_deposito():
    global deposito
    global deposito_n
    global saldo
    global operacao

    print(mensagens['mensagem_deposito_01'])
    deposito.append(float(input()))

    while deposito[deposito_n] < 0:
        print('Não são permitidos depósitos negativos, tente novamente ou insira 0 (ZERO) para sair. ')
        deposito.insert(len(deposito)-1, float(input()))
        deposito.pop(len(deposito)-1)

    saldo += deposito[deposito_n]

    print(f'''O depósito de R$ {deposito[deposito_n]:.2f}
foi realizado com sucesso!
Seu novo saldo é de R$ {saldo:.2f}.''')
    print(f'''-----------------------------------
Podemos lhe ajudar em mais alguma
hoje, {nome}?
Escolha uma das opções abaixo:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------''')
    deposito_n += 1
    operacao = int(input())
    

def funcao_extrato():
    global operacao
    global time_now
    
    tempo = datetime.now()
    time_now = tempo.strftime("%d-%m-%Y às %H:%M:%S")
    print(f'''-----------------------------------
Extrato gerado para a conta de
{nome} em {time_now}. 
-----------------------------------''')
    print()
    print('Depósitos realizados no período:')
    for i in range(0, deposito_n):
        print(f'+ R$ {deposito[i]:.2f}')

    print('Saques realizados no período:')
    for j in range(0, saque_n):
        print(f'- R$ {saque[j]:.2f}')

    print()
    print(f'SALDO: R$ {saldo:.2f}')

    print('EXTRATO GERADO COM SUCESSO!')        
    print(f'''-----------------------------------
Podemos lhe ajudar em mais alguma
hoje, {nome}?
Escolha uma das opções abaixo:
[1] Depósito
[2] Saque
[3] Extrato
[0] Sair
-----------------------------------''')
    operacao = int(input())

def funcao_cadastrar_usuarios(nome, data_nascimento, cpf, endereco, login, password, password_validation):
    global usuarios
    global validacao
    validacao = cpf in usuarios

    if (password != password_validation) and (validacao == False):
        print('A confirmação da senha não confere, tente novamente.')
    elif (validacao == True) and (password == password_validation):
        print('O CPF informado já possui cadastro! Tente novamente.')
    elif (password != password_validation) and (validacao == True):
        print('A confirmação da senha não confere e o CPF informado já possui cadastro! Tente novamente.')       
    else:
        usuarios.update({cpf: {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'usuario': login, 'password': password, 'password_validation': password_validation}})
    
    print(f'''
***Usuário criado com sucesso!***
!!!Anote os seus dados de Cadastro:!!!
NOME: {usuarios[cpf]['nome']}
DATA DE NASCIMENTO: {usuarios[cpf]['data_nascimento']}
ENDEREÇO: {usuarios[cpf]['endereco']}
USUÁRIO: {usuarios[cpf]['usuario']}
SENHA: {usuarios[cpf]['password']}''')
    
    return validacao, usuarios

def funcao_cadastrar_contas(cpf_usuario, conta_usuario):
    global usuarios
    global contas
    global validacao
    global contas
    global numero_conta
    global validacao_conta

    validacao = cpf_usuario in usuarios
    validacao_conta = conta_usuario in contas

    if validacao == True:
        print(f'Esse CPF pertence a {usuarios[cpf_usuario]['nome']}.')
        print('Informe a senha do usuário para continuar: ')
        senha_informada = input()

        while (senha_informada != usuarios[cpf_usuario]['password']) and (senha_informada != '0'):
            print('A senha informada está incorreta, tente novamente ou pressione [0] para sair.')
            print('Informe a senha do usuário: ')
            senha_informada = input()
    
        if senha_informada != '0':

            contas.update({numero_conta+1: {'cpf': cpf_usuario, 'agencia': '001', 'nome': usuarios[cpf_usuario]['nome'], 'senha': usuarios[cpf_usuario]['password']}})
            print(f'''
***Conta criada com sucesso!***
!!!Anote os seus dados de acesso:!!!
AGÊNCIA: {contas[numero_conta+1]['agencia']}
CONTA: {numero_conta+1}
LOGIN: {contas[numero_conta+1]['cpf']}
SENHA: {contas[numero_conta+1]['senha']}''')
            numero_conta += 1
            return validacao, usuarios
        else:
            print('Obrigado!')

    else:
        print('Não encontramos usuários cadastrados para o CPF informado! Tente novamente.')

#SISTEMA BANCARIO

##Boas-vindas
print(mensagens['primeiras_mensagens']['mensagem_00'])
operacao = int(input())

while operacao_pass == False:
    
    if operacao_pass == False:
        if operacao == 2:
            funcao_cadastrar_usuarios(nome= input('Nome do Usuário: '), data_nascimento= input('Data de Nascimento: '), cpf= input('CPF: '), endereco= input('''Endereço 
    (EXEMPLO: Rua, Número - Bairro - Cidade/SiglaEstado): '''), login= input('Digite um nome de usuário: '), password= input('Agora insira uma senha: '), password_validation= input('Repita a senha para a validação: '))

            print(mensagens['primeiras_mensagens']['mensagem_00a'])
            operacao = int(input())
            if operacao != 2:
                continue
        elif operacao == 3:
            funcao_cadastrar_contas(cpf_usuario= input('Insira o CPF do titular da conta: '), conta_usuario= numero_conta)

            print(mensagens['primeiras_mensagens']['mensagem_00a'])
            operacao = int(input())
            if operacao != 2:
                continue
        elif operacao == 1:
            agencia_pass = (input('Número da agêcia: '))
            conta_pass = int((input('Número da sua conta: ')))
            senha_pass = (input('Digite a sua senha: '))

            validacao_conta = conta_pass in contas

            if validacao_conta == True:

                while (agencia_pass != contas[conta_pass]['agencia']) or (senha_pass != contas[conta_pass]['senha']):
                    print('Dados incorretos, tente novamente!')
                    agencia_pass = (input('Número da agêcia: '))
                    conta_pass = int((input('Número da sua conta: ')))
                    senha_pass = (input('Digite a sua senha: '))
                else:
                    operacao_pass = True
            else:
                print('Conta não encontrada!')
                print(mensagens['primeiras_mensagens']['mensagem_00b'])
                operacao = int(input())
        elif operacao == 0:
            print(f'''-----------------------------------
Muito obrigado por utilizar nossos
serviços, {nome}!
Até a próxima!
-----------------------------------''')
            break
        else:
            print('Operação invalida, tente novamente!')
            operacao = int(input())        

        
    if operacao_pass == True:
        ##Primeiras Informacoes
        print(mensagens['primeiras_mensagens']['mensagem_01'])
        nome = input()

        print(f'''-----------------------------------
É um prazer ter você aqui conosco,
{nome}! Agora vamos te passar
algumas opções disponíveis aqui, 
ok?
-----------------------------------''')
        print(mensagens['primeiras_mensagens']['mensagem_03'])
        operacao = int(input())

        ##Operacoes Bancarias
        while operacao is int(operacao):

            if operacao == 1:
                funcao_deposito(deposito, deposito_n, saldo, operacao)
            elif operacao == 2:
                #corrigir limite do saque
                funcao_saque(total_saque = saque_acumulado, total_limite = LIMITE_ACUMULADO, saque_permitido = LIMITE_SAQUE)
            elif operacao == 3:
                funcao_extrato()
            elif operacao == 0:
                print(f'''-----------------------------------
Muito obrigado por utilizar nossos
serviços, {nome}!
Até a próxima!
-----------------------------------''')
                break
            else:
                print('Operação invalida, tente novamente!')
                operacao = int(input())
    else:
        if operacao == 0:
            print(f'''-----------------------------------
Muito obrigado por utilizar nossos
serviços, {nome}!
Até a próxima!
-----------------------------------''')
            break


#FIM DO CODIGO#