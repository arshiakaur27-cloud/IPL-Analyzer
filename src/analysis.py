print("Hello Arshia, project started")
import pandas as pd
import matplotlib.pyplot as plt
print("Libraries installed successfully")

import pandas as pd

df = pd.read_csv("data/deliveries.csv")

print(df.head())
print(df.columns)
df.info()

# Total runs scored by each player-top 10
runs=df.groupby("batter")["batsman_runs"].sum()
top_players=runs.sort_values(ascending=False).head(10)
print(top_players)
#balls faced
balls=df.groupby('batter').size()
#strike rate
strike_rate=(runs/balls)*100
#Combining into one table
player_stats=pd.DataFrame({'runs':runs,'balls':balls,'strike_rate':strike_rate})
print(player_stats.sort_values(by='runs',ascending=False).head(10))

#filter players who faced at least 100 balls
filtered_players=player_stats[player_stats['balls']>=100]
print(filtered_players.sort_values(by='runs',ascending=False).head(10))
# Top 10 players by strike rate (filtered)
top_sr_players = filtered_players.sort_values(by='strike_rate', ascending=False).head(10)
print(top_sr_players)

import matplotlib.pyplot as plt
# Plot top strike rate players
colors = ['red', 'blue', 'green', 'purple', 'orange', 'teal', 'pink', 'yellow', 'cyan', 'grey']
top_sr_players['strike_rate'].plot(kind='bar', color=colors)

plt.title('Top 10 Players by Strike Rate (Min 100 balls)')
plt.xlabel('Player')
plt.ylabel('Strike rate')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("output/top_players.png")
plt.show()

#compare two players
player1="V Kohli"
player2='RG Sharma'
comparison=player_stats.loc[[player1,player2]]
print(comparison)

comparison['strike_rate'].plot(kind='bar',color=['red','blue'])
plt.title('Strike Rate Comparison')
plt.ylabel('Strike Rate')

plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("output/Strike Rate comparison.png")
plt.show()
filtered_players.reset_index().to_csv('player_stats.csv',index=False)

top_runs=player_stats.sort_values(by='runs',ascending=False).head(10)
plt.figure(figsize=(10,5))
plt.bar(top_runs.index, top_runs['runs'])
plt.xticks(rotation=45)
plt.xlabel('Players')
plt.ylabel('Runs')

plt.tight_layout()
plt.savefig('output/top_run_scorers.png')
plt.show()
