""" ООП - Объектно ориентированное программирование """

# hello_geeks = "Geeks" #Змеинный регистр

# HelloGeeks = "Geeks" #Верблюжий регистр 

# def car():
#     pass 

class Car: # Шаблон или чертеж
    def __init__(self, motor, wheel, body): # __init__ - это конструктор
        self.motor = motor  # self - ссылка на текущий объект
        self.wheel = wheel # атрибут класса
        self.body = body
        
        self.bak = 1
        self.is_start = False # Флажок
        
    def info(self): # Функция внутри класса превращяется в метод
        print(f"Мотор - {self.motor} Колесо - {self.wheel} Кузов - {self.body}")
        
    def start(self):
        if self.bak > 0:
            self.is_start =True
            print("Машина заведена")
        else:
            print("У машины нет топлива")
            
    def stop(self):
        self.is_start = False
        print("Машина заглушена")
        
    def drive(self, city):
        if self.is_start == True:
            print(f"Машина едет в {city}")
        else:
            print("Машина не заведена")
            
            
        
car = Car('V6', "R20", "Khan") #Экземпляр класса
car.info()
car.start() 
# car.stop()
car.drive("Дубай")


name = ("Asko", "Isko", "Sema")
list_exapmle = list(name)
list_exapmle.append("Aslan")
name = tuple(list_exapmle)
print(name)

""" Создать класс (Book).Передать параметры (avtor, book_name, year). Создать метод info. Вызвать переданный аргумент """