# # lê o arquivo de entrada e o divide em linhas
# import os

# def divide():
#     path = "Mailing/"

#     for filename in os.listdir(path):
#         with open(os.path.join(path, filename), "r") as input_file:
#             lines = input_file.readlines()
#     # cria um dicionário para armazenar as linhas para cada valor da primeira coluna
#         data = {}
#         for line in lines:
#             parts = line.strip().split()
#             if parts[0] in data:
#                 data[parts[0]].append(line)
#             else:
#                 data[parts[0]] = [line]

#         # escreve as linhas para cada arquivo de saída
#         for key in data:
#             with open("Mailing Tratado/output_" + key + ".txt", "w") as output_file:
#                 for line in data[key]:
#                     output_file.write(line)


