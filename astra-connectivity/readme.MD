# Astra Connectivity

This example shows 3 different ways to connect to Astra.
1. [CQL Proxy](https://github.com/datastax/cql-proxy): A client-side proxy/sidecar that listens on a local address and securely forwards your application's CQL traffic. This lets you connect existing Cassandra applications to [Astra DB](https://www.datastax.com/products/datastax-astra) without changing the application code.
2. Connect with a Secure Connect Bundle (SCB): This is a compressed file containing the necessary security credentials and certificates for connecting your applications to your Astra DB database. It provides a secure and standardized way to establish mutually authenticated TLS connections between your application and the Astra DB service. You can download it from the connect tab within the Astra DB Console. [More here](https://docs.datastax.com/en/astra-serverless/docs/connect/connecting.html)
3. Connect without a Secure Conenct Bundle (SCB): The SCB is the only way to connect to Astra using a driver connection. There are alternative ways to connect to Astra such as the [Rest API](https://docs.datastax.com/en/astra-serverless/docs/_attachments/restv2.html), the [Document API](https://docs.datastax.com/en/astra-serverless/docs/_attachments/docv2.html), etc. This example still uses a **driver connection**, but leverages the [DevOps API](https://docs.datastax.com/en/astra-serverless/docs/_attachments/devopsv2.html#tag/Database-Operations/operation/generateSecureBundleURL) to automate the process of downloading the SCB.

Follow the steps before to try each one of these 3 examples:
## Prerequisits
1. Follow [these steps](https://docs.datastax.com/en/astra-serverless/docs/connect/drivers/connect-python.html#_working_with_secure_connect_bundle) to download the SCB.
2. Update the environment variables in the `.env.example` file, and rename it as `.env`.
## Connect via CQL Proxy
1. Execute the next commands to give execution permissions to `start_cqlproxy.sh`, and execute it.

    ```bash
    chmod +x start_cqlproxy.sh
    ./start_cqlproxy.sh
    ```
2. Execute the following commands from a new terminal to connect to cassandra.

    ```bash
    python connect_database_with_cqlproxy.py
    ```
## Connect with a Secure Connect Bundle (SCB)
1. Execute the following command from the terminal to connect to cassandra.

    ```bash
    python connect_database_with_scb.py
    ```
## Connect without a Secure Conenct Bundle (SCB)
1. Execute the following command from the terminal to connect to cassandra.

    ```bash
    python connect_database_without_scb.py
    ```