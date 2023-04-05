salarioBruto = float(input("Insira o seu salário por hora trabalhada: ")) * float(input("Insira a quantidade de horas trabalhadas: "))

print(f"O salário bruto é de {salarioBruto} reais")
print(f"O valor do Imposto de Renda é de {salarioBruto*0.11} reais")
print(f"O valor INSS é de {salarioBruto*0.08} reais")
print(f"O valor do imposto relativo ao Sindicato é de {salarioBruto*0.05} reais")
print(f"O salário liquido é de {salarioBruto*0.76} reais")
