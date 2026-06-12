soma = 0
while True:
    valor_saque = int(input("digite o valor que queira sacar:"))
sobra = valor_saque
sobra = sobra % 100
sobra = sobra % 50
sobra = sobra % 20

if sobra == 0:
        print("Saque realizado com sucesso")
        break
else:
    print("Não é possível realizar esse saque")