#Grupo AquaSafe - 1TSCPG
#Guilherme Norio Takada - RM565246
#Guilherme Rodrigues Fernandes - RM565084
#Leonardo Vargas Palmeira - RM563777

tipos_desastres = []
paises = []
cidades = []
bairros = []
ruas = []
total_afetados = []
criancas = []
adultos = []
idosos = []
mobilidade_reduzida = []
feridos = []

quantidade_desastres = int(input("Quantos desastres foram registrados?: "))

for i in range(quantidade_desastres):
    print(f"\n--- Cadastro do desastre {i+1} ---")

    tipo = input("Qual desastre ocorreu(ex: incêndio, enchente, etc.)?: ")
    pais = input("Em que país ocorreu?: ")
    cidade = input("Em que cidade ocorreu?: ")
    bairro = input("Em que bairro ocorreu?: ")
    rua = input("Em que rua ocorreu?: ")

    while True:
        total = int(input("Quantas pessoas foram afetadas?: "))
        qtd_criancas = int(input("Quantas crianças (0-18 anos) foram afetadas?: "))
        qtd_adultos = int(input("Quantos adultos (18-60 anos) foram afetados?: "))
        qtd_idosos = int(input("Quantos idosos (60+ anos) foram afetados?: "))
        qtd_mobilidade = int(input("Quantas pessoas com mobilidade reduzida foram afetadas?: "))
        qtd_feridos = int(input("Quantas pessoas se feriram?: "))

        soma = qtd_criancas + qtd_adultos + qtd_idosos

        if soma == total:
            break
        else:
            print("A soma das categorias não corresponde ao total de pessoas afetadas.")
            print("Por favor, insira os dados novamente.\n")