products = {
    "001": {"name": "Батончик", "price": 70},
    "002": {"name": "Вода", "price": 45},
    "003": {"name": "Газировка", "price": 64},
    "004": {"name": "Булочка", "price": 33},
}

def display_products():
    print("| ID  | ProductName | Цена |")
    print("|-----|-------------|------|")
    for product_id, product_info in products.items():
        print(f"| {product_id} | {product_info['name']:<11} | {product_info['price']:>4} |")

def vending_machine():
    display_products()
    
    product_id = input("Введите ID товара: ").strip()
    if product_id == "ОТМЕНА":
        print("Выход из программы.")
        return
    
    if product_id not in products:
        print("Товара с таким ID не существует.")
        return
    
    product_price = products[product_id]["price"]
    print(f"Внесите {product_price} тугриков")
    
    total_inserted = 0
    
    while total_inserted < product_price:
        user_input = input("Внесите купюру (10/50/100/500): ").strip()
        
        if user_input == "ОТМЕНА":
            print("Выход из программы.")
            return
        
        try:
            bill = int(user_input)
            if bill not in [10, 50, 100, 500]:
                print("Внесена фальшивая купюра")
                continue
        except ValueError:
            print("Некорректный ввод. Введите номинал купюры.")
            continue
        
        total_inserted += bill
        
        if total_inserted >= product_price:
            change = total_inserted - product_price
            print(f"Ваша сдача: {change} тугриков")
            return
        else:
            remaining = product_price - total_inserted
            print(f"Осталось внести {remaining} тугриков")


vending_machine()
