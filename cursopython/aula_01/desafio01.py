# Desafio --> Calculo de Bonus com Entrada de Usuario
CONST_BONUS = 1000
nome_usuario = input("Digite o seu nome: ")
salario_usuario = float(input("Digite o seu salario: "))
bonus_usuario = float(input("Digite a pct(%) do bonus: "))
valor_bonus = round(CONST_BONUS + (salario_usuario * bonus_usuario),2)

print(f"O usuario {nome_usuario} possuiu o bonus de {valor_bonus}")