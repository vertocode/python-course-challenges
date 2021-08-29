import random
n = random.randint(0, 5)
r =  int(input("Tente adivinhar o número que o computador pensou de 0 - 5, qual é: "))
print("Você acertou!" if n == r else "Você errou!")