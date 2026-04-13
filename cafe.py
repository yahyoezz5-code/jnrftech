while True:
    print("---MENU---")
    print("1 - вход")
    print("2 - показать")
    print("3 - заказ")
    print("enough - заказы из меню")
    print("0 - выход")

    choice = int(input("enter your number: "))

    if choice == 1:
        name = input("enter your name: ")
        print(f"добро пожаловать в кафе {name}")

    elif choice == 2:
        ls = ["1 - хот-дог", "2 - шаурма","3 - бургер","4 - пицца","5 - газированный", "6 - cofee", "7 - картошка-фри"]
        print(f"ваш меню {ls}")

    elif choice == 3:
        order = []
        while True:

            zakaz = input("ваш заказ :) ")
            if zakaz == "1":
                print("хот-дог")
                order.append("хот-дог")

            elif zakaz == "2":
                print("шаурма")
                order.append("шаурма")

            elif zakaz == "3":
                print("бургер")
                order.append("бургер")

            elif zakaz == "4" :
                print("пицца")
                order.append("пицца")

            elif zakaz == "5":
                print("газированный")
                order.append("газированный")
            
            elif zakaz == "6":
                print("coffe")
                order.append("cofee")

            elif zakaz == "7":
                print("картошка-фри")
                order.append("картошка-фри")

            elif zakaz == "enough":
                ordering = input(f"господин {name} этот список ваш {order} ? | Yes/No |----> ?   ")
                if ordering == "Yes":
                    print("приятного опетита :)")
                    break
                if ordering == "No":
                    print("ваш заказ отменён !")
                    break
            
    elif choice == 0:
        print("выход")
        break
    else :
        print("неверный выбор")
        break