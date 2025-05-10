import asyncio
from concurrent.futures import ThreadPoolExecutor

from moduls.put_data_cards import put_data_cards
from moduls.db_OLX import OLX_cars_db, DB_NAME

from moduls.CONSTANTS import number_max, memory
from moduls.put_data_cards import put_data_cards

from moduls.get_cards_sync import get_cards_sync_2, create_driver
from moduls.CONSTANTS import user_id, num_tabs, number_max, memory_cards


# Подготовка базы данных
OLX_cars_db.create_db(DB_NAME)
OLX_cars_db.create_new_table_olx_cards(DB_NAME)
OLX_cars_db.create_new_table_olx_card(DB_NAME)

async def get_info(loop, executor):
    data = await loop.run_in_executor(executor, get_cards_sync_2, number_max, num_tabs, memory_cards)
    if data:
        put_data_cards(data)

async def main(number_max):

    loop = asyncio.get_running_loop()
    executor = ThreadPoolExecutor(max_workers=2)

    tasks = []
    tasks.append(get_info(loop, executor))

    await asyncio.gather(*tasks)
    executor.shutdown()

    OLX_cars_db.create_index(DB_NAME)                 # создаем индекс в базе данных для ускорения доступа
    OLX_cars_db.remove_duplicates_olx_cards(DB_NAME)  # удаляем дубликаты стаблицы olx_cards
    OLX_cars_db.remove_duplicates_olx_card(DB_NAME)   # удаляем дубликаты стаблицы olx_card
    OLX_cars_db.delete_DB_OLX_null_cards(DB_NAME)     # удаляем дубликаты, оставляя только первую запись из таблицы OLX_cards

if __name__ == '__main__':                            # блок кода будет выполняться только при непосредственном запуске файла, а не при его импорте в другой скрипт.
    asyncio.run(main(number_max))
