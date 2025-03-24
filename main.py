import requests
import json 
# ------------------------------------------

infoCEP = "CEP INFO:\n"
erro = "Error, no requests possible"
info = "Inquery CEP Software - v1.0"

# ------------------------------------------

CEP = input("What CEP? \n> ")
api_CEP_info = f"https://viacep.com.br/ws/{CEP}/json/"
collect = requests.get(api_CEP_info)

# ------------------------------------------

    
def  save_to_json(data, filename =f"{CEP}_info.json"):
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4)
        
# ------------------------------------------

if collect.status_code == 200:
    getinfos = collect.json()
    print(infoCEP)
    print(getinfos)
    save_to_json(getinfos)
else:
    print(erro)
