maior = float('inf')
cont = 1 #precisa ter uma variavel de contador
while cont <= 10: #substituir "soma" por contador
    num = int(input("Digite um número: "))
    if num > maior:
       maior = num
    cont +=1 #cada vez que rodar, o cont irá aumentar
print('O maior número é', maior)

