# -*- coding: utf-8 -*-
"""Imersão Python-Alura-Aula 02.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WgOPVTT-ws1RLZLg3NOwhq_9l1_FxbKU
"""

import pandas as pd

df_principal = pd.read_excel("/content/Alura Imersão Python - Tabela de ações-executado-260324.xlsx", sheet_name="Principal")
df_principal

df_total_acoes = pd.read_excel("/content/Alura Imersão Python - Tabela de ações-executado-260324.xlsx", sheet_name="Total_de_acoes")
df_total_acoes

df_ticker = pd.read_excel("/content/Alura Imersão Python - Tabela de ações-executado-260324.xlsx", sheet_name="Ticker")
df_ticker

df_chatgpt = pd.read_excel("/content/Alura Imersão Python - Tabela de ações-executado-260324.xlsx", sheet_name="ChatGPT")
df_chatgpt