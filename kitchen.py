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
    measuremen: Measurmen

    def __str__(self):
        return f'{self.product} ({self.measurment})'

class Ingredient:
    shelf: Shelf
    measuremen: Measurmen

    def __str__(self):
        return f'{self.shelf} ({self.measurment})'

class Recipe:
    ingredients: List[Ingredient]
    description: str
    name: str
