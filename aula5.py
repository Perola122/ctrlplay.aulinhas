notas = int(input("Nota do Aluno: "))

if notas >= 7:
    print("Você foi aprovado.")

elif notas >= 6:#pode ter vários elif
    print("Você está de recuperação")

else:
    print("Você está reprovado")
