import csv

import pandas as pd
import networkx as nx
import matplotlib.pylab as plt
from timeframe import TimeFrame
from datetime import datetime
train_sessions = pd.read_csv(r"..\dressipi_recsys2022_dataset\train_sessions.csv")
train_purchases = pd.read_csv(r"..\dressipi_recsys2022_dataset\train_purchases.csv")
item_features = pd.read_csv(r"..\dressipi_recsys2022_dataset\item_features.csv")

#dictionary of sessions
#training_sessions_df = train_sessions.copy()
#training_sessions_df = training_sessions_df.sort_values(by=["session_id","date"])
#training_sessions_df = training_sessions_df.groupby('session_id')['item_id'].apply(list).reset_index(name='session_sequences')
#training_sessions_df['session_purchase'] = train_purchases['item_id']

train_sessions
train_sessions = train_sessions.sort_values(by=["session_id","date"],ignore_index=True)
# new data frame with split value columns
new = train_sessions["date"].str.split(" ", n=1, expand=True)
train_sessions["eventdate"] = new[0]
#train_sessions["timeframe"] = train_sessions["date"]
dates = train_sessions["date"]
session_ids = train_sessions["session_id"]
timeframes = []
session_id = train_sessions["session_id"][0]
tf=1
for ind in range(0,len(train_sessions.index)-1):
    current_session_id = session_ids[ind]
    next_session_id = session_ids[ind+1]
    #if current_session_id == session_id:
    if current_session_id == next_session_id:
            timestamp1 = train_sessions['date'][ind]
            timestamp2 = train_sessions['date'][ind + 1]
            tf = TimeFrame(datetime.strptime(timestamp1[:19], '%Y-%m-%d %H:%M:%S'),
                           datetime.strptime(timestamp2[:19], '%Y-%m-%d %H:%M:%S'))
            timeframes.append(int(tf.duration * 1000))
            print(int(tf.duration * 1000))

    elif current_session_id != next_session_id:
            timeframes.append(int(tf.duration * 1000))
            #session_id = next_session_id
            print(int(tf.duration * 1000))

    #else: session_id = next_session_id

timeframes.append(int(tf.duration * 1000))

print(train_sessions.shape[0])
print(f'len %d',len(timeframes))
print("done")
# Dropping columns
#train_sessions.drop(columns=train_sessions.columns[0], inplace=True)

train_sessions['timeframe'] = timeframes

train_sessions.to_csv("train_sessions_dressipi.csv")
