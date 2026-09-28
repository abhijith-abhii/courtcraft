import pandas as pd,pytest
from core import summarize,analyze

def test_reconciliation():
 d=analyze({'minimum_minutes':0});assert sum(x['minutes'] for x in d['rows'])==d['metrics']['Minutes']
 assert all(x['lower90']<x['shrunk_points_per36']<x['upper90'] for x in d['rows'])
def test_empty_filter():assert analyze({'minimum_minutes':999999})['rows']==[]
def test_bad_metric():
 with pytest.raises(ValueError):analyze({'metric':'made_up'})
def test_zero_minutes_rejected():
 df=pd.DataFrame([dict(player='A',game=1,minutes=0,points=1,fga=1,fta=0,turnovers=0,rebounds=0,assists=0)])
 with pytest.raises(ValueError):summarize(df)
