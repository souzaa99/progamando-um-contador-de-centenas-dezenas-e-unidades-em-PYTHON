numero = int(input("Digite um número inteiro menor que 1000: "))
if 0 < numero < 1000:
    centena = numero // 100
    numero = numero % 100

    dezena= numero // 10
    numero= numero % 10

    unidade= numero // 1
    numero= numero % 1

    print("Seu número tem:", end=" ")
    if centena > 0 :
        if centena < 2:
            print(centena ,"centena" ,end= "")
        else:
            print(centena ,"centenas",end= "")
        if dezena == 0 and unidade == 0:
            print("")
        elif dezena > 0 and unidade == 0:
            print(" e ", end="")
        elif dezena == 0 and unidade > 0:
            print(" e ", end="")
        elif dezena > 0 and unidade > 0:
            print(", ", end="")
        else:
            print(", ", end="")
    if dezena>0:
        if dezena<2:
            print(dezena ,"dezena",end= "")
        else:
            print(dezena ,"dezenas",end= "")
        if unidade > 0 and centena == 0:
            print(" e ", end="")
        elif unidade > 0:
            print(" e ", end="")
        else:
            print("", end="")
    if unidade>0:
        if unidade < 2 :
            print( unidade,"unidade" )
        else:
            print( unidade,"unidades")
else:
    print("numero invalido")