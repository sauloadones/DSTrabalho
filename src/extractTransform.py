import requests
import pandas as pd

def requestApi() -> pd.DataFrame:

    url_usd = (
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        "CotacaoDolarPeriodo(dataInicial='01-01-2023',dataFinalCotacao='12-31-2025')"
        "?$top=10000&$format=json"
    )
    url_eur = (
        "https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/"
        "CotacaoMoedaPeriodo(moeda='EUR',dataInicial='01-01-2023',dataFinalCotacao='12-31-2025')"
        "?$top=10000&$format=json"
    )

    
    df_usd = pd.DataFrame(requests.get(url_usd).json()['value'])
    df_eur = pd.DataFrame(requests.get(url_eur).json()['value'])



    
    df_usd['tipoBoletim'] = 'Fechamento'

    
    df_usd = df_usd.rename(columns={
        'cotacaoCompra': 'cotacaoCompra_USD',
        'cotacaoVenda': 'cotacaoVenda_USD'
    })
    df_eur = df_eur.rename(columns={
        'cotacaoCompra': 'cotacaoCompra_EUR',
        'cotacaoVenda': 'cotacaoVenda_EUR',
        'paridadeCompra': 'paridadeCompra_USDEUR',
        'paridadeVenda': 'paridadeVenda_USDEUR'
    })

   
    df_merged = pd.merge(
        df_usd,
        df_eur,
        on=['dataHoraCotacao', 'tipoBoletim'],
        how='inner'
    )

   
    df = df_merged[[
        'dataHoraCotacao', 'tipoBoletim',
        'cotacaoCompra_USD', 'cotacaoVenda_USD',
        'cotacaoCompra_EUR', 'cotacaoVenda_EUR',
        'paridadeCompra_USDEUR', 'paridadeVenda_USDEUR'
    ]]

    return df
