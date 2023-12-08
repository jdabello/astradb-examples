from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json

# Connect to Cassandra
cluster = Cluster(['127.0.0.1'])  # replace with your Cassandra cluster's contact points
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")