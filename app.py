import json
import requests
continuar = True
while continuar:
    cep = input("Digite o CEP que deseja consultar: ")

    cep = cep.replace(".", "")
    cep = cep.replace("-", "")

    req = requests.get(f"https://viacep.com.br/ws/{cep}/json/")

    try:
        response = json.loads(req.content)

        print("."*30)
        print("Informações de seu endereço:")
        print("CEP: ", cep)
        print("Logradouro: ", response["logradouro"])
        print("Complemento: ", response["complemento"])
        print("Bairro: ", response["bairro"])
        print("Cidade: ", response["localidade"])
        print("UF: ", response["uf"])
        print("IBGE: ", response["ibge"])
        print("GIA: ", response["gia"])
        print("DDD: ", response["ddd"])
        print("SIAFI: ", response["siafi"])
        print("."*30)
    except:
        print("CEP Não encontrado")
    
    continuarStr = input("Deseja continuar? (S/N) ").lower()
    if "s" not in continuarStr:
        continuar = False

        

