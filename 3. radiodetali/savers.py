import csv

def save_html(page, content):
    with open(f"./savehtml/page - {page}.html", mode='w', encoding="utf-8") as file:
        file.write(str(content))
        print(f"Данные сохранены в файл {page}.html")


            
def create_csv():
    with open(f"./glavsnab.csv", mode='w', newline="") as file:
        writer = csv.writer(file)
        writer.writerow([])