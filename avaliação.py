peso = float(input("digite eu peso:"))
altura = float(input("digite sua altura:"))

IMC = peso/(altura**2)
if IMC < 18.5:
    print("abaixo de peso")
elif IMC < 24.9:
    print("peso normal")
elif IMC < 29.9:
    print("sobrepeso")
elif IMC < 34.9:
    print("obesidade grau I")
elif IMC < 39.9:
    print("obesidade grau II")
else:
    print("obesidade grau III")
