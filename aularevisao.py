idade = int(input("Digite sua idade: "))

ingresso = str(input("Você tem ingresso? "))

if idade < 18:
    print("Você não pode entrar sozinho.") 

elif idade >= 18 and (ingresso == "Sim" or ingresso == "S" or ingresso == "SIM" or ingresso == "Ss" or ingresso == "ss" or ingresso == "sim"):
    print("Você é maior de idade, não precisa de um responsável e pode curtir o show!!")

elif idade >= 18 and (ingresso == "Não" or ingresso == "N" or ingresso == "Nao" or ingresso == "n" or ingresso == "nao"):
    print("Você é maior de idade, mas não tem ingresso, então não pode curtir o show!")


