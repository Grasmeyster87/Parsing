import asyncio
from concurrent.futures import ThreadPoolExecutor
from moduls.getpage import get_cards_sync
from moduls.put_data_cards import put_data_cards
from moduls.db_OLX import OLX_cars_db, DB_NAME

# Подготовка базы данных
OLX_cars_db.create_db(DB_NAME)
OLX_cars_db.create_new_table_olx_cards(DB_NAME)
OLX_cars_db.create_new_table_olx_card(DB_NAME)

number_max = 5  # количество страниц которое нужно скачать где число подставляется в ссылку https://www.olx.ua/uk/transport/?page={page_number} в page_number от 0 до number_max
memory = 0  # память для асинхронной работы чтобы паралельно не грузить  одинаковые страницы

def gen_page_number(number_max):
    global memory
    if memory < number_max:
        memory += 1
        return memory
    return None

async def get_info(page_number, user_id, loop, executor):
    data = await loop.run_in_executor(executor, get_cards_sync, page_number, user_id)
    if data:
        put_data_cards(data)

async def main(number_max):
    loop = asyncio.get_running_loop()
    executor = ThreadPoolExecutor(max_workers=2)

    tasks = []
    for i in range(number_max):
        page = gen_page_number(number_max)
        if page is not None:
            tasks.append(get_info(page, i + 1, loop, executor))

    await asyncio.gather(*tasks)
    executor.shutdown()

    OLX_cars_db.create_index(DB_NAME)
    OLX_cars_db.remove_duplicates_olx_cards(DB_NAME)
    OLX_cars_db.remove_duplicates_olx_card(DB_NAME)

if __name__ == '__main__':
    asyncio.run(main(number_max))
