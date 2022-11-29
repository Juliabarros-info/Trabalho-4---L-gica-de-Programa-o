i=0
z=0
while z!=5:
    print("\n---MENU---")
    print("1- Cadastro")
    print("2- Ler")
    print("3- Deletar")
    print("4- Atualizar")
    print("5- Sair")
    print("\nDigite a sua opção:")
    o = int(input("> "))
    if o ==1:
        arquivo = open("execut.txt", "w")
        for i in range(1): 
            nome = input("\nNome: ")
            endereco = input("Endereço: ")
            celular = input("Celular: ")
            cpf = input("CPF: ")
            email = input("E-mail: ")
            senha = input("Senha: ")
            arquivo.write("%s\n"%nome)
            arquivo.write("%s\n"%endereco)
            arquivo.write("%s\n"%celular)
            arquivo.write("%s\n"%cpf)
            arquivo.write("%s\n"%email)
            arquivo.write("%s\n"%senha)
        arquivo.close()
        
    if o ==2:
        arquivo = open("execut.txt" ,"r")
        ler = arquivo.read()
        print(ler)
        arquivo.close()
    if o ==3:
        print("\nDeseja deletar cadastro? ")
        print("1- Sim")
        print("2- Não")
        print("\nDigite a sua opção:")
        d = int(input("> "))
        if d ==1:
            print("\nQual campo você deseja deletar? ")
            print("1- Nome")
            print("2- Endereço")
            print("3- Celular")
            print("4- CPF")
            print("5- E-mail")
            print("6- Senha")
            print("7- Apagar todos os campos")
            e = int(input("> "))
            if e==1:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[0]=""
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e==2:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[1]=""
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e==3:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[2]=""
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e==4:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[3]=""
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e==5:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[4]=""
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e==6:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[5]=""
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e==7:
                arquivo = open("execut.txt","w")
                arquivo.close()
        else:
            print("\n-----DADOS NÃO DELETADOS-----")
            arquivo.close()
    if o ==4:
        print("\nDeseja atualizar cadastro? ")
        print("1- Sim")
        print("2- Não")
        print("\nDigite a sua opção:")
        a = int(input("> "))
        if a==1:
            print("\nQual campo você deseja atualizar? ")
            print("1- Nome")
            print("2- Endereço")
            print("3- Celular")
            print("4- CPF")
            print("5- E-mail")
            print("6- Senha")
            print("7- Apagar todos os campos")
            e = int(input("> "))
            if e ==1:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[0]=input("\nNovo Nome: ")
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e ==2:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[1]=input("\nNovo Endereço: ")
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e ==3:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[2]=input("\nNovo Celular: ")
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e ==4:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[3]=input("\nNovo CPF: ")
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e ==5:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[4]=input("\nNovo E-mail: ")
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e ==6:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                lista[5]=input("\nNova Senha: ")
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()
            if e==7:
                arquivo = open("execut.txt","r")
                lista = arquivo.readlines()
                arquivo.close()
                lista=[s.replace("\n","") for s in lista]
                print("----NOVOS DADOS----")
                lista[0]=input("\nNovo Nome: ")
                lista[1]=input("Novo Endereço: ")
                lista[2]=input("Novo Celular: ")
                lista[3]=input("Novo CPF: ")
                lista[4]=input("Novo E-mail: ")
                lista[5]=input("Nova Senha: ")
                arquivo = open("execut.txt","w")
                for i in lista:
                    arquivo.write("%s\n"%i)
                arquivo.close()  
        else:
            print("\n---DADOS NÃO ATUALIZADOS---")
            arquivo.close()
    if o ==5:
        print("\nDeseja sair? ")
        print("1- Sim")
        print("2- Não")
        print("\nDigite a sua opção:")
        s = int(input("> "))
        if s ==1:
            print("\n---VOCÊ SAIU DO SISTEMA--- ")
            z=5
        else:
            print("\n---VOCÊ CONTINUA NO SISTEMA--- ")
    if o>5:
        print("\n=====ESSA OPÇÃO NÃO EXISTE====\nDIGITE NOVAMENTE UM NÚMERO PRESENTE NO MENU PRINCIPAL")
        