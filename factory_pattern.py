from enum import Enum
from abc import ABC, abstractmethod

# interface class

class Burgers(Enum):
  CHEESE = "CHEESE"
  DELUXECHEESE = "DELUXECHEESE"
  VEGAN = "VEGAN"
  DELUXEVEGAN = "DELUXVEGAN"

class Burger(ABC):

  def __init__(self):
    self.name = ""
    self.bread = ""
    self.sauce = ""
    self.toppings = []

  @abstractmethod
  def prepare(self):
    pass

  @abstractmethod
  def cook(self):
    pass

  @abstractmethod
  def serve(self):
    pass

  def get_name(self):
    return self.name

class CheeseBurger(Burger):

  def __init__(self):
    super().__init__()
    self.name = "Cheese Burger"

  def prepare(self):
    pass

  def cook(self):
    pass

  def serve(self):
    pass

class DeluxeCheeseBurger(Burger):

  def __init__(self):
    super().__init__()
    self.name = "Deluxe Cheese Burger"

  def prepare(self):
    pass

  def cook(self):
    pass

  def serve(self):
    pass

class VeganBurger(Burger):

  def __init__(self):
    super().__init__()
    self.name = "DeluxeVegan Burger"

  def prepare(self):
    pass

  def cook(self):
    pass

  def serve(self):
    pass

class BurgerStore(ABC):

  @abstractmethod
  def create_burger(self, item):
    pass

  def order_burger(self, item):
    burger = self.create_burger(item)
    print(f"--- Making a {burger.get_name()} ---")
    burger.prepare()
    burger.cook()
    burger.serve()
    return burger

class CheeseBurgerStore(BurgerStore):
  def create_burger(self, item):
    if item == Burgers.CHEESE:
      return CheeseBurger()
    elif item == Burgers.DELUXECHEESE:
      return DeluxeCheeseBurger()
    else:
      return None

class VeganBurgerStore(BurgerStore):
  def create_burger(self, item):
    if item == Burgers.VEGAN:
      return VeganBurger()
    elif item == Burgers.DELUXEVEGAN:
      return DeluxeVeganBurger()
    else:
      return None


cheese_store = CheeseBurgerStore()
vegan_store = VeganBurgerStore()

burger = cheese_store.order_burger(Burgers.CHEESE)
print(f"Ethan ordered a {burger.get_name()}")
burger = vegan_store.order_burger(Burgers.VEGAN)
print(f"Joel ordered a {burger.get_name()}")