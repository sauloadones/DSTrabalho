import pandas as pd
from src.extractTransform import requestApi

from src.load import salvarCsv

dadosBcb = requestApi()

salvarCsv(dadosBcb, "src/datasets/saldosMensais.csv", ";",".")