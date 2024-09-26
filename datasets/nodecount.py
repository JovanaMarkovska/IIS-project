
import pandas as pd
import networkx as nx
import matplotlib.pylab as plt
from timeframe import TimeFrame
from datetime import datetime
train_sessions = pd.read_csv(r"..\datasets\train_sessions_dressipi.csv")
# TODO adjust number of sessions
#train_sessions_copy = train_sessions.iloc[0:500000,:]
train_sessions_copy = train_sessions.copy()

train_sessions_copy.drop(train_sessions_copy.filter(regex="Unnamed"),axis=1, inplace=True)
print(train_sessions_copy)
n = len(pd.unique(train_sessions_copy['item_id']))
print(n)
print(len(pd.unique(train_sessions_copy['session_id'])))
train_sessions_copy.to_csv("train_sessions_dressipi_less_nodes.csv")

