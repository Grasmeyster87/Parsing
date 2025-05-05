def output_result(cards):
    """ Вывести значения всех карточек"""
    print('Выводим значение карточек:')
    num = 1
    for res in cards:
        print(num, ' ', res['title'], '  ', res['link'], '\n',
            res['price'], '  ', res['place_date'], '\n\n')
        num += 1