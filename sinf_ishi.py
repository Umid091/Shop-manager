
class Shop:

    def __int__(self, title, phone):
        self.title = title
        self.phone = phone

    # def add_water(self):
    #     title=input("title")
    #     price=int(input("price"))
    #     year=int(input("year"))
    #     p1=Prodact(title,price, year)
    #     p1.type="water"
    #     self.baza.append(p1)
    #
    # def add_food(self):
    #     title = input("title")
    #     price = int(input("price"))
    #     year = int(input("year"))
    #     p1 = Prodact(title, price, year)
    #     p1.type="food"
    #     self.baza.append(p1)
    #
    # def view_all(self):
    #     for item in self.baza:
    #         print(f"title:{item.tite} price:{item.price} type:{item.type}")

s1 = Shop()

print(s1.phone)


