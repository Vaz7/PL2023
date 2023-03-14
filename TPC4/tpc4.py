import csv
import json
import re

path = 'C:\\Users\\henrique\\Desktop\\PL\\pl2023\TPC4\\'


def nada():
    with open(path + 'alunos.csv', 'r') as csvfile:

        reader = csv.DictReader(csvfile)
        header = next(reader)
        registros = []

        for row in reader:
            registros.append(dict(row))

    json_data = json.dumps(registros, indent=2)

    with open(path + 'alunos.json', 'w') as jsonfile:
        jsonfile.write(json_data)

def q1():

    with open(path + 'alunos2.csv', 'r') as csvfile:
        
        reader = csv.reader(csvfile)
        header = next(reader)
        registros = []

        for row in reader:
            registro = {}

            for i, campo in enumerate(header):
                if '{' in campo and '}' in campo:
                    n = int(campo.split('{')[1].split('}')[0])
                    valores = []

                    for j in range(i, i+n):
                        valores.append(row[j])

                    registro[campo.split('{')[0]] = valores
                else:
                    registro[campo] = row[i]

            registros.append(registro)

    json_data = json.dumps(registros, indent=2)

    with open(path + 'alunos2.json', 'w') as jsonfile:
        jsonfile.write(json_data)

def q2():
    
    with open(path + 'alunos3.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header_row = next(reader)
        header_dict = {}
        for field in header_row:
            match = re.match(r'(.+){(\d+)(,\d+)?}', field)
            if match:
                field_name = match.group(1)
                num_cols = int(match.group(2))
                header_dict[field_name] = num_cols
            else:
                header_dict[field] = 1

    with open(path + 'alunos3.csv', newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        json_list = []
        for row in reader:
            json_row = {}
            for field, num_cols in header_dict.items():
                if num_cols == 1:
                    json_row[field] = row.pop(0)
                else:
                    json_row[field] = row[:num_cols]
                    row = row[num_cols:]
            json_list.append(json_row)

    lalala = json.dumps(json_list, indent=2)
    with open(path + 'alunos3.json', 'w') as jsonfile:
        jsonfile.write(lalala)

def q3():
    
    with open(path + 'alunos4.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        def sum_notas(rows):
            notas = [int(nota) for nota in rows if nota]
            return sum(notas)

        json_data = []
        for row in csv_reader:
            json_row = {}
            for field, value in zip(header, row):
                if field.startswith('Notas{'):
                    continue
                elif field.endswith('::sum'):
                    continue
                else:
                    json_row[field] = value

            json_row['Notas_sum'] = sum_notas(row[3:])
            json_data.append(json_row)

    with open(path + 'alunos4.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2)


    with open(path + 'alunos5.csv') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)

        def sum_notas(rows):
            notas = [int(nota) for nota in rows if nota]
            return sum(notas)

        json_data = []
        for row in csv_reader:
            i = 0
            json_row = {}
            for field, value in zip(header, row):
                i += 1
                if field.startswith('Notas{'):
                    continue
                elif field.endswith('::media'):
                    continue
                else:
                    json_row[field] = value
                        

            json_row['Notas_media'] = round(sum_notas(row[3:])/i)
            json_data.append(json_row)

    with open(path + 'alunos5.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=2)


if __name__ == "__main__":
    q1()
    q2()
    q3()
