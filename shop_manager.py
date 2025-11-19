class Prodact:
    def __init__(self, title, price, year):
        self.title = title
        self.price = price
        self.year = year
        self.type = ''


p1 = Prodact("olma", 9000, 2025)


class Shop:

    def __init__(self, title, phone):
        self.title = title
        self.phone = phone
        self.baza = []

    def add_water(self):
        title = input("title")
        price = int(input("price"))
        year = int(input("year"))
        p1 = Prodact(title, price, year)
        p1.type = "water"
        self.baza.append(p1)

    def add_food(self):
        title = input("title")
        price = int(input("price"))
        year = int(input("year"))
        p1 = Prodact(title, price, year)
        p1.type = "food"
        self.baza.append(p1)

    def view_all(self):
        tur = input("qaysi turdagi mahsulotni ko'rmoqchisiz: ")

        sanash = 0  # bu true/false emas, qo'ldan chiqqan mahsulotlar soni

        for item in self.baza:
            if item.type == tur:
                print(f"title:{item.title} price:{item.price} year:{item.year} type:{item.type}")
                sanash += 1

        if sanash == 0:
            print("bunday mahsulot topilmadi")

    def update(self):
        nom = input("Qaysi mahsulotni tahrirlaysiz? nomini kiriting: ")

        for item in self.baza:
            if item.title == nom:
                print(" eski qiymatlar:", item.title, item.price, item.year)

                item.title = input("yangi title: ")
                item.price = int(input("yangi price: "))
                item.year = int(input("yangi year: "))
                print("Mahsulot yangilandi!")
                return

        print("Bunday mahsulot topilmadi.")

    def delete(self):
        nom = input("Qaysi mahsulotni o'chirasiz? nomini kiriting: ")

        for item in self.baza:
            if item.title == nom:
                self.baza.remove(item)
                print("Mahsulot o'chirildi!")
                return

        print("Bunday mahsulot yo‘q.")


shop1 = Shop('shop1', "12345")


def shop_manager(shop: Shop):
    while True:
        kod = input("1.add water \n 2.add food \n 3.view all \n  4.update \n 5.delete \n 6.break:")
        if kod == "1":
            shop.add_water()
        elif kod == "2":
            shop.add_food()
        elif kod == "3":
            shop.view_all()
        elif kod == "4":
            shop.update()
        elif kod == "5":
            shop.delete()

        else:
            break


shop_manager(shop1)