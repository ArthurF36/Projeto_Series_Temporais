import os
from datetime import datetime

def salvar_resultados(df):
    pasta = r"/workspaces/Projeto_Series_Temporais/Data"

    os.makedirs(pasta, exist_ok = True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    caminho = os.path.join(pasta, f"dataset_Minimum_Temperatures_{timestamp}.xlsx")
    df.to_excel(caminho, index = False, engine = "openpyxl")
    
    print(f"\nResultados salvos em: {caminho}")