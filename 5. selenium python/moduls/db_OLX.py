import sqlite3

DB_NAME = "./moduls/OLX_cars_db.db"


class OLX_cars_db():
    def __init__(self, name_DB, title, link, price, place_date, cards):
        self.name_DB = name_DB
        self.title = title
        self.link = link
        self.price = price
        self.place_date = place_date
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
                place_date TEXT
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

    # def create_new_string(name_DB):
    #     with sqlite3.connect(name_DB) as sqlite_conn:
    #         sqlite_request = """INSERT INTO OLX_cards VALUES(?, ?, ?, ?);"""
    #         sqlite_conn.execute(
    #             sqlite_request, (251, "Python course", 100, 30))
    #         sqlite_conn.commit()

    # def create_new_strings(name_DB, cards):
    #     with sqlite3.connect(name_DB) as sqlite_conn:
    #         sqlite_request = "INSERT INTO OLX_cards VALUES(?, ?, ?, ?)"
    #         for card in cards:
    #             sqlite_conn.execute(sqlite_request, card)
    #         sqlite_conn.commit()

    def create_new_strings(name_DB, cards):
        try:
            with sqlite3.connect(name_DB) as sqlite_conn:
                sqlite_request = "INSERT INTO OLX_cards (title, link, price, place_date) VALUES (?, ?, ?, ?)"
                cursor = sqlite_conn.cursor()
                for card in cards:
                    cursor.execute(
                        sqlite_request, (card['title'], card['link'], card['price'], card['place_date']))
                    sqlite_conn.commit()
        except sqlite3.Error as e:
            print("Ошибка базы данных:", e)

    def read_DB(name_DB):
        with sqlite3.connect(name_DB) as sqlite_conn:
            # sql_request = "SELECT * FROM courses"
            sql_request = "SELECT * FROM courses WHERE reviews_qty>=50"
            sql_cursor = sqlite_conn.execute(sql_request)
            # for record in sql_cursor:
            #     print(record)
            # print(record[1])
            records = sql_cursor.fetchall()
            print(records)

    courses = [
        (351, "JavaScript course", 415, 100),
        (614, "C++ course", 161, 10),
        (721, "Java full course", 100, 35)
    ]

# create_db(DB_NAME)
# create_new_table_olx_cards(name_DB)
# create_new_table_olx_card(name_DB)
# create_new_string(DB_NAME)
# create_new_strings(DB_NAME, courses)

# OLX_cars_db.read_DB(DB_NAME)
