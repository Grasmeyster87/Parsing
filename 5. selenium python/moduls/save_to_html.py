
def save_to_html(cards):
    # Сохранить в файл все карточки
    with open('file.html', 'wt', encoding='utf-8') as file:
        for card in cards:
            file.write(card.get_attribute('outerHTML') + '\n')