from pathlib import Path
import pandas as pd,numpy as np
from scipy.stats import gamma
ROOT=Path(__file__).parent
def summarize(df,minimum=100):
 cols=['minutes','points','fga','fta','turnovers','rebounds','assists']
 if df.empty or df[['player','game']].duplicated().any():raise ValueError('Empty data or duplicate player/game')
 if df[cols].isna().any().any() or (df[cols]<0).any().any() or (df.minutes<=0).any():raise ValueError('Invalid box score')
 g=df.groupby('player')[cols].sum();g['games']=df.groupby('player').size()
 rate=df.points.sum()/df.minutes.sum();prior_minutes=120
 g['points_per36']=36*g.points/g.minutes
 g['shrunk_points_per36']=36*(g.points+rate*prior_minutes)/(g.minutes+prior_minutes)
 g['lower90']=36*gamma.ppf(.05,g.points+rate*prior_minutes,scale=1/(g.minutes+prior_minutes))
 g['upper90']=36*gamma.ppf(.95,g.points+rate*prior_minutes,scale=1/(g.minutes+prior_minutes))
 g['true_shooting']=g.points/(2*(g.fga+.44*g.fta)).replace(0,np.nan)
 g['assist_to_turnover']=g.assists/g.turnovers.replace(0,np.nan)
 return g[g.minutes>=minimum].reset_index()
def analyze(p):
 minimum=float(p.get('minimum_minutes',100));metric=p.get('metric','shrunk_points_per36')
 if not np.isfinite(minimum) or minimum<0:raise ValueError('Minutes must be nonnegative')
 if metric not in ['shrunk_points_per36','points_per36','true_shooting']:raise ValueError('Unsupported metric')
 df=pd.read_csv(ROOT/'data/boxscores.csv');g=summarize(df,minimum).sort_values(metric,ascending=False);rows=g.round(3).replace({np.nan:None}).to_dict('records')
 return dict(metrics={'Players shown':len(g),'Games in sample':len(df),'Minutes':int(df.minutes.sum())},bars=[dict(label=x['player'],value=x[metric]) for x in rows[:12]],rows=rows,notice='Poisson/Gamma intervals assume a constant scoring rate; they do not model opponent strength or game dependence. True shooting uses the conventional 0.44 free-throw approximation.',details={'prior_minutes':120,'prior':'empirical global points per minute','ranking':metric,'data':'synthetic'})
