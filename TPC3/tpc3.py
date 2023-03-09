import re
import json

file = 'processos.txt'


def pointA():

    with open(file, 'r', encoding='utf8') as f:
        processos = f.read()

        anos = re.findall(r'(\d{4})-\d{2}-\d{2}', processos)
        frequencias = {}

        for ano in anos:
            if ano in frequencias:
                frequencias[ano] += 1
            else:
                frequencias[ano] = 1

        for ano, frequencia in frequencias.items():
            print(f'Ano: {ano}, Frequência: {frequencia}')

def pointB():

    nomes_proprios = {}
    apelidos = {}

    with open(file, 'r', encoding='utf8') as f:
        for line in f:
            fields = line.split("::")
            if len(fields) < 3:
                continue

            nome_completo = fields[2]
            nomes = re.findall(r'\b\w+\b', nome_completo)

            primeiro_nome = nomes[0]
            ultimo_nome = nomes[-1]

            seculo = int(fields[1].split("-")[0]) // 100 + 1

            # Frequência de nomes próprios por século
            tipo = "nomes_proprios"
            if seculo not in nomes_proprios:
                nomes_proprios[seculo] = {}
            nomes_proprios[seculo][primeiro_nome] = nomes_proprios[seculo].get(primeiro_nome, 0) + 1

            # Frequência de apelidos por século
            tipo = "apelidos"
            if seculo not in apelidos:
                apelidos[seculo] = {}
            apelidos[seculo][ultimo_nome] = apelidos[seculo].get(ultimo_nome, 0) + 1

    # Top 5 nomes próprios por século
    print("Top 5 nomes próprios por século:")
    for seculo, nomes in nomes_proprios.items():
        top_nomes = sorted(nomes.items(), key=lambda x: x[1], reverse=True)[:5]
        print(f"Século {seculo}: {[nome[0] for nome in top_nomes]}")

    # Top 5 apelidos por século
    print("\nTop 5 apelidos por século:")
    for seculo, apelidos_seculo in apelidos.items():
        top_apelidos = sorted(apelidos_seculo.items(), key=lambda x: x[1], reverse=True)[:5]
        print(f"Século {seculo}: {[apelido[0] for apelido in top_apelidos]}")

def pointC():

    relacoes = {}

    with open(file, 'r', encoding='utf-8') as f:
        for line in f:
            match = re.search(r'([A-Za-z ]+)\.+\s*(?:Proc\.)(\d+)\.', line)
            if match:
                relacao, proc_num = match.group(1, 2)
                relacoes[relacao] = relacoes.get(relacao, 0) + 1

    # imprimir resultados ordenados por frequência decrescente
    print("Frequências de relações:")
    for relacao, freq in sorted(relacoes.items(), key=lambda x: x[1], reverse=True):
        print(f"{relacao}: {freq}")

def pointD():
   
    input_file = open(file, 'r')
    output_file = open('output.json', 'w')

    output_list = []

    for i in range(20):
        line = input_file.readline().strip()
        fields = re.split(r"::", line)
        id = fields[0]
        data = fields[1]
        nome_proprio, *apelido = fields[2].split()
        apelido = " ".join(apelido)
        pai = fields[3]
        mae = fields[4]
        relacoes = fields[5] if fields[5] else "[]"
        record = {
            "id": id,
            "data": data,
            "nome_proprio": nome_proprio,
            "apelido": apelido,
            "pai": pai,
            "mae": mae,
            "relacoes": relacoes
        }
        output_list.append(record)

    json.dump(output_list, output_file, indent=2)
    output_file.write('\n')

if __name__ == "__main__":
    pointD()