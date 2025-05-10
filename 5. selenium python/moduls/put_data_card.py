from moduls.db_OLX import OLX_cars_db

def put_data_card(cards):
    """Обрабатывает карточки и сохраняет их в базу данных"""
    for card in cards:
        try:
            title = card.get("title", "Нет названия")
            price = card.get("price", "Нет цены")
            # будет сохраняться в поле "link"
            user = card.get("user", "Нет ссылки")
            description = card.get("description", "Нет ссылки")
            olx_cards_id = card.get("olx_cards_id", "Нет ссылки")

            OLX_cars_db.save_card(title=title, price=price,
                                  user=user, description=description, olx_cards_id = olx_cards_id)

        except Exception as e:
            print(f"Ошибка при обработке данных: {e}")