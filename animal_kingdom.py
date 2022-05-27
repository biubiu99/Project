from typing import Any


# print(object) -> print() looks for __repr__() in the object -> __repr__() will give a string, and then print() prints the string

class Animal:
    """
    :param species: Name of animal species

    """

    def __init__(self, species: str, age: int, mass: float, sex: str):
        self.species: str = species
        self.age: int = age
        self.mass: float = mass
        self.sex: str = sex

    def __repr__(self) -> str:
        return f'{self.species} of age {self.age} with mass {self.mass}'

    def __lt__(self, other: Any):
        if isinstance(other, Animal):
            return self.mass < other.mass
        else:
            raise TypeError('Not allowed')

    def __gt__(self, other):
        return self.mass > other.mass

    def __le__(self, other):
        return self.mass <= other.mass

    def __ge__(self, other):
        return self.mass >= other.mass

    def __eq__(self, other):
        return self.mass == other.mass


class Dog(Animal):
    def __init__(self, age: int, mass: float, sex: str):
        super().__init__('canis familiaris', age, mass, sex)

    def bark(self):
        if self.mass < 10:
            for i in range(max(self.age, 10)):
                print('woof.')
        else:
            for i in range(max(self.age, 20)):
                print('WOOF!')

    def walk(self):
        if self.age <= 1:
            print("Lets go for a walk twice a day")
        elif 6 > self.age > 1:
            print('Lets go for a walk 3 times a day!')
        else:
            print('Just stay at home, I am tried already.')

    def __repr__(self) -> str:
        self.bark()
        return f'Hi. I am a dog of age {self.age}'


class Husky(Dog):
    def __init__(self, age: int, mass: float, sex: str):
        super().__init__(age, mass, sex)

    def bark(self):
        self._howl()

    def _howl(self):
        if self.sex == "M":
            if self.age < 5:
                for i in range(max(self.age, 5)):
                    print('owooooo')
            else:
                for i in range(max(self.age, 10)):
                    print('owooooo')
        else:
            if self.age < 5:
                for i in range(max(self.age, 7)):
                    print('OWOOOO!')
            else:
                for i in range(max(self.age, 12)):
                    print('OWOOOO!')


class Cat(Animal):
    def __init__(self, age: int, mass: float, sex: str, color: str):
        super().__init__('felis catus', age, mass, sex)
        self.color: str = color

    def rub(self):
        if self.age < 2:
            print('please rub me as much as you can!')
        else:
            print('LEAVE ME ALONE!')

    def __repr__(self):
        return f'Hi. I am a cat of age {self.age}'


my_dog = Dog(2, 6.5, 'M')
print(my_dog)
my_cat = Cat(5, 2.2, "M", 'white')
print(my_cat)