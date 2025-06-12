import requests
import pandas as pd
from urllib.parse import quote


def requestApi() -> pd.DataFrame:

    url = (
    "https://olinda.bcb.gov.br/olinda/servico/Saldos_BCB/versao/v1/odata/"
    "Saldos_Mensais_BCB(Data_base=@Data_base,Data_fim=@Data_fim)"
    )

    params = {
        "@Data_base": "'2024-01-01'",
        "@Data_fim": "'2024-12-31'",
        "$format": "json",
        "$top": 100
    }

    response = requests.get(url, params=params)


    # === Verificação e tratamento dos dados ===
    if response.status_code == 200:
        dados = response.json()["value"]
       
        return pd.DataFrame(dados)
    else:
        print(f"Erro na requisição: {response.status_code}")