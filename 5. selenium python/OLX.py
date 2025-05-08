import asyncio
from concurrent.futures import ThreadPoolExecutor
from moduls.getpage import get_cards_sync
from moduls.get_data_cards import get_data_cards
from moduls.db_OLX import OLX_cars_db, DB_NAME

# Подготовка базы данных
OLX_cars_db.create_db(DB_NAME)
OLX_cars_db.create_new_table_olx_cards(DB_NAME)
OLX_cars_db.create_new_table_olx_card(DB_NAME)

number_max = 10
memory = 0

def gen_page_number(number_max):
    global memory
    if memory < number_max:
        memory += 1
        return memory
    return None

async def get_info(page_number, user_id, loop, executor):
    data = await loop.run_in_executor(executor, get_cards_sync, page_number, user_id)
    if data:
        get_data_cards(data)

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
