import datetime
import pandas as pd

def get_serie(serie_code, start_date, end_date) -> pd.DataFrame:
    start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d').strftime("%d/%m/%Y")
    end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d').strftime("%d/%m/%Y")

    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{serie_code}/dados?formato=json&dataInicial={start_date}&dataFinal={end_date}"

    time_serie = pd.read_json(url)
    if time_serie.empty:
        return pd.DataFrame(columns=['data', 'valor'])
    
    time_serie['data'] = pd.to_datetime(time_serie['data'], format="%d/%m/%Y")
    time_serie['valor'] = pd.to_numeric(time_serie['valor'], errors='coerce')
    
    return time_serie