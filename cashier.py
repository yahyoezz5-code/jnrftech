inventory = []  
total_sales_sum = 10000
total_sold_count = 10000
settings = ("Мой Супермаркет", "сом") 


def show_settings():
    
    name, currency = settings
    print(f"--- Настройки ---")
    print(f"Магазин: {name}. Валюта: {currency}")
    
    categories = set()
    for item in inventory:
        categories.add(item["category"])
    
    print(f"Уникальные категории товаров: {categories}")

def add_product():
    
    print("--- Добавление товара ---")
    name = input("Введите название: ")
    price = float(input("Введите цену: "))
    count = int(input("Введите количество: "))
    category = input("Введите категорию: ")
    
    in_stock = count > 0
    
    product = {
        "name": name,
        "price": price,
        "count": count,
        "category": category,
        "available": in_stock
    }
     
    
    inventory.append(product)
    print("Товар успешно добавлен!")

def show_inventory():
    
    if not inventory:
        print("Магазин пуст.")
        return

    print("--- Список товаров ---")
    for index, item in enumerate(inventory, 1):
        print(f"{index}. {item['name']} | Цена: {item['price']} | Кол-во: {item['count']} | Кат: {item['category']}")

def sell_product():
    
    global total_sales_sum, total_sold_count
    show_inventory()
    
    if not inventory:
        return

    choice = int(input("Введите номер товара для продажи: "))
    index = choice - 1

    if 0 <= index < len(inventory):
        item = inventory[index]
        
        if item["available"] and item["count"] > 0:
            qty = int(input(f"Сколько единиц '{item['name']}' продать? "))
            
            if qty <= item["count"]:
                item["count"] -= qty
                total_sales_sum += qty * item["price"]
                total_sold_count += qty
                

                if item["count"] == 0:
                    item["available"] = False
                
                print(f"Продано! Сумма: {qty * item['price']}")
            else:
                print("Ошибка: На складе нет столько товара.")
        else:
            print("Товара нет в наличии.")
    else:
        print("Неверный номер.")

def delete_product():
    """Функция удаления товара"""
    show_inventory()
    if not inventory:
        return

    choice = int(input("Введите номер товара для удаления: "))
    index = choice - 1

    if 0 <= index < len(inventory):
        inventory.pop(index)
        print("Товар удален.")
    else:
        print("Ошибка: такого номера нет.")

def show_stats():
    """Функция статистики"""
    in_stock = 0
    out_of_stock = 0
    
    for item in inventory:
        if item["available"]:
            in_stock += 1
        else:
            out_of_stock += 1

    print("--- Статистика магазина ---")
    print(f"Всего позиций в базе: {len(inventory)}")
    print(f"Товаров в наличии: {in_stock}")
    print(f"Товаров раскуплено: {out_of_stock}")
    print(f"Всего продано единиц: {total_sold_count}")
    print(f"Общая выручка: {total_sales_sum} {settings[1]}")

def main():
    """Основная логика программы"""
    print("*** Программа: Консольная касса Магазина ***")
    kasir_name = input("Введите имя кассира: ")
    print(f"Добро пожаловать в систему, {kasir_name}!\n")

    while True:
        print("Добро пожаловать в наш Магазин")
        print("1. Добавить товар")
        print("2. Показать все товары")
        print("3. Продать товар")
        print("4. Удалить товар")
        print("5. Статистика")
        print("6. Настройки")
        print("7. Выход")
        choice = input("Выберите действие (1-7): ")

        if choice == "1":
            add_product()
        elif choice == "2":
            show_inventory()
        elif choice == "3":
            sell_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            show_stats()
        elif choice == "6":
            show_settings()
        elif choice == "7":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")