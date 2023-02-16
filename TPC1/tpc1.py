def distrIdades(dados):

    idadesDict = {} #dicionario para a distribuiçao

    for i in range(len(dados)):
        
        if dados[i][1] in idadesDict:
            idadesDict[dados[i][1]] += 1

        else:
            idadesDict[dados[i][1]] = 1
        i +=1

    print(idadesDict)

def maxAge(dados):
    maxAge = 0

    for i in range(len(dados)):
        if(int(dados[i][0])>maxAge):
            maxAge = int(dados[i][0])
        i+=1

    print(f"A idade maxima é {maxAge}")



def main():
        i = 0
        dados = []

        with open("/home/henrique/Desktop/uminho_lei/3_ano/2_semestre/PL/praticas/tpc1/myheart.csv") as f:
            lixo = f.readline() #para tirar a primeira linha
            contents = f.readlines()

            for content in contents:#partir as linhas nas virgulas e guardar numa lista de listas
                content = content.strip('\n')
                dados.append(content.split(","))
        
        distrIdades(dados)
        maxAge(dados)




if __name__ == "__main__":
    main()