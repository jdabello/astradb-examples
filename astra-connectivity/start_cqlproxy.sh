source .env
docker run -p 9042:9042 \
  datastax/cql-proxy:v0.1.4 \
  --astra-token $ASTRA_DB_TOKEN  --astra-database-id $ASTRA_DB_DATABASE_ID