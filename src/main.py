import psycopg


def main():
    try:
        # Подключение к PostgreSQL
        with psycopg.connect(
            host="127.0.0.1",
            port=5432,
            dbname="postgres",
            user="postgres",
            password="12345",
            connect_timeout=5
        ) as conn:

            print("Успешное подключение к PostgreSQL!")

            # Создание курсора для выполнения SQL-запросов
            with conn.cursor() as cur:
                cur.execute("SELECT version();")

                version = cur.fetchone()

                print("\nИнформация о сервере PostgreSQL:")
                print(version[0])

    except psycopg.OperationalError as error:
        print("Не удалось подключиться к PostgreSQL:")
        print(error)

    except psycopg.Error as error:
        print("Ошибка при работе с PostgreSQL:")
        print(error)


if __name__ == "__main__":
    main()