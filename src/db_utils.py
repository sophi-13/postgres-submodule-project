def get_connection_params(database, user, password, host="localhost", port=5432):
    return {
        "dbname": database,
        "user": user,
        "password": password,
        "host": host,
        "port": port
    }