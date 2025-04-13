from bs4 import BeautifulSoup
from savers import save_html, create_csv
# from model import Product

def page_hadler(page, res, max_item, list_product, count_items, counter):
    soup = BeautifulSoup(res.text, "lxml")
    # print(soup)
    #save_html(page, soup)

    products = soup.find_all("div", class_="short-item")
    count = 0
    for product in products:
        count += 1
    # print(count)
    
    for product in products:
        
        # if count_items >= max_item:
        #         break

        # count_items += 1
        
        name = product.select_one("h3.short-title a i").next_sibling.strip()

        link_card = 'https://radiodetali.com.ua' +product.select_one("h3.short-title a")["href"]

        # Знаходимо всі елементи <td>, які знаходяться в рядку з текстом "Ціна (грн.):"
        price_row = product.find('th', string='Ціна (грн.):').find_parent('tr')
        price_cells = price_row.find_all('td')

        # Отримуємо ціну з першої колонки цін
        if price_cells:
            price_td = price_cells[0]
        # Знаходимо весь текст в елементі <td>, включаючи текст поза <span>
            full_price_text = price_td.get_text(strip=True)
            price_sht = full_price_text.split('.')[0] + '.00 грн'
            # print(price_sht)
        else:
            print("Елемент з ціною не знайдено.")

        # print(name, ' ', link_card, ' ', price_sht)

        if (price_sht != True):
            price = "По запросу"
        list_product.append(
            {'counter': counter,
            'name': name,
            'link_card':link_card,                
            'price_sht':price_sht})
        counter += 1
        # print(list_product)

    return list_product, counter