class Person:
    def __init__ (self, name, surname):
        self.full_name = f"{name} {surname}" # Propiedad pública
        self.__name = name # Propiedad privada

    def get_name (self):
        return self.__name

    def walk (self):
        print(f"{self.full_name} está caminando")


my_person = Person('Ale', 'Sutil')
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()