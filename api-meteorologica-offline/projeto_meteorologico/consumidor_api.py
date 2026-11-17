import requests

def obter_dados_meteorologicos():
    url =   "http://127.0.0.1:8000/v1/forecast"

    parametros = {
        "latitude": -26.4851,
        "longitude": -49.0713,
        }

    resposta = requests.get(url, params=parametros, timeout=15)
    resposta.raise_for_status()
    dados = resposta.json()

    condicoes_atuais = dados["current"]



    print(condicoes_atuais)
    return{
        "temperatura" : condicoes_atuais["temperature_2m"],
        "umidade_relativa" : condicoes_atuais["relative_humidity_2m"],
        "velocidade_vento" : condicoes_atuais["wind_speed_10m"],
        "precipitacao" : condicoes_atuais["precipitation"],
        "sensacao_termica" : condicoes_atuais["apparent_temperature"],
        "horario" : condicoes_atuais["time"]
    }