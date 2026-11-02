from src.db_utils import get_connection_params


def test_default_connection_params():
    params = get_connection_params(
        "test_db",
        "postgres",
        "12345"
    )

    assert params["dbname"] == "test_db"
    assert params["user"] == "postgres"
    assert params["host"] == "localhost"
    assert params["port"] == 5432


def test_custom_connection_params():
    params = get_connection_params(
        "my_db",
        "admin",
        "password",
        host="127.0.0.1",
        port=5433
    )

    assert params["host"] == "127.0.0.1"
    assert params["port"] == 5433


def test_password_is_saved():
    params = get_connection_params(
        "test_db",
        "postgres",
        "secret"
    )

    assert params["password"] == "secret"