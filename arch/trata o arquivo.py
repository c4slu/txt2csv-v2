# Abrir o arquivo original com o modo de leitura

import os
import time
import pandas as pd


def divide():
    pasta = "Mailing Tratado/"
    arquivos = os.listdir(pasta)
    
    for arquivo in arquivos:
        arquivo_path = os.path.join(pasta, arquivo)
        if os.path.isfile(arquivo_path):
            os.remove(arquivo_path)



    path = "Mailing/"

    for filename in os.listdir(path):
        with open(os.path.join(path, filename), "r") as input_file:
            lines = input_file.readlines()
    # cria um dicionário para armazenar as linhas para cada valor da primeira coluna
        data = {}
        for line in lines:
            parts = line.strip().split()
            if parts[0] in data:
                data[parts[0]].append(line)
            else:
                data[parts[0]] = [line]

        # escreve as linhas para cada arquivo de saída
        for key in data:
            with open("Mailing Tratado/output_" + key + ".txt", "w") as output_file:
                for line in data[key]:
                    output_file.write(line)

def arch01():
  try:
    with open("Mailing Tratado\output_01.txt", "r") as in_file:
        # Criar um novo arquivo com as colunas separadas
        with open("Mailing Tratado\output_01.csv", "w") as out_file:
            out_file.write("TP_REGISTRO" + "|"
            + "CUST_ACCOUNT_ID" + "|" 
            + "CNPJ9_CPF" + "|" 
            + "TIPO_CNPJ" + "|" 
            + "RAZ_SOC" + "|" 
            + "FANTASIA" + "|" 
            + "DT_FUNDACAO_CLI" + "|" 
            + "FPD" + "|" 
            + "VALOR_TOTAL_ABERTO" + "|" 
            + "ESTRATEGIA" + "|" 
            + "CAMPO1" + "|" 
            + "CAMPO2" + "|" 
            + "CAMPO3" + "|" 
            + "CAMPO4" + "\n"
            )
            # Iterar sobre as linhas do arquivo original
            for line in in_file:
                # Remover o espaçamento em branco da linha
                line = line.strip()
                # Separar a linha em colunas
                TP_REGISTRO = line[:2].strip()
                CUST_ACCOUNT_ID = line[3:17].strip()
                CNPJ9_CPF = line[18:26].strip()
                TIPO_CNPJ = line[27:27].strip()
                RAZ_SOC = line[27:127].strip()
                FANTASIA = line[128:176].strip()
                DT_FUNDACAO_CLI = line[177:187].strip()
                FPD = line[188:188].strip()
                VALOR_TOTAL_ABERTO = line[189:206].strip()
                ESTRATÉGIA = line[207:216].strip()
                CAMPO1 = line[217:236].strip()
                CAMPO2 = line[237:257].strip()
                CAMPO3 = line[258:267].strip()
                CAMPO4 = line[268:277].strip()
                # Escrever as colunas no novo arquivo

                out_file.write(TP_REGISTRO + "|" +	CUST_ACCOUNT_ID + "|" +	CNPJ9_CPF + "|" +	TIPO_CNPJ + "|" +	RAZ_SOC + "|" +	FANTASIA + "|" +	DT_FUNDACAO_CLI + "|" +	FPD + "|" +	VALOR_TOTAL_ABERTO + "|" +	ESTRATÉGIA + "|" +	CAMPO1 + "|" +	CAMPO2 + "|" +	CAMPO3 + "|" + CAMPO4 + "|" + "\n")

    os.remove("Mailing Tratado\output_01.txt")
  except FileNotFoundError:
    print("Arquivo não existe")

