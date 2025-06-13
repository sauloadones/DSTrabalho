import pandas as pd
from src.extractTransform import requestApi

from src.load import salvarCsv

dadosCotacao = requestApi()

salvarCsv(dadosCotacao, "src/datasets/dolar.csv", ";",".")