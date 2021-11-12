import pandas as pd
import csv
import time
import json

with open("NOVO_AGRUPAMENTO.csv","r",encoding="utf-8") as f:
    reader = csv.reader(f,delimiter=";")
    print(reader)
    next(reader)
    data = {"CIDADES":[]}
    for row in reader:        
        # print(row[0])
        # time.sleep(1)
        data["CIDADES"].append({"CIDADE":row[0],"UF":row[1],"GRUPO_ANTIGO":row[2],"GRUPO_NOVO":row[3],"Oferta_foco":row[4]})
    #print(data)
    
with open("cidades.json","w", encoding="utf-8") as f:
    json.dump(data,f,indent=4)
