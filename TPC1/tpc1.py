import math

def distrGen(dados):

    genDict = {} #dicionario para a distribuiçao

    for i in range(len(dados)):
        
        if (dados[i][1] in genDict) and dados[i][5]=='1':
            genDict[dados[i][1]] += 1

        elif (dados[i][1] not in genDict) and dados[i][5]=='1':
            genDict[dados[i][1]] = 1
        i +=1

    print(f"Distribuição da doença por sexo: {genDict}")

def maxAge(dados):
    maxAge = 0

    for i in range(len(dados)):
        if(int(dados[i][0])>maxAge):
            maxAge = int(dados[i][0])
        i+=1

    return maxAge


def doentesIntervalos(category, interval,data):
    struct = dict()

    for info in data:
        value = int(info[category-1])
        lower = 0
        higher = interval - 1

        if value > 0:
            lower = interval * (math.ceil(value / interval) - 1)
            higher = (interval * math.ceil(value / interval)) - 1

        key = f"[{lower}-{higher}]"

        # Verificamos se a chave atual já se encontra no dicionário (retornamos None caso esta não exista)
        if not struct.get(key, None):
            struct[key] = 0

        if int(info[5]):
            struct[key] += 1

    print(dict(sorted(struct.items())))  # Ordenamos o dicionário por ordem ascendente de intervalos (maior legibilidade)



def main():
        i = 0
        dados = []

        with open("/home/henrique/Desktop/uminho_lei/3_ano/2_semestre/PL/praticas/tpc1/myheart.csv") as f:
            lixo = f.readline() #para tirar a primeira linha
            contents = f.readlines()

            for content in contents:#partir as linhas nas virgulas e guardar numa lista de listas
                content = content.strip('\n')
                dados.append(content.split(","))
        
        distrGen(dados)
        idadeMax = maxAge(dados)
        doentesIntervalos(0,5,dados)



if __name__ == "__main__":
    main()