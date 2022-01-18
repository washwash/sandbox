from typing import List
from decimal import Decimal
from enum import Enum


class MeasurmentUnit(Enum):
    GRAM = 'gram'
    LITER = 'liter'
    PIECE = 'piece'


class Measurment:
    measurement: MeasurmentUnit
    quantity: Decimal

    def __str__(self):
        return f'{self.quantity} {self.measurement.value}'


class Kitchen:
    products: List[Product]
    recipes: List[Recipe]


class Product:
    name: str

    def __str__(self):
        return self.name


class Shelf:
    product: Product
    measurement: Measurment

    def __str__(self):
        return f'{self.product} ({self.measurment})'

class Ingredient:
    shelf: Shelf
    measurement: Measurment

    def __str__(self):
        return f'{self.shelf} ({self.measurment})'

    #def bind(self, ):

class Recipe:
    ingredients: List[Ingredient]
    description: str
    name: str

    def __init__(self, name, ingredients, description=None):
        self.name = name
        self.ingredients = ingredients
        self.description = description

    def bind_ingredients(self):
        for ingredient in self.ingredients:
            ingredient.bind(self)

## Client code
# define abstract users products
penne = Product("penne")
spaghetti = Product("spaghetti")
pesto_shop = Product("Pesto from shop")

# add some value to abstract products and make them tangible
penne_shelf = Shelf(
    penne,
    Measurment(measurement=MeasurmentUnit.GRAM.value, quantity=Decimal(1000))
)

spaghetti_shelf = Shelf(
    spaghetti,
    Measurment(measurement=MeasurmentUnit.GRAM.value, quantity=Decimal(200))
)

pesto_shop_shelf = Shelf(
    pesto_shop,
    Measurment(measurement=MeasurmentUnit.PIECE.value, quantity=Decimal(1))
)

# add actual products in the kitchen to some recepies and dishes
pesto_homemade = Recipe("Pesto home made")

ingredients = [
    Ingredient(
        shelf=pesto_shop_shelf,
        measurment=Measurment(
            measurement=MeasurmentUnit.PIECE.value,
            quantity=Decimal(1)
        )
    ),
    Ingredient(
        shelf=penne_shelf,
        measurment=Measurment(
            measurement=MeasurmentUnit.GRAM.value,
            quantity=Decimal(250)
        )
    )
]
pasta_pesto_dish = Recipe("Pasta pesto shop", ingredients=ingredients)
