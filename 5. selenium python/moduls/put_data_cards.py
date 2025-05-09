from moduls.db_OLX import OLX_cars_db


def put_data_cards(cards):
    """Обрабатывает карточки и сохраняет их в базу данных"""
    for card in cards:
        try:
            title = card.get("title", "Нет названия")
            price = card.get("price", "Нет цены")
            # будет сохраняться в поле "link"
            link = card.get("url", "Нет ссылки")
            place = card.get("place", "Нет ссылки")
            date = card.get("date", "Нет ссылки")

            # print(f"Название: {title}")
            # print(f"Цена: {price}")
            # print(f"Ссылка: {link}")
            # print(f"Ссылка: {place}")
            # print(f"Ссылка: {date}")
            # print("-" * 40)

            OLX_cars_db.save_cards(title=title, price=price,
                                  link=link, place=place, date=date)

        except Exception as e:
            print(f"Ошибка при обработке данных: {e}")
