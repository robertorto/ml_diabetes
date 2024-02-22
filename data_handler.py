import pandas as pd
import numpy as np
import json


# como o nome informa, este arquivo serve para dar acesso e manipular os dados do nosso dataset.

def load_data():
    dados = pd.read_csv('./data/diabetes.csv')
    # dados = pd.read_csv('C:\\Users\\Roberto\\ml_deploy_aula\\ml_diabetes\\data\\diabetes.csv')

    # nosso modelo descartou a informação SkinThickness por ela não ajudar na previsão, então vamos descartá-la também
    dados = dados.drop(['SkinThickness'], axis=1)
    return dados


# retorna todos os dados já armazenados das predições realizadas e validadas pelo usuário
# TODO: verificar se o arquivo existe antes de abrir
def get_all_predictions():
    data = None
    with open('predictions.json', 'r') as f:
        data = json.load(f)
        
    return data

# salva as predições em um arquivo JSON
# TODO: verificar se já não está salvo no arquivo antes de salvar de novo
def save_prediction(paciente):
    # lê todos as predições
    data = get_all_predictions()
    # adiciona a nova predição nos dados já armazenados
    data.append(paciente)
    # salva todas as predições no arquivo json
    with open('predictions.json', 'w') as f:
        json.dump(data, f)