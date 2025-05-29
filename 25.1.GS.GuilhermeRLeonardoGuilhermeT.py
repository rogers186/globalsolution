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

#EXERCICIO 1A
qtd_desastres = int(input("Insira a quantidade de desastres: "))

#EXERCICIO 1B e 2
for i in range(qtd_desastres):
    print(f"\n--- Desastre {i + 1} ---")
    tipos_desastres.append(input("Tipo de desastre: "))
    paises.append(input("País: "))
    cidades.append(input("Cidade: "))
    bairros.append(input("Bairro: "))
    ruas.append(input("Rua: "))

    while True:
        total = int(input("Total de pessoas afetadas: "))
        c = int(input("Número de crianças (0-18 anos): "))
        a = int(input("Número de adultos (18-60 anos): "))
        i = int(input("Número de idosos (60+ anos): "))
        m = int(input("Número de pessoas com mobilidade reduzida: "))
        f = int(input("Número de feridos: "))
        if c + a + i + m + f == total:
            total_afetados.append(total)
            criancas.append(c)
            adultos.append(a)
            idosos.append(i)
            mobilidade_reduzida.append(m)
            feridos.append(f)
            break
        else:
            print("A soma das categorias não corresponde ao total de pessoas afetadas. Tente novamente.")

#EXERCICIO 3A
print(f"Total de desastres registrados: {qtd_desastres}")

#EXERCICIO 3B
total_geral = sum(total_afetados)
print(f"Total geral de pessoas afetadas: {total_geral}")

#EXERCICIO 3C
total_criancas = sum(criancas)
total_adultos = sum(adultos)
total_idosos = sum(idosos)
total_mobilidade = sum(mobilidade_reduzida)
total_feridos = sum(feridos)

print("Resumo de pessoas afetadas por categoria:")
print(f"Crianças: {total_criancas} | Adultos: {total_adultos} | Idosos: {total_idosos} | Mobilidade reduzida: {total_mobilidade} | Feridos: {total_feridos}")

#EXERCICIO 3D
categorias = ["Crianças", "Adultos", "Idosos", "Mobilidade reduzida", "Feridos"]
valores = [total_criancas, total_adultos, total_idosos, total_mobilidade, total_feridos]
indice_mais_afetada = valores.index(max(valores))
print(f"Categoria mais afetada: {categorias[indice_mais_afetada]}")

#EXERCICIO 3E
indice_mais_afetado = total_afetados.index(max(total_afetados))
print("Desastre com maior número de afetados")
print(f"Tipo: {tipos_desastres[indice_mais_afetado]}")
print(f"Local: {ruas[indice_mais_afetado]}, {bairros[indice_mais_afetado]}, {cidades[indice_mais_afetado]}, {paises[indice_mais_afetado]}")





