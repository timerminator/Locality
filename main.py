# Создаем родительский класс: Населенный пункт
class Locality:
    # Конструктор класса
    def __init__(self, title='Locality', population=50000):
        # Определеяем приватные переменные
        self.__title = title
        self.__population = population

    # getter для названия населенного пункта
    def get_title(self):
        return self.__title

    # getter для количетсва человек населенного пункта
    def get_population(self):
        return self.__population

    # setter для названия населенного пункта
    def set_title(self, title):
        self.__title = title

    # setter для количетсва человек населенного пункта
    def set_population(self, population):
        self.__population = population

    # преопределение стандартного метода __str__ для вывода в консоль информации об экземпляре класса
    def __str__(self):
        return f'Населенный пункт: {self.get_title()}. Население: {self.get_population()} человек'


# Класс Город наследуется от класса Населенный пункт
class City(Locality):

    # Переопределяем конструктор класса
    def __init__(self, title='City', population=500000):
        # Вызывает конструктор родительского класса
        super().__init__(title, population)

    # Переопределяем setter населения
    def set_population(self, population):
        if population in range(100, 100000000):
            self.__population = population
        else:
            print("Недопустимое население")

    # преопределение стандартного метода __str__ для вывода в консоль информации об экземпляре класса
    def __str__(self):
        return f'Город: {self.get_title()}. Население: {self.get_population()} человек'


# Класс Столица наследуется от класса Город. Может быть только в единственном экземпляре
class Capital(City):
    # Переменная __instance__ будет содержать единственный объект для создания экземпляра
    __instance__ = None

    # Конструктор проверяет наличие существующего класса или выдает ошибку
    def __init__(self, title='Москва', population=10000000):
        if Capital.__instance__ is None:
            Capital.__instance__ = self
            super().__init__(title, population)
        else:
            raise Exception('Вы не можете создать 2 экземпляр Capital.')

    # Статический метод get_instance() при извлечении объекта проверяет, есть ли существующий экземпляр.
    # Если нет, то создает и возвращает
    @staticmethod
    def get_instance():
        if not Capital.__instance__:
            Capital()
        return Capital.__instance__


# Абстрактный класс для создания населенных пунктов
class LocalityCreator(object):
    def create_locality(self, type_):
        raise NotImplementedError()


# Класс для создания населенных пунктов, наследуемый от абстрактного класса LocalityCreator
class MyLocalityCreator(LocalityCreator):
    # Статический метод create_locality создает Населенный пункт, Город или Столицу в зависимости от параметра
    @staticmethod
    def create_locality(type_=''):
        if type_ == 'city':
            return City()
        elif type_ == 'capital':
            return Capital.get_instance()
        else:
            return Locality()


# Точка входа
if __name__ == '__main__':
    locality = Locality('Благовещенск', 40000)
    print(locality)
    city = City('Стерлитамак')
    print(city)
    capital = Capital.get_instance()
    print(capital)
    city2 = MyLocalityCreator.create_locality('city')
    print(city2)
    locality2 = MyLocalityCreator.create_locality()
    print(locality2)
