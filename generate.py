import csv,random
from pathlib import Path
r=random.Random(81);root=Path(__file__).parent;(root/'data').mkdir(exist_ok=True)
with (root/'data/boxscores.csv').open('w') as f:
 w=csv.writer(f);w.writerow(['player','game','minutes','points','fga','fta','turnovers','rebounds','assists'])
 for player in range(24):
  ability=r.uniform(.35,.8)
  for g in range(r.randint(8,35)):
   minutes=r.randint(7,37);fga=max(1,round(minutes*r.uniform(.2,.5)));fta=r.randint(0,8);points=round(fga*ability*2+fta*.72)
   w.writerow([f'Player {player+1:02}',g,minutes,points,fga,fta,r.randint(0,5),r.randint(0,12),r.randint(0,10)])
