from typing import List
from decimal import Decimal
from enum import Enum


class MeasurmentUnit(Enum):
    GRAM = 'gram'
    LITER = 'liter'
    PIECE = 'piece'


class Measurment:
    unit: MeasurmentUnit
    value: Decimal

    def __init__(self, unit: MeasurmentUnit, value: Decimal):
        self.unit = unit
        self.value = value

    def __str__(self):
        return f'{self.value} {self.unit.value}'


class Subject:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._subscribers = set()

    def attach(self, observer: 'Observer'):
        self._subscribers.add(observer)

    def detach(self, observer: 'Observer'):
        self._subscribers.remove(observer)

    def notify(self):
        for sub in self._subscribers:
            sub.update(self)

class Observer:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._subjects = set()

    def update(self, subject: Subject):
        pass

    def subscribe(self, subjects: List[Subject]):
        for subject in subjects:
            self._subjects.add(subject)
            subject.attach(self)


class Kitchen:
    products: List['Product']
    shelfs: List['Shelf']
    recipes: List['Recipe']


class Product:
    id: str
    name: str

    def __init__(self, name: str):
        self.name = name
        self.id = 1

    def __str__(self):
        return f'{self.id} self.name'


class Shelf(Subject):
    product: Product
    left: Measurment

    def __init__(self, product: Product, left: Measurment):
        super().__init__()
        self.product = product
        self.left = left

    def __str__(self):
        return f'{self.product} ({self.left})'

    def remove(self, quantity: Measurment):
        # do removing from shelf
        # and then notify subscribers that amount was changed
        print(f'{self} I am notifying!')
        self.notify()


class Ingredient(Subject, Observer):
    shelf: Shelf
    measurement: Measurment

    def __init__(self, shelf: Shelf, measurment: Measurment):
        super().__init__()
        self.shelf = shelf
        self.measurement = measurment
        self.subscribe([shelf, ])
        
    def __str__(self):
        return f'{self.shelf} ({self.measurement})'

    def update(self, subject: Subject):
        print(f'{self} just passing...')
        self.notify()


class Recipe(Observer):
    ingredients: List[Ingredient]
    description: str
    name: str

    def __init__(self, name, ingredients: List[Ingredient], description=None):
        super().__init__()
        self.name = name
        self.ingredients = ingredients
        self.description = description

        self.subscribe(ingredients)
        self.reload_state()

    def __str__(self):
        return self.name

    def update(self, subject: Subject):
        self.reload_state()

    def reload_state(self):
        # check conditions to complete recipe
        # go though ingredients and check amount on shelfs
        print(f"{self} - I'm reloading")


## Client code
# define abstract users products
penne = Product("penne")
spaghetti = Product("spaghetti")
pesto_shop = Product("Pesto from shop")

# add some value to abstract products and make them tangible
penne_shelf = Shelf(
    penne,
    Measurment(unit=MeasurmentUnit.GRAM, value=Decimal(1000))
)

spaghetti_shelf = Shelf(
    spaghetti,
    Measurment(unit=MeasurmentUnit.GRAM, value=Decimal(200))
)

pesto_shop_shelf = Shelf(
    pesto_shop,
    Measurment(unit=MeasurmentUnit.PIECE, value=Decimal(1))
)

# add actual products in the kitchen to some recepies and dishes
pesto_homemade = Recipe("Pesto home made", ingredients=[])

ingredients = [
    Ingredient(
        shelf=pesto_shop_shelf,
        measurment=Measurment(
            unit=MeasurmentUnit.PIECE,
            value=Decimal(1)
        )
    ),
    Ingredient(
        shelf=penne_shelf,
        measurment=Measurment(
            unit=MeasurmentUnit.GRAM,
            value=Decimal(250)
        )
    )
]
pasta_pesto_dish = Recipe("Pasta pesto shop", ingredients=ingredients)

# do some modifications
spaghetti_shelf.remove(Measurment(unit=MeasurmentUnit.GRAM, value=Decimal(100)))
penne_shelf.remove(Measurment(unit=MeasurmentUnit.GRAM, value=Decimal(100)))