def arch02():
  try:
    with open("Mailing Tratado\output_02.txt", "r") as in_file:
        # Criar um novo arquivo com as colunas separadas
        with open("Mailing Tratado\output_02.csv", "w") as out_file:
            out_file.write("TP_REGISTRO" + "|"
            + "CUST_ACCOUNT_ID" + "|" 
            + "CNPJ9_CPF" + "|" 
            + "TIPO_CNPJ" + "|" 
            + "FILIAL" + "|" 
            + "DIGITO" + "|" 
            + "LOGRADOURO" + "|" 
            + "NUMERO" + "|" 
            + "COMPLEMENTO" + "|" 
            + "BAIRRO" + "|" 
            + "CEP" + "|" 
            + "CIDADE" + "|" 
            + "UF" + "\n"
            )
            # Iterar sobre as linhas do arquivo original
            for line in in_file:
                # Remover o espaçamento em branco da linha
                
                # Separar a linha em colunas
                TP_REGISTRO = line[:2].strip()
                CUST_ACCOUNT_ID = line[3:17].strip()
                CNPJ9_CPF = line[18:26].strip()
                TIPO_CNPJ = line[26:27].strip()
                FILIAL = line[27:31].strip()
                DIGITO = line[31:33].strip()
                LOGRADOURO = line[33:134].strip()
                NUMERO = line[134:142].strip()
                COMPLEMENTO = line[142:172].strip()           
                #COMPLEMENTO = line[142:172].strip()
                BAIRRO = line[172:203].strip()
                CEP = line[203:211].strip()
                CIDADE = line[211:271].strip()
                UF = line[271:273].strip()

                # Escrever as colunas no novo arquivo

                out_file.write(TP_REGISTRO + "|" +	CUST_ACCOUNT_ID + "|" +	CNPJ9_CPF + "|" +	TIPO_CNPJ + "|" +	FILIAL + "|" +	DIGITO + "|" +	LOGRADOURO + "|" +	NUMERO + "|" +	COMPLEMENTO + "|" +	BAIRRO + "|" +	CEP + "|" +	CIDADE + "|" +	UF + "|" + "\n")
    os.remove("Mailing Tratado\output_02.txt")
  except FileNotFoundError:
      print("Arquivo não existe")


def arch03():
  try:
    with open("Mailing Tratado\output_03.txt", "r") as in_file:
        # Criar um novo arquivo com as colunas separadas
        with open("Mailing Tratado\output_03.csv", "w") as out_file:
            out_file.write("TP_REGISTRO" + "|"
            +"CUST_ACCOUNT_ID" + "|"
            +"CNPJ9_CPF" + "|"
            +"TIPO_CNPJ" + "|"
            +"TEL01" + "|"
            +"TEL02" + "|"
            +"TEL03" + "|"
            +"TEL04" + "|"
            +"TEL05" + "|"
            +"TEL06" + "|"
            +"TEL07" + "|"
            +"TEL08" + "|"
            +"TEL09" + "|"
            +"TEL10" + "\n"
            )
            # Iterar sobre as linhas do arquivo original
            for line in in_file:
                # Remover o espaçamento em branco da linha
                line = line.strip()
                # Separar a linha em colunas
                TP_REGISTRO = line[:2].strip()
                CUST_ACCOUNT_ID = line[3:17].strip()
                CNPJ9_CPF = line[18:26].strip()
                TIPO_CNPJ = line[26:27].strip()
                TEL01 = line[27:38].strip()
                TEL02 = line[38:49].strip()
                TEL03 = line[49:60].strip()
                TEL04 = line[60:71].strip()
                TEL05 = line[71:82].strip()
                TEL06 = line[82:93].strip()
                TEL07 = line[93:104].strip()
                TEL08 = line[104:115].strip()
                TEL09 = line[115:126].strip()
                TEL10 = line[126:137].strip()
                # Escrever as colunas no novo arquivo

                out_file.write(TP_REGISTRO + "|" +	CUST_ACCOUNT_ID + "|" +	CNPJ9_CPF + "|" +	TIPO_CNPJ + "|" +	TEL01 + "|" +	TEL02 + "|" +	TEL03 + "|" +	TEL04 + "|" +	TEL05 + "|" +	TEL06 + "|" +	TEL07 + "|" +	TEL08 + "|" +	TEL09 + "|" +	TEL10 + "|" +"\n")
    os.remove("Mailing Tratado\output_03.txt")
  except FileNotFoundError:
      print("Arquivo não existe")

def arch04():
    try:
      with open("Mailing Tratado\output_04.txt", "r") as in_file:
          # Criar um novo arquivo com as colunas separadas
          with open("Mailing Tratado\output_04.csv", "w") as out_file:
              out_file.write("TP_REGISTRO" + "|"
              +"CUST_ACCOUNT_ID" + "|"
              +"CNPJ9_CPF" + "|"
              +"TIPO_CNPJ" + "|"
              +"NOME_SOCIO" + "|"
              +"TEL_SOCIO" + "\n"
              )
              # Iterar sobre as linhas do arquivo original
              for line in in_file:
                  # Remover o espaçamento em branco da linha
                  line = line.strip()
                  # Separar a linha em colunas
                  TP_REGISTRO = line[:2].strip()
                  CUST_ACCOUNT_ID = line[3:17].strip()
                  CNPJ9_CPF = line[18:26].strip()
                  TIPO_CNPJ = line[27:27].strip()
                  NOME_SOCIO = line[27:97].strip()
                  TEL_SOCIO = line[97:108].strip()
                  # Escrever as colunas no novo arquivo

                  out_file.write(TP_REGISTRO + "|" +	CUST_ACCOUNT_ID + "|" +	CNPJ9_CPF + "|" +	TIPO_CNPJ + "|" + NOME_SOCIO + "|" + TEL_SOCIO + "|" + "\n")
      os.remove("Mailing Tratado\output_04.txt")
    except FileNotFoundError:
       print("Arquivo não existe")

