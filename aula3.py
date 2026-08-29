
#correurapido = True
#if correurapido:
#   print("Voce caiu...")

#correuNoCorredor = input("Voce correu rápido?  ")
#if correuNoCorredor == "sim":
 ##   print("Você caiu...")
#elif correuNoCorredor == "Nao" or "nao":
#    print("Você nao caiu.")

nome = input("Qual o seu nome?")
idade = int(input("Quantos anos voce tem? "))
cidade = input("Onde você mora?")

print("Olá", nome, "!")

if idade >= 18:
    print("Voce é maior de idade!!!")
elif idade < 18:
    print("Voce é menor de idade!!!")
else:
    print("Qual o seu problema?")
