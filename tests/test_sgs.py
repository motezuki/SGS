import pandas as pd

from SGS.sgs import get_serie

def test_get_serie_valid_dates():
    serie_code = 1  # Example series code
    start_date = '2023-01-01'
    end_date = '2023-01-10'
   
    df = get_serie(serie_code, start_date, end_date)
    
    assert not df.empty
    assert 'data' in df.columns
    assert 'valor' in df.columns
    assert all(df['data'] >= pd.to_datetime(start_date))
    assert all(df['data'] <= pd.to_datetime(end_date))