def arch05():
  try:
    with open("Mailing Tratado\output_05.txt", "r") as in_file:
        # Criar um novo arquivo com as colunas separadas
        with open("Mailing Tratado\output_05.csv", "w") as out_file:

            out_file.write("TP_REGISTRO" + "|"
            +"CUST_ACCOUNT_ID" + "|"
            +"CNPJ9_CPF" + "|"
            +"TIPO_CNPJ" + "|"
            +"CUSTOMER_TRX_ID" + "|"
            +"PAYMENT_SCHEDULE_ID" + "|"
            +"NUMERO_PARCELA" + "|"
            +"TIPO_TRANSACAO" + "|"
            +"DT_NF" + "|"
            +"TRX_NUMBER" + "|"
            +"VENC_NFe" + "|"
            +"Nosso_Numero" + "|"
            +"PAYMENT_METHOD" + "|"
            +"VLR_ORIG_TITULO" + "|"
            +"VLR_ABRT_TITULO" + "|"
            +"DT_PGTO" + "|"
            +"COD_STATUS_TITULO" + "|"
            +"MULTA" + "|"
            +"JUROS" + "|"
            +"NUMERO_ACORDO_ESCR_COBR" + "|"
            +"PAYMENT_TERM" + "|"
            +"NOME_ESCRITORIO" + "\n"

            )
            # Iterar sobre as linhas do arquivo original
            for line in in_file:
                # Remover o espaçamento em branco da linha
                line = line.strip()
                # Separar a linha em colunas
                TP_REGISTRO = line[:2].strip()
                CUST_ACCOUNT_ID = line[3:17].strip()
                CNPJ9_CPF = line[18:26].strip()
                TIPO_CNPJ = line[27:27].strip()
                CUSTOMER_TRX_ID = line[27:43].strip()
                PAYMENT_SCHEDULE_ID = line[43:59].strip()
                NUMERO_PARCELA = line[59:64].strip()
                TIPO_TRANSACAO = line[64:65].strip()
                DT_NF = line[65:75].strip()
                TRX_NUMBER = line[75:93].strip()
                VENC_NFe = line[93:103].strip()
                Nosso_Numero = line[103:119].strip()
                PAYMENT_METHOD = line[119:169].strip()
                VLR_ORIG_TITULO = line[169:188].strip()
                VLR_ABRT_TITULO = line[188:207].strip()
                DT_PGTO = line[207:217].strip()
                COD_STATUS_TITULO = line[217:219].strip()
                MULTA = line[219:229].strip()
                JUROS = line[229:239].strip()
                NUMERO_ACORDO_ESCR_COBR = line[239:255].strip()
                PAYMENT_TERM = line[255:285].strip()
                NOME_ESCRITORIO = line[285:315].strip()
                RETENCAO_IMPOSTOS = line[315:330].strip()
                # Escrever as colunas no novo arquivo

                out_file.write(TP_REGISTRO + "|" +	CUST_ACCOUNT_ID + "|" +	CNPJ9_CPF + "|" +	TIPO_CNPJ + "|" +	CUSTOMER_TRX_ID + "|" +	PAYMENT_SCHEDULE_ID + "|" +	NUMERO_PARCELA + "|" +	TIPO_TRANSACAO + "|" +	DT_NF + "|" +	TRX_NUMBER + "|" +	VENC_NFe + "|" +	Nosso_Numero + "|" +	PAYMENT_METHOD + "|" +	VLR_ORIG_TITULO + "|" +	VLR_ABRT_TITULO + "|" +	DT_PGTO + "|" +	COD_STATUS_TITULO + "|" +	MULTA + "|" +	JUROS + "|" +	NUMERO_ACORDO_ESCR_COBR + "|" +	PAYMENT_TERM + "|" +	NOME_ESCRITORIO + "|" +	RETENCAO_IMPOSTOS + "|" + "\n")
    os.remove("Mailing Tratado\output_05.txt")
  except FileNotFoundError:
       print("Arquivo não existe")

