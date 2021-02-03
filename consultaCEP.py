# Gabriel F. Habermann -- Programa para consultar CEP digitado -- 04/02/2021

import requests
from endereco import Enderecos
import json

def MakeRequestByCEP(cep):
    
    request = requests.get('http://viacep.com.br/ws/{}/json/'.format(cep))

    if ('erro' in request.text):
        print('CEP não encontrado na consulta')
        return -1

    enderecoVec = json.loads(request.text)

    enderecoResult = Enderecos(
        logradouro = enderecoVec["logradouro"],
        cep = enderecoVec["cep"],
        complemento = enderecoVec["complemento"],
        bairro = enderecoVec["bairro"],
        localidade = enderecoVec["localidade"],
        uf = enderecoVec["uf"],
        ibge = enderecoVec["ibge"],
        siafi = enderecoVec["siafi"],
        ddd = enderecoVec["ddd"],
        gia = enderecoVec["gia"])

    return enderecoResult

def printEndereco(endereco):

    print('\nLogradouro: {}'.format(endereco.logradouro))
    print('Complemento: {}'.format(endereco.complemento))
    print('Bairro: {}'.format(endereco.bairro))
    print('Cidade: {}'.format(endereco.localidade))
    print('UF: {}'.format(endereco.uf))
    print('CEP: {}'.format(endereco.cep))
    print('DDD: {}'.format(endereco.ddd))
    print('IGBE: {}'.format(endereco.ibge))
    print('GIA: {}'.format(endereco.gia))
    print('SIAFI: {}\n'.format(endereco.siafi)) 

def main():

    while 1:

        cep = input('Digite o CEP para receber seus dados: (Digite 0 para sair do programa)\n')

        if cep == '0':
            exit()

        if (len(cep) != 8):
            print('Tamanho do CEP inválido\n')
            continue

        try:
            int(cep)
        except:
            print('CEP inválido\n')
            continue

        result = MakeRequestByCEP(cep)

        if result== -1:
            print("O CEP não foi encontrado na consulta")
            main()
        break

    printEndereco(result)

    while 1 :
        again = input('Deseja realizar uma nova consulta? (s/n)\n')

        if again == 's':
            main()
        elif again == 'n':
            exit()
        else:
            print('Entrada inválida')
            continue

if __name__ == '__main__':
    print('Consulta CEP')
    main()