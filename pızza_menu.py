#Ömer Kuru Pizza Menu Projesi

import csv
import datetime
import time
#menu.txt oluşturma
with open("menu.txt", "w") as menu:
#Pizza Çeşitleri
    menu.write("1.Margarita\n")
    menu.write("2.Türk Pizza\n")
    menu.write("3.Sade Pizza\n")
    menu.write("4.Supreme\n")
    menu.write("5.Pepperoni\n")
    menu.write("6.Vejetaryan\n")
# Soslar
    menu.write("1.Zeytin\n")
    menu.write("2.Mantar\n")
    menu.write("3.Peynir\n")
    menu.write("4.Et\n")
    menu.write("5.Soğan\n")
    menu.write("6.Mısır\n")
    menu.write("7.Sarımsak\n")

#menü içi bilgiler
class Pizza:
    def __init__(self):
        self.description = "Pizza"
        self.cost = 0

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


class Margarita(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Özel sos,mozzarella"
        self.cost = 65


class Turkpizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Özel Sos, Mozzarella Peyniri, Pastırma, Küp Sucuk, Mantar, Yeşil Biber, Domates"
        self.cost = 80


class Sadepizza(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Mozzarella Peyniri"
        self.cost = 55


class Supreme(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Özel,Sos, Mozzarella Peyniri, Küp Sucuk, Pepperoni, Mantar, Yeşil Biber, Soğan"
        self.cost = 85


class Pepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Özel Sos, Mozzarella Peyniri, Pepperoni"
        self.cost = 70


class Vejetaryan(Pizza):
    def __init__(self):
        super().__init__()
        self.description = "Özel Sos, Kekik, Köz Biber, Mısır, Mozzarella Peyniri, Siyah Zeytin, Yeşil Biber, Domates"
        self.cost = 70

class Decorator(Pizza):
    def __init__(self, topping):
        super().__init__()
        self.topping = topping

    def get_cost(self):
        return self.topping.get_cost() + super().get_cost()

    def get_description(self):
        return self.topping.get_description() + " " + super().get_description()


class Zeytin(Decorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.description = "Siyah Zeytin"
        self.cost = 5


class Mantar(Decorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.description = "Mantar"
        self.cost = 5


class Peynir(Decorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.description = "Keçi Peyniri"
        self.cost = 7


class Et(Decorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.description = "Et Parçacıkları"
        self.cost = 9


class Soğan(Decorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.description = "Soğan"
        self.cost = 5


class Mısır(Decorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.description = "Mısır"
        self.cost = 3


class Sarımsak(Decorator):
    def __init__(self, topping):
        super().__init__(topping)
        self.description = "Sarımsak"
        self.cost = 5

def main():
    pizzalar = ["Margarita", "Türk Pizza", "Sade Pizza", "Supreme","Pepperoni","Vejetaryan"]
    soslar = ["Zeytin", "Mantar", "Peynir","Et","Soğan","Mısır","Sarımsak"]
    fiyatlar = {"Margarita": 65, "Türk Pizza": 80, "Sade Pizza": 55, "Supreme": 85,"Pepperoni":70,"Vejetaryan":70,
              "Zeytin": 5, "Mantar": 5, "Peynir": 7,"Et":9,"Soğan":5,"Mısır":3,"Sarımsak":5}

    print("Merhabalar Pizza Restoranımza Hoşgeldiniz")
    print("Aşağıdan Menümüze Ulaşabilirsiniz!")
    print("Pizzalarımız: ")
    for i, pizza in enumerate(pizzalar):
        print(f"{i + 1}. {pizza} - {fiyatlar[pizza]}TL")
    print("Soslarımız: ")
    for i, sos in enumerate(soslar):
        print(f"{i + 1}. {sos} - {fiyatlar[sos]}TL")

    pizza_sec = int(input("Lütfen Bir Pizza Seçiniz (1-6): "))
    sos_sec = int(input("Lütfen Bir Sos Seçiniz (1-7): "))
    pizza_fiyat = fiyatlar[pizzalar[pizza_sec - 1]]
    sos_fiyat = fiyatlar[soslar[sos_sec - 1]]
    toplam_fiyat = pizza_fiyat + sos_fiyat

    print("Sipariş fişiniz aşağıdadır:")
    print(f"- {pizzalar[pizza_sec - 1]} - {pizza_fiyat}TL")
    print(f"- {soslar[sos_sec - 1]} - {sos_fiyat}TL")
    print(f"Toplam Fiyat: {toplam_fiyat}TL")

    isim = input("Lütfen Adınızı Giriniz: ")
    id_num = input("Lütfen Kimlik Numarınızı Giriniz: ")
    card_num = input("Lütfen Kredi Kartı Numarınızı Giriniz: ")
    card_pass = input("Lütfen Kredi Kartı Şifrenizi Giriniz: ")
    print("Siparişiniz tamamlandı afiyet olsun")

    sip_dty = f"{pizzalar[pizza_sec - 1]} with {soslar[sos_sec - 1]} sos"
    sip_zmn = datetime.datetime.now()

    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([isim, id_num, card_num, card_pass, sip_dty, sip_zmn, toplam_fiyat])


if __name__ == "__main__":
    main()