def arch06():
  try:
    with open("Mailing Tratado\output_06.txt", "r") as in_file:
        # Criar um novo arquivo com as colunas separadas
        with open("Mailing Tratado\output_06.csv", "w") as out_file:
            out_file.write("TP_REGISTRO" + "|"
            +"CUST_ACCOUNT_ID" + "|"
            +"CNPJ9_CPF" + "|"
            +"TIPO_CNPJ" + "|"
            +"CUSTOMER_TRX_ID" + "|"
            +"FAMILIA_PROD" + "|"
            +"DESCR_PROD" + "|"
            +"QTDE_PROD" + "|"
            +"PRECO_TOT_PROD" + "\n"

            )
            # Iterar sobre as linhas do arquivo original
            for line in in_file:
                # Remover o espaçamento em branco da linha
                line = line.strip()
                # Separar a linha em colunas
                TP_REGISTRO = line[:2].strip()
                CUST_ACCOUNT_ID = line[3:17].strip()
                CNPJ9_CPF = line[18:26].strip()
                TIPO_CNPJ = line[27:27].strip()
                CUSTOMER_TRX_ID = line[27:43].strip()
                # LINE_NUMBER = line[43:46].strip()
                FAMILIA_PROD = line[45:85].strip()
                DESCR_PROD = line[85:136].strip()
                QTDE_PROD = line[136:146].strip()
                PRECO_TOT_PROD = line[146:165].strip()

                # Escrever as colunas no novo arquivo

                out_file.write(TP_REGISTRO + "|" +	CUST_ACCOUNT_ID + "|" +	CNPJ9_CPF + "|" +	TIPO_CNPJ + "|" +	CUSTOMER_TRX_ID + "|"+	FAMILIA_PROD + "|" +	DESCR_PROD + "|" +	QTDE_PROD + "|" +	PRECO_TOT_PROD + "|" + "\n")
    os.remove("Mailing Tratado\output_06.txt")
  except FileNotFoundError:
      print("Arquivo não existe")
def arch99():
  try:
    path = "Mailing Tratado/"

    for filename in os.listdir(path):
      if filename[0:9] == "output_99":
        with open(os.path.join(path, filename), "r") as in_file:
        #with open("Mailing Tratado\output_99.txt", "r") as in_file:
        # Criar um novo arquivo com as colunas separadas
          with open("Mailing Tratado\output_99.csv", "w") as out_file:
              out_file.write("TP_REGISTRO" + "|"
              +"DT_CRIACAO" + "|"
              +"QTD_EMPRESA" + "|"
              +"QTD_TITULO" + "|"
              +"QTD_LINHAS" + "|"
              +"VLR_TOTAL_ARQUIVO" + "\n"
              )
              # Iterar sobre as linhas do arquivo original
              for line in in_file:
                  # Remover o espaçamento em branco da linha
                  line = line.strip()
                  # Separar a linha em colunas
                  TP_REGISTRO = line[:2].strip()
                  DT_CRIACAO = line[2:10].strip()
                  QTD_EMPRESA = line[10:18].strip()
                  QTD_TITULO = line[18:26].strip()
                  QTD_LINHAS = line[26:34].strip()
                  VLR_TOTAL_ARQUIVO = line[34:53].strip()

                  # Escrever as colunas no novo arquivo
              
              out_file.write(TP_REGISTRO + "|" +	DT_CRIACAO + "|" +	QTD_EMPRESA + "|" +	QTD_TITULO + "|" +	QTD_LINHAS + "|" +	VLR_TOTAL_ARQUIVO + "|" + "\n")
              

    for filename in os.listdir(path):
      if filename[:9] == "output_99" and filename != "output_99.csv":
        os.remove(f"Mailing Tratado\{filename}")
      if filename[:9] == "output_00":
        os.remove(f"Mailing Tratado\{filename}")
  except FileNotFoundError:
    print("Arquivo não existe")



divide()
# dados = pd.read_csv("Mailing Tratado/output_01.csv", sep="|")
# dados['CUST_ACCOUNT_ID'] = dados['CUST_ACCOUNT_ID'].astype(float)
# dados = dados.to_csv("Mailing Tratado/output_01_2.csv")


print('👍 Arquivo dividido \n')
time.sleep(1)
arch01()
print('✨ Arquivo 1 Tratado')
time.sleep(.5)
arch02()
print('✨ Arquivo 2 Tratado')
time.sleep(.5)
arch03()
print('✨ Arquivo 3 Tratado')
time.sleep(.5)
arch04()
print('✨ Arquivo 4 Tratado')
time.sleep(.5)
arch05()
print('✨ Arquivo 5 Tratado')
time.sleep(.5)
arch06()
print('✨ Arquivo 6 Tratado')
time.sleep(.5)
arch99()
print('✨ Arquivo 99 Tratado')

