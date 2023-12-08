from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
import json
from dotenv import dotenv_values

config = dotenv_values('.env')
cloud_config= {
  'secure_connect_bundle': config["SCB_PATH"]
}

CLIENT_ID = config["ASTRA_DB_CLIENT_ID"]
CLIENT_SECRET = config["ASTRA_DB_CLIENT_SECRET"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
session = cluster.connect()

row = session.execute("select release_version from system.local").one()
if row:
  print(row[0])
else:
  print("An error occurred.")