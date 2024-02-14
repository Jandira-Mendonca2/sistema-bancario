menu='''
    [1] Depositar
    [2] Sacar 
    [3] Extrato
    [0] Sair
'''
saldo=0
limite=500
extrato=""
numero_saques=0
limite_saques=3
#d=valor
while True:
    opcao=input(menu)
    if opcao=='1':
        #print("Deposita")
        d=float(input("Valor depositado: "))
        if d>0:
            saldo += d
            extrato += f"Depósito R$ {d:.2f}\n"
        #print(d)
        else:
            print("Operação falhou! O valor depositado é inválido.")
    elif opcao=='2':
        #print("Saque")
        d=float(input("Valor do saque: "))
        excedeu_saldo=d>saldo
        excedeu_limite=d>limite
        excedeu_saques=numero_saques>=limite_saques
        if excedeu_saldo:
            print("Operação falhou! O saldo é insuficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excedeu o limite. ")
        elif excedeu_saques:
            print("Operação falhou! Excedeu o número máximo de saques.")
        elif d>0:
            saldo -=d
            extrato += f"Saque R$ {d:.2f}\n"
            numero_saques +=1
        else:
            print("Operação falhou! O valor informado é inválido.") 
    elif opcao=='3':
        #print("Extrato")
        print("----------Extrato----------")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("---------------------------")
    elif opcao=='0':
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada!")
