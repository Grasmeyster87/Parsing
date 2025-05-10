from moduls.put_data_cards import put_data_cards
from moduls.put_data_card import put_data_card
from moduls.db_OLX import OLX_cars_db, DB_NAME

from moduls.CONSTANTS import number_max, memory, limit
from moduls.put_data_cards import put_data_cards

from moduls.get_cards_sync import get_cards_sync_2, create_driver
from moduls.get_card_sync import get_card_sync
from moduls.CONSTANTS import user_id, num_tabs, number_max, memory_cards

# Подготовка базы данных
OLX_cars_db.create_db(DB_NAME)
OLX_cars_db.create_new_table_olx_cards(DB_NAME)
OLX_cars_db.create_new_table_olx_card(DB_NAME)

def main(number_max):
    driver = create_driver()  # создаем драйвер один раз
    # data_cards =  get_cards_sync_2(driver, number_max, num_tabs, memory_cards)
    # if data_cards:
    #     put_data_cards(data_cards)

    page_arr = OLX_cars_db.get_DB_OLX_link_cards(DB_NAME, limit)
    data_card =  get_card_sync(driver, page_arr, num_tabs)
    if data_card:
            put_data_card(data_card)

    OLX_cars_db.create_index(DB_NAME)                 # создаем индекс в базе данных для ускорения доступа
    OLX_cars_db.remove_duplicates_olx_cards(DB_NAME)  # удаляем дубликаты стаблицы olx_cards
    OLX_cars_db.remove_duplicates_olx_card(DB_NAME)   # удаляем дубликаты стаблицы olx_card
    OLX_cars_db.delete_DB_OLX_null_cards(DB_NAME)     # удаляем дубликаты, оставляя только первую запись из таблицы OLX_cards

if __name__ == '__main__':                            # блок кода будет выполняться только при непосредственном запуске файла, а не при его импорте в другой скрипт.
    main(number_max)
