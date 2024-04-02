import sqlalchemy as data
import pandas as pd
engine = data.create_engine("mysql+mysqlconnector://root:mysqlroot@localhost/project")
#mysql://username:password@hostname/database
conn=engine.connect()

metadata=data.MetaData()
restraunts=data.Table('restraunt1',metadata, autoload_with=engine)

# print(repr(metadata.tables['restraunt1']))

#print(restraunts.columns.keys())

query=restraunts.select().where(restraunts.columns.sno== 20)

#to show the sql command for the above
#print(query)

exe=conn.execute(query)

result=exe.fetchall()

# print(result)

data1=pd.DataFrame(result)
# data1.columns=result[0].keys()
data1

import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="whitegrid")

f, ax = plt.subplots(figsize=(15, 6))
plt.xticks(rotation=90)
sns.set_color_codes("pastel")
sns.barplot(x="HomeTeam", y="FTHG", data=data1,
            label="Home Team Goals", color="b")

sns.barplot(x="HomeTeam", y="FTAG", data=data1,
            label="Away Team Goals", color="r")
ax.legend(ncol=2, loc="upper left", frameon=True)
ax.set(ylabel="", xlabel="")
sns.despine(left=True, bottom=True)