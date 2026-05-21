chances = 5
palavra_secreta = 'batata'
while chances > 0: 
    palavra = input(f"Qual a palavra secreta? Você tem {chances} chances")
    chances -= 1
    #quando você erra, automaticamente você vai perdendo suas chances.
    if palavra == 'batata':
        print("Você acertou a palavra, toma aqui uma batata 🥔")
    #porém, quando você acerta a palavra, o break interrompe o while, ou seja, ele nao vai rodar pra sempre
        break

