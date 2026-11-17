import requests # Biblioteca 

def obter_dados_meteorologicos():

    url = "http://127.0.0.1:8000/v1/forecast" # ENDPOINT (Esse recurso disponibiliza as informações meteorológicas em formato JSON).


    parametros = { # Informações enviadas junto à URL para definir a localização e os dados que deverão ser retornados pela API.

        "latitude": -26.4851, # latitude da localização consultada.
        "longitude": -49.0713 # longitude da localização consultada.
    }



    resposta = requests.get( # Realiza a requisição HTTP.
        url, # Variável que guarda o ENDPOINT
        params=parametros, # Envia os parâmetros de consulta.
        timeout=10 # Estabelece um limite de espera pela resposta.
    )

    resposta.raise_for_status() # verifica se a resposta HTTP indica uma falha.

    dados = resposta.json()

    temperatura = dados["current"]["temperature_2m"]
    umidade = dados["current"]["relative_humidity_2m"]
    sensacao_termica = dados["current"]["apparent_temperature"]
    precipitacao = dados["current"]["precipitation"]
    vento = dados["current"]["wind_speed_10m"]
    horario = dados["current"]["time"]

    print("\n== Dados Metereológicos de Jaraguá do Sul ==\n")

    print(f"Temperatura atual de: {temperatura}°C")
    print(f"Umidade atual : {umidade}%")
    print(f"Sensação Térmica atual de: {sensacao_termica}°C")
    print(f"Precipitação atual de: {precipitacao}mm")
    print(f"Velocidade do Vento: {vento} km/h")
    print(f"Horário atual : {horario}\n")

obter_dados_meteorologicos()