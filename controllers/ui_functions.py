import requests
import json

def consulta_cnpj(cnpj: str):
    url = f"https://receitaws.com.br/v1/cnpj/{cnpj}"

    querystring = {"token":"XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX","cnpj":"06990590000123","plugin":"RF"}

    response = requests.request("GET", url, params=querystring)

    result = json.loads(response.text )

    if __name__ == "__main__":
        print(result['cnpj'])
        print(result['nome'])
        print(result['logradouro'])
        print(result['numero'])
        print(result['bairro'])
        print(result['municipio'])
        print(result['uf'])
        print(result['cep'])
        print(result['telefone'])
        print(result['email'])

        return result['nome'], result['logradouro'], result['numero'], result['bairro'], result['municipio'], result['uf'], result['cep'], result['telefone'], result['email']


if __name__ == "__main__":
    consulta_cnpj('11815149000145')