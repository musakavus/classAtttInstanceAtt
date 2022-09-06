class Personel:
    count: int = 0  # class attribute. --> Bütün nesneler için değeri ortaktırç
    adet: int = 0

    def __init__(self, name) -> None:
        self.__name = name  # instance attributes --> Nesneden nesneye değeri değişir.
        self.increase()

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.name = value

    def increase(self):
        self.count = self.count + 1  # instance method
        return self.count


p1 = Personel('Yavuz')
print(p1.count)  # Output |  1

p2 = Personel('Murat')
print(p2.count)  # Output | 1

p3 = Personel('Sabri')  # Output | 1
print(p3.count)

print(Personel.count)  # Nesne eklemeden de class attributesi bu şekilde değiştirilebilir.
# --> Dikkat edilidği üzere 3 kez nesne oluşturulmasına rağmen her defasında count sayısı 1 verilmiştir.
# --> Çünkü self.count = self.count + 1 olarak oluşturulmuş yani self olarak. (Yani instance olarak sadece nesneye ait)


# instance method ve attributeler her nesne oluşumunda yeni değerler alır.
# Ama class instance nesne oluşturulurken sabittir.
# selfin olduğu her yer instance method yada attributedir.
# constructorda da self olduğu için bir instance methoddur.
# instance attribute yada metodlara ulaşmak için muhakkak nesne oluşturulmalıdır.
