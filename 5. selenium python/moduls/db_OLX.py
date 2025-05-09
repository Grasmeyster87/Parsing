import sqlite3

DB_NAME = "./moduls/OLX_cars_db.db"
DB_NAME_MODULS = "./OLX_cars_db.db"


class OLX_cars_db():
    def __init__(self, name_DB, title, link, price, place, date, cards, user, description, olx_cards_id):
        self.name_DB = name_DB
        self.title = title
        self.link = link
        self.price = price
        self.place = place
        self.date = date
        self.cards = cards
        self.user = user
        self.description = description
        self.olx_cards_id = olx_cards_id

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
                sqlite_request = """CREATE TABLE "OLX_cards" (
                                    "id"	INTEGER,
                                    "title"	TEXT NOT NULL,
                                    "link"	TEXT,
                                    "price"	TEXT,
                                    "place"	TEXT,
                                    "date"	TEXT,
                                    PRIMARY KEY("id")
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
                sqlite_request = """CREATE TABLE "OLX_card" (
                                    "id"	INTEGER,
                                    "title"	TEXT,
                                    "price"	TEXT,
                                    "user"	TEXT,
                                    "description"	TEXT,
                                    "olx_cards_id"	INTEGER NOT NULL,
                                    PRIMARY KEY("id"),
                                    FOREIGN KEY("olx_cards_id") REFERENCES "OLX_cards"("id"));
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

    @staticmethod
    def save_cards(title, price, link, place, date):
        conn = sqlite3.connect(DB_NAME)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO OLX_cards (title, price, link, place, date)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, price, link, place, date))  # place и date пока пустые
        conn.commit()
        conn.close()

    @staticmethod
    def save_card(title, price, user, description, olx_cards_id):
        conn = sqlite3.connect(DB_NAME_MODULS)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO OLX_card (title, price, user, description, olx_cards_id)
            VALUES (?, ?, ?, ?, ?)
        ''', (title, price, user, description, olx_cards_id))  # place и date пока пустые
        conn.commit()
        conn.close()

    def get_DB_OLX_link_cards(name_DB):
        try:
            with sqlite3.connect(DB_NAME_MODULS) as sqlite_conn:
                sql_request = """SELECT OLX_cards.id, OLX_cards.link
                             FROM OLX_cards
                             LEFT JOIN OLX_card ON OLX_cards.id = OLX_card.olx_cards_id
                             WHERE OLX_card.olx_cards_id IS NULL
                             LIMIT 50;"""

                sql_cursor = sqlite_conn.execute(sql_request)
                records = sql_cursor.fetchall()
                num = 1
                for card in records:
                    print(num, card, '\n')
                    num += 1
                return records
        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")
   
    def delete_DB_OLX_null_cards(name_DB):
        try:
            with sqlite3.connect(name_DB) as sqlite_conn:
                cursor = sqlite_conn.cursor()

                # Учитываем:
                # - SQL NULL
                # - строку 'NULL'
                # - пустые строки или пробелы
                cursor.execute("""
                    SELECT id, olx_cards_id FROM OLX_card
                    WHERE (title IS NULL OR TRIM(title) = '' OR title = 'NULL')
                    AND (price IS NULL OR TRIM(price) = '' OR price = 'NULL')
                    AND (user IS NULL OR TRIM(user) = '' OR user = 'NULL')
                    AND (description IS NULL OR TRIM(description) = '' OR description = 'NULL')
                """)
                rows = cursor.fetchall()
                olx_cards_ids = [row[1] for row in rows]

                print(f"Найдено записей OLX_card с пустыми/NULL полями: {len(rows)}")
                print("olx_cards_id для удаления:", olx_cards_ids)

                if olx_cards_ids:
                    # Удалить такие записи из OLX_card
                    cursor.execute("""
                        DELETE FROM OLX_card
                        WHERE (title IS NULL OR TRIM(title) = '' OR title = 'NULL')
                        AND (price IS NULL OR TRIM(price) = '' OR price = 'NULL')
                        AND (user IS NULL OR TRIM(user) = '' OR user = 'NULL')
                        AND (description IS NULL OR TRIM(description) = '' OR description = 'NULL')
                    """)

                    # Удалить связанные OLX_cards
                    query = f"""
                        DELETE FROM OLX_cards
                        WHERE id IN ({','.join('?' for _ in olx_cards_ids)})
                    """
                    cursor.execute(query, olx_cards_ids)

                    sqlite_conn.commit()
                    print("Удаление завершено.")
                else:
                    print("Нет записей для удаления.")

        except sqlite3.Error as e:
            print(f"Ошибка базы данных: {e}")



# create_db(DB_NAME)
# create_new_table_olx_cards(name_DB)
# create_new_table_olx_card(name_DB)
# create_new_string(DB_NAME)
# create_new_strings(DB_NAME, courses)

# OLX_cars_db.read_DB(DB_NAME)
# SELECT name FROM sqlite_master WHERE type = 'index' AND tbl_name = 'OLX_cards'; # создан ли индекс


# OLX_cars_db.get_DB_OLX_link_cards(DB_NAME_MODULS)
OLX_cars_db.delete_DB_OLX_null_cards(DB_NAME_MODULS)
