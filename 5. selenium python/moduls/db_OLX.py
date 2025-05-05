import sqlite3

DB_NAME = "./moduls/OLX_cars_db.db"


class OLX_cars_db():
    def __init__(self, name_DB, title, link, price, place, date, cards):
        self.name_DB = name_DB
        self.title = title
        self.link = link
        self.price = price
        self.place = place
        self.date = date
        self.cards = cards

    def create_db(name_DB):
        with sqlite3.connect(name_DB) as sqlite_conn:
            print(sqlite_conn)
            print(sqlite3.version)

    def create_new_table_olx_cards(name_DB):
        with sqlite3.connect(name_DB) as sqlite_conn:
            cursor = sqlite_conn.cursor()

            # Проверяем, существует ли таблица
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='OLX_cards';")
            if cursor.fetchone() is None:
                sqlite_request = """CREATE TABLE OLX_cards (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                link TEXT,
                price TEXT,
                place TEXT,
                date TEXT
                );"""
                sqlite_conn.execute(sqlite_request)
                print("Таблица 'OLX_cards' создана.")
            else:
                print("Таблица 'OLX_cards' уже существует.")

    def create_new_table_olx_card(name_DB):
        with sqlite3.connect(name_DB) as sqlite_conn:
            cursor = sqlite_conn.cursor()

            # Проверяем, существует ли таблица
            cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name='OLX_card';")
            if cursor.fetchone() is None:
                sqlite_request = """CREATE TABLE OLX_card (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                description TEXT,
                olx_cards_id INTEGER,
                FOREIGN KEY (olx_cards_id) REFERENCES OLX_cards(id)
                );"""
                sqlite_conn.execute(sqlite_request)
                print("Таблица 'OLX_card' создана.")
            else:
                print("Таблица 'OLX_card' уже существует.")

    def create_new_strings(name_DB, cards):
        try:
            with sqlite3.connect(name_DB) as sqlite_conn:
                sqlite_request = "INSERT INTO OLX_cards (title, link, price, place, date) VALUES (?, ?, ?, ?, ?)"
                cursor = sqlite_conn.cursor()
                for card in cards:
                    cursor.execute(
                        sqlite_request, (card['title'], card['link'], card['price'], card['place'], card['date']))
                    sqlite_conn.commit()
        except sqlite3.Error as e:
            print("Ошибка базы данных:", e)

    def read_DB_OLX_cards(name_DB):
        try:
            with sqlite3.connect(name_DB) as sqlite_conn:
                # sql_request = "SELECT * FROM courses"
                sql_request = "SELECT * FROM OLX_cards"
                sql_cursor = sqlite_conn.execute(sql_request)
                # for record in sql_cursor:
                #     print(record)
                # print(record[1])
                records = sql_cursor.fetchall()
                # print(records)
                num = 1
                for card in records:
                    print(num, card, '\n')
                    num += 1
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")

    def create_index(name_DB):
        with sqlite3.connect(name_DB) as sqlite_conn:
            cursor = sqlite_conn.cursor()

            # Проверяем, существует ли индекс
            cursor.execute("PRAGMA index_list('OLX_cards')")
            indexes = [index[1] for index in cursor.fetchall()]

            if "idx_username" not in indexes:
                cursor.execute(
                    "CREATE INDEX idx_username ON OLX_cards (title)")
                sqlite_conn.commit()
                print("Индекс 'idx_username' создан.")
            else:
                print("Индекс 'idx_username' уже существует.")

            cursor.close()

    def remove_duplicates_olx_cards(name_DB):
        with sqlite3.connect(name_DB) as sqlite_conn:
            cursor = sqlite_conn.cursor()

            # Удаляем дубликаты, оставляя только первую запись
            cursor.execute("""
                DELETE FROM OLX_cards WHERE id NOT IN (
                    SELECT MIN(id) FROM OLX_cards GROUP BY title, link, price, place, date
                )
            """)

            sqlite_conn.commit()
            print("Дубликаты из 'OLX_cards' удалены.")

    def remove_duplicates_olx_card(name_DB):
        with sqlite3.connect(name_DB) as sqlite_conn:
            cursor = sqlite_conn.cursor()

            # Удаляем дубликаты, оставляя только первую запись
            cursor.execute("""
                DELETE FROM OLX_card WHERE id NOT IN (
                    SELECT MIN(id) FROM OLX_card GROUP BY title, description, olx_cards_id
                )
            """)

            sqlite_conn.commit()
            print("Дубликаты из 'OLX_card' удалены.")


# create_db(DB_NAME)
# create_new_table_olx_cards(name_DB)
# create_new_table_olx_card(name_DB)
# create_new_string(DB_NAME)
# create_new_strings(DB_NAME, courses)

# OLX_cars_db.read_DB(DB_NAME)
# SELECT name FROM sqlite_master WHERE type = 'index' AND tbl_name = 'OLX_cards'; # создан ли индекс
