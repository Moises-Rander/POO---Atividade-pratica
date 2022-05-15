class Person:

    def __init__(self, name, age, cpf):
        self.__name = name
        self.__age = age
        self.__cpf = cpf

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @property
    def cpf(self):
        return self.__cpf